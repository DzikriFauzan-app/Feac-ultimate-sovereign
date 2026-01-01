#!/usr/bin/env python3
"""
core/resource_manager.py

ResourceManager: registry dan importer sederhana untuk:
 - Mesh (OBJ importer minimal)
 - Material (plain JSON-based material description)
 - Texture (binary file + hash; no external image dep)

Fitur:
 - register_resource(type, path, metadata)
 - load_mesh_from_obj(path) -> MeshResource (parsing basic OBJ)
 - get_resource(res_id) / get_by_path(path)
 - save_index() / load_index() ke assets/resources_index.json

Catatan desain:
 - Resource diidentifikasi oleh SHA1 hash dari konten sumber (atau file path jika bukan file).
 - MeshResource menyimpan geometry minimal: positions, normals, uvs, faces (tri/quad)
 - MaterialResource adalah dict berisi shader refs dan uniform defaults
 - TextureResource menyimpan path dan content hash (loader tidak membuka/canvas image)
 - Dir index default: <project_root>/assets/resources_index.json
"""

from __future__ import annotations
import os
import json
import hashlib
from typing import Dict, Any, Optional, List, Tuple

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
INDEX_PATH = os.path.join(ASSETS_DIR, "resources_index.json")

# -------------------------
# Helper utilities
# -------------------------
def ensure_assets_dir():
    os.makedirs(ASSETS_DIR, exist_ok=True)

def file_sha1(path: str, chunk_size: int = 8192) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def dict_sha1(d: Dict[str, Any]) -> str:
    # stable JSON encoding
    j = json.dumps(d, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha1(j).hexdigest()

# -------------------------
# Resource classes
# -------------------------
class Resource:
    def __init__(self, res_id: str, res_type: str, source: str, metadata: Optional[Dict[str,Any]] = None):
        self.id = res_id
        self.type = res_type
        self.source = source  # original path or descriptor
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str,Any]:
        return {"id": self.id, "type": self.type, "source": self.source, "metadata": self.metadata}

class MeshResource(Resource):
    def __init__(self, res_id: str, source: str, positions: List[Tuple[float,float,float]],
                 normals: List[Tuple[float,float,float]], uvs: List[Tuple[float,float]],
                 faces: List[Tuple[Tuple[int,int,int], ...]], metadata: Optional[Dict[str,Any]] = None):
        super().__init__(res_id, "mesh", source, metadata)
        self.positions = positions
        self.normals = normals
        self.uvs = uvs
        # faces: list of tuples of vertex refs. Each vertex ref is (v_idx, vt_idx, vn_idx) with 1-based OBJ indices or None
        self.faces = faces

    def to_dict(self) -> Dict[str,Any]:
        d = super().to_dict()
        d.update({
            "positions_count": len(self.positions),
            "normals_count": len(self.normals),
            "uvs_count": len(self.uvs),
            "faces_count": len(self.faces),
        })
        return d

class MaterialResource(Resource):
    def __init__(self, res_id: str, source: str, material_def: Dict[str,Any]):
        super().__init__(res_id, "material", source, metadata=material_def)
        self.material_def = material_def

    def to_dict(self):
        d = super().to_dict()
        d.update({"material": self.material_def})
        return d

class TextureResource(Resource):
    def __init__(self, res_id: str, source: str, size: int, hash_hex: str):
        super().__init__(res_id, "texture", source, metadata={"size": size, "hash": hash_hex})
        self.size = size
        self.hash = hash_hex

    def to_dict(self):
        d = super().to_dict()
        d.update({"size": self.size, "hash": self.hash})
        return d

# -------------------------
# OBJ importer (basic)
# -------------------------
def parse_obj(path: str):
    """
    Basic OBJ parser:
    - collects vertices (v), texcoords (vt), normals (vn)
    - reads faces (f) with arbitrary polygon size -> converted to tuples as-is
    - does not process materials (mtl)
    Returns (positions, uvs, normals, faces)
    """
    positions = []
    uvs = []
    normals = []
    faces = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            parts = ln.split()
            if not parts:
                continue
            tag = parts[0]
            if tag == "v":
                vals = tuple(float(x) for x in parts[1:4])
                positions.append(vals)
            elif tag == "vt":
                vals = tuple(float(x) for x in parts[1:3])
                uvs.append(vals)
            elif tag == "vn":
                vals = tuple(float(x) for x in parts[1:4])
                normals.append(vals)
            elif tag == "f":
                # face entries: v, v/vt, v//vn, v/vt/vn
                verts = []
                for v in parts[1:]:
                    # split by '/'
                    comp = v.split('/')
                    # convert to ints if present, keep None for missing
                    vi = int(comp[0]) if comp[0] else None
                    vti = int(comp[1]) if len(comp) > 1 and comp[1] else None
                    vni = int(comp[2]) if len(comp) > 2 and comp[2] else None
                    verts.append((vi, vti, vni))
                faces.append(tuple(verts))
    return positions, uvs, normals, faces

# -------------------------
# ResourceManager
# -------------------------
class ResourceManager:
    def __init__(self, index_path: Optional[str] = None):
        ensure_assets_dir()
        self.index_path = index_path or INDEX_PATH
        # maps id -> Resource dict (persisted minimal metadata)
        self._index: Dict[str, Dict[str,Any]] = {}
        # in-memory instances (actual Resource objects)
        self._loaded: Dict[str, Resource] = {}
        self.load_index()

    # ---- index persistence ----
    def load_index(self):
        if os.path.exists(self.index_path):
            try:
                with open(self.index_path, "r", encoding="utf-8") as f:
                    self._index = json.load(f)
            except Exception:
                self._index = {}
        else:
            self._index = {}

    def save_index(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(self._index, f, indent=2, sort_keys=True)

    # ---- registration & lookup ----
    def register_resource(self, res: Resource):
        self._loaded[res.id] = res
        self._index[res.id] = res.to_dict()
        self.save_index()
        return res.id

    def get_resource(self, res_id: str) -> Optional[Resource]:
        r = self._loaded.get(res_id)
        if r:
            return r
        md = self._index.get(res_id)
        if not md:
            return None
        # lazy rehydrate minimal resource objects (keep light)
        typ = md.get("type")
        src = md.get("source")
        if typ == "mesh":
            # no full geometry loaded — require explicit load_mesh_by_id
            return Resource(res_id, typ, src, metadata=md.get("metadata"))
        if typ == "material":
            return MaterialResource(res_id, src, md.get("metadata", {}))
        if typ == "texture":
            meta = md.get("metadata", {})
            return TextureResource(res_id, src, meta.get("size", 0), meta.get("hash"))
        return Resource(res_id, typ, src, metadata=md.get("metadata"))

    def find_by_path(self, source_path: str) -> Optional[str]:
        for rid, md in self._index.items():
            if os.path.abspath(md.get("source", "")) == os.path.abspath(source_path):
                return rid
        return None

    # ---- specialized loaders/importers ----
    def import_mesh_obj(self, path: str) -> MeshResource:
        """
        Import an OBJ file, compute SHA1-of-file as id, parse geometry, register MeshResource.
        If resource with same hash exists, return existing id.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        h = file_sha1(path)
        existing = self._index.get(h)
        if existing and existing.get("type") == "mesh":
            # if already in index and loaded, rehydrate
            loaded = self._loaded.get(h)
            if isinstance(loaded, MeshResource):
                return loaded
            # otherwise parse again and register
        # parse geometry
        positions, uvs, normals, faces = parse_obj(path)
        mesh = MeshResource(
            res_id=h,
            source=os.path.abspath(path),
            positions=positions,
            normals=normals,
            uvs=uvs,
            faces=faces,
            metadata={"file_size": os.path.getsize(path)}
        )
        self.register_resource(mesh)
        return mesh

    def load_mesh_by_id(self, res_id: str) -> Optional[MeshResource]:
        """
        If index contains mesh metadata but not loaded geometry, attempt load from source path.
        """
        idx = self._index.get(res_id)
        if not idx:
            return None
        if idx.get("type") != "mesh":
            return None
        src = idx.get("source")
        if not src or not os.path.exists(src):
            return None
        positions, uvs, normals, faces = parse_obj(src)
        mesh = MeshResource(res_id=res_id, source=src, positions=positions, normals=normals, uvs=uvs, faces=faces, metadata=idx.get("metadata"))
        self._loaded[res_id] = mesh
        return mesh

    def import_texture(self, path: str) -> TextureResource:
        """
        Register a texture by hashing file content. Does not decode or validate image.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        h = file_sha1(path)
        existing = self._index.get(h)
        if existing and existing.get("type") == "texture":
            loaded = self._loaded.get(h)
            if isinstance(loaded, TextureResource):
                return loaded
        size = os.path.getsize(path)
        tex = TextureResource(res_id=h, source=os.path.abspath(path), size=size, hash_hex=h)
        self.register_resource(tex)
        return tex

    def import_material_from_json(self, path: str) -> MaterialResource:
        """
        Load material definition from a JSON file. Material id is SHA1 of the JSON content.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        with open(path, "r", encoding="utf-8") as f:
            mat = json.load(f)
        h = dict_sha1(mat)
        existing = self._index.get(h)
        if existing and existing.get("type") == "material":
            return self.get_resource(h)
        mres = MaterialResource(res_id=h, source=os.path.abspath(path), material_def=mat)
        self.register_resource(mres)
        return mres

    # ---- convenience ----
    def list_resources(self, res_type: Optional[str] = None) -> List[Dict[str,Any]]:
        out = []
        for rid, md in self._index.items():
            if res_type is None or md.get("type") == res_type:
                out.append(md)
        return out

    def unload(self, res_id: str):
        if res_id in self._loaded:
            del self._loaded[res_id]

    def clear(self):
        self._loaded.clear()
        self._index.clear()
        try:
            os.remove(self.index_path)
        except Exception:
            pass

# -------------------------
# Simple CLI usage helper
# -------------------------
if __name__ == "__main__":
    rm = ResourceManager()
    print("Resources index loaded. Count:", len(rm._index))
    # quick demo: scan assets for obj and images
    found = []
    for root, dirs, files in os.walk(ASSETS_DIR):
        for fn in files:
            if fn.lower().endswith(".obj"):
                p = os.path.join(root, fn)
                try:
                    mesh = rm.import_mesh_obj(p)
                    print("Imported mesh:", mesh.id, fn)
                except Exception as e:
                    print("OBJ import error:", p, e)
            elif fn.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                p = os.path.join(root, fn)
                try:
                    tex = rm.import_texture(p)
                    print("Imported texture:", tex.id, fn)
                except Exception as e:
                    print("Texture import error:", p, e)
    print("Done. Total resources:", len(rm._index))
