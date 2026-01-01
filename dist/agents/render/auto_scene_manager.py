#!/usr/bin/env python3
"""
render/auto_scene_manager.py

Scene manager for NeoEngine render subsystem.

Features:
- Entity / component minimal system (Transform, Camera, MeshRenderer)
- Scene container with add/remove/find operations
- Simple distance-based culling
- Pipeline registry and integration with RenderPipeline.render(camera)
- Simple load/save (JSON)
- Deterministic, dependency-free (stdlib only) and ready to be called by RenderAgent

Usage (example):
    from render.auto_scene_manager import SceneManager, Camera, MeshRenderer, Transform
    sm = SceneManager()
    cam = Camera(name="main_cam", position=(0,2,5), fov=60)
    e = sm.create_entity("tree_01")
    e.add_component(Transform(position=(2,0,0)))
    e.add_component(MeshRenderer(mesh_name="tree.obj", bounding_radius=1.2))
    sm.register_pipeline("deferred_pbr", config={"passes":["gbuffer","lighting","post"]})
    out = sm.render_frame("deferred_pbr", camera_name="main_cam")
"""

from __future__ import annotations
import time
import json
import math
import uuid
from typing import Dict, Any, List, Optional, Tuple

# Import RenderPipeline (assumes render/render_pipeline.py exists)
try:
    from render.render_pipeline import RenderPipeline
except Exception:
    # defensive fallback: lightweight internal stub that mirrors expected API
    class RenderPipeline:
        def __init__(self, name: str, config: Dict):
            self.name = name
            self.config = config or {}
        def render(self, camera):
            return {"pipeline": self.name, "passes_executed": [], "resources_snapshot": {}, "rendered_at": time.time()}

# ---------------------------
# Basic component primitives
# ---------------------------
class Transform:
    __slots__ = ("position","rotation","scale")
    def __init__(self, position: Tuple[float,float,float]=(0,0,0),
                 rotation: Tuple[float,float,float]=(0,0,0),
                 scale: Tuple[float,float,float]=(1,1,1)):
        self.position = tuple(float(x) for x in position)
        self.rotation = tuple(float(x) for x in rotation)
        self.scale = tuple(float(x) for x in scale)

class Camera:
    """
    Minimal camera object used by render pipeline.
    - position: tuple
    - target: optional point camera looks at
    - fov: degrees
    - near/far: clipping planes
    """
    def __init__(self, name: str="camera", position=(0,0,0), target=(0,0, -1),
                 fov: float=60.0, near: float=0.1, far: float=1000.0):
        self.id = f"cam-{uuid.uuid4().hex[:8]}"
        self.name = name
        self.position = tuple(float(x) for x in position)
        self.target = tuple(float(x) for x in target)
        self.fov = float(fov)
        self.near = float(near)
        self.far = float(far)
        self.enabled = True

    def distance_to(self, point: Tuple[float,float,float]) -> float:
        dx = self.position[0] - point[0]
        dy = self.position[1] - point[1]
        dz = self.position[2] - point[2]
        return math.sqrt(dx*dx + dy*dy + dz*dz)

class MeshRenderer:
    """
    Minimal mesh renderer component.
    - mesh_name: identifier for mesh resource (string)
    - bounding_radius: approximate radius for culling
    - visible: flag
    """
    def __init__(self, mesh_name: str, bounding_radius: float=1.0):
        self.mesh_name = mesh_name
        self.bounding_radius = float(bounding_radius)
        self.visible = True
        self.material = None  # optional material reference

# ---------------------------
# Entity & Scene
# ---------------------------
class Entity:
    def __init__(self, name: str):
        self.id = f"ent-{uuid.uuid4().hex[:8]}"
        self.name = name
        self.components: Dict[str, Any] = {}
        self.tags: List[str] = []

    def add_component(self, component):
        self.components[component.__class__.__name__] = component
        return component

    def get_component(self, cls):
        return self.components.get(cls.__name__)

    def remove_component(self, cls):
        self.components.pop(cls.__name__, None)

    def has_component(self, cls):
        return cls.__name__ in self.components

class Scene:
    def __init__(self, name: str="default"):
        self.name = name
        self.entities: Dict[str, Entity] = {}
        self.created_at = time.time()

    def create_entity(self, name: str) -> Entity:
        e = Entity(name)
        self.entities[e.id] = e
        return e

    def remove_entity(self, entity_id: str):
        if entity_id in self.entities:
            del self.entities[entity_id]

    def find_by_name(self, name: str) -> Optional[Entity]:
        for e in self.entities.values():
            if e.name == name:
                return e
        return None

    def all_entities(self) -> List[Entity]:
        return list(self.entities.values())

    def to_dict(self) -> Dict[str,Any]:
        # minimal serialization
        ent_list = []
        for e in self.entities.values():
            comps = {}
            for k,v in e.components.items():
                if isinstance(v, Transform):
                    comps[k] = {"position": v.position, "rotation": v.rotation, "scale": v.scale}
                elif isinstance(v, Camera):
                    comps[k] = {"name": v.name, "position": v.position, "target": v.target, "fov": v.fov, "near": v.near, "far": v.far}
                elif isinstance(v, MeshRenderer):
                    comps[k] = {"mesh_name": v.mesh_name, "bounding_radius": v.bounding_radius, "visible": v.visible}
                else:
                    # best-effort repr
                    comps[k] = repr(v)
            ent_list.append({"id": e.id, "name": e.name, "components": comps, "tags": e.tags})
        return {"name": self.name, "created_at": self.created_at, "entities": ent_list}

    @staticmethod
    def from_dict(data: Dict[str,Any]) -> "Scene":
        s = Scene(name=data.get("name","scene"))
        for ent in data.get("entities", []):
            e = Entity(ent.get("name","entity"))
            e.id = ent.get("id", e.id)
            for cname, cdata in ent.get("components", {}).items():
                if cname == "Transform":
                    e.add_component(Transform(position=tuple(cdata.get("position",(0,0,0))),
                                              rotation=tuple(cdata.get("rotation",(0,0,0))),
                                              scale=tuple(cdata.get("scale",(1,1,1)))))
                elif cname == "Camera":
                    cam = Camera(name=cdata.get("name","camera"),
                                 position=tuple(cdata.get("position",(0,0,0))),
                                 target=tuple(cdata.get("target",(0,0,-1))),
                                 fov=cdata.get("fov",60.0),
                                 near=cdata.get("near",0.1),
                                 far=cdata.get("far",1000.0))
                    e.add_component(cam)
                elif cname == "MeshRenderer":
                    e.add_component(MeshRenderer(mesh_name=cdata.get("mesh_name","mesh"),
                                                 bounding_radius=cdata.get("bounding_radius",1.0)))
                else:
                    # ignore unknown components
                    pass
            e.tags = ent.get("tags", [])
            s.entities[e.id] = e
        return s

# ---------------------------
# Scene Manager
# ---------------------------
class SceneManager:
    """
    Manages a set of scenes and pipelines. Lightweight and synchronous.
    """
    def __init__(self):
        self.scenes: Dict[str, Scene] = {}
        self.pipelines: Dict[str, RenderPipeline] = {}
        self.cameras: Dict[str, Camera] = {}
        self._active_scene: Optional[str] = None

    # Scene lifecycle
    def create_scene(self, name: str="scene") -> Scene:
        s = Scene(name)
        self.scenes[name] = s
        if self._active_scene is None:
            self._active_scene = name
        return s

    def set_active_scene(self, name: str):
        if name not in self.scenes:
            raise KeyError(f"scene not found: {name}")
        self._active_scene = name

    def get_active_scene(self) -> Scene:
        if self._active_scene is None:
            return self.create_scene("default")
        return self.scenes[self._active_scene]

    def remove_scene(self, name: str):
        if name in self.scenes:
            del self.scenes[name]
            if self._active_scene == name:
                self._active_scene = None

    # pipeline management
    def register_pipeline(self, name: str, config: Dict):
        self.pipelines[name] = RenderPipeline(name, config)
        return self.pipelines[name]

    def unregister_pipeline(self, name: str):
        self.pipelines.pop(name, None)

    def get_pipeline(self, name: str) -> Optional[RenderPipeline]:
        return self.pipelines.get(name)

    # camera registry
    def register_camera(self, camera: Camera):
        self.cameras[camera.name] = camera
        return camera

    def get_camera(self, name: str) -> Optional[Camera]:
        return self.cameras.get(name)

    def remove_camera(self, name: str):
        self.cameras.pop(name, None)

    # Entity convenience
    def create_entity(self, name: str) -> Entity:
        return self.get_active_scene().create_entity(name)

    # Culling & update
    def _distance_cull(self, camera: Camera, entity: Entity, max_distance: Optional[float]=None) -> bool:
        """
        True if entity should be rendered (passes culling).
        Default cull: compare entity transform position to camera distance + bounding radius.
        """
        tr: Transform = entity.get_component(Transform)
        mr: MeshRenderer = entity.get_component(MeshRenderer)
        if not mr or not tr:
            # not renderable -> do not include
            return False
        if not mr.visible:
            return False
        if max_distance is None:
            # use camera.far as max distance
            max_distance = camera.far
        dist = camera.distance_to(tr.position)
        # include if within far plane + radius and beyond near plane
        if dist - mr.bounding_radius > max_distance:
            return False
        if dist + mr.bounding_radius < camera.near:
            return False
        return True

    def gather_renderables(self, camera: Camera, max_distance: Optional[float]=None) -> List[Dict]:
        """
        Returns list of dict {entity, transform, mesh, distance} for render pipeline.
        """
        scene = self.get_active_scene()
        out = []
        for e in scene.all_entities():
            if self._distance_cull(camera, e, max_distance):
                tr: Transform = e.get_component(Transform)
                mr: MeshRenderer = e.get_component(MeshRenderer)
                dist = camera.distance_to(tr.position)
                out.append({"entity": e, "transform": tr, "mesh": mr, "distance": dist})
        # sort by distance (near -> far) could be useful for transparency ordering
        out.sort(key=lambda x: x["distance"])
        return out

    # Frame pipeline
    def render_frame(self, pipeline_name: str, camera_name: str, extra_context: Optional[Dict]=None) -> Dict:
        """
        Prepare frame and call pipeline.render(camera). Returns pipeline result dict.
        Steps:
         - validate pipeline & camera
         - update per-frame resources
         - gather visible renderables and attach to camera.resources
         - call RenderPipeline.render(camera)
        """
        if pipeline_name not in self.pipelines:
            raise KeyError(f"pipeline not registered: {pipeline_name}")
        pipe = self.pipelines[pipeline_name]
        cam = self.get_camera(camera_name)
        if cam is None:
            raise KeyError(f"camera not found: {camera_name}")

        # Build camera resources object (can be extended)
        camera_resources = {
            "id": cam.id,
            "name": cam.name,
            "position": cam.position,
            "target": cam.target,
            "fov": cam.fov,
            "near": cam.near,
            "far": cam.far,
            "timestamp": time.time(),
            "renderables": []
        }
        renderables = self.gather_renderables(cam)
        for r in renderables:
            # minimal renderable description
            camera_resources["renderables"].append({
                "entity_id": r["entity"].id,
                "name": r["entity"].name,
                "mesh": r["mesh"].mesh_name,
                "position": r["transform"].position,
                "bounding_radius": r["mesh"].bounding_radius,
                "distance": r["distance"]
            })

        # attach extra context
        if extra_context:
            camera_resources.update(extra_context)

        # call pipeline
        result = pipe.render(camera_resources)
        # Add some meta info
        if isinstance(result, dict):
            result.setdefault("camera", camera_resources["name"])
            result.setdefault("pipeline", pipe.name)
            result.setdefault("renderable_count", len(camera_resources["renderables"]))
            result.setdefault("rendered_at", time.time())
        return result

    # Save/load
    def save_scene(self, scene_name: str, path: str):
        if scene_name not in self.scenes:
            raise KeyError("scene not found")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.scenes[scene_name].to_dict(), f, indent=2)

    def load_scene(self, path: str) -> Scene:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        s = Scene.from_dict(data)
        self.scenes[s.name] = s
        if self._active_scene is None:
            self._active_scene = s.name
        # register any Camera components into camera registry
        for e in s.all_entities():
            cam: Camera = e.get_component(Camera)
            if cam:
                self.register_camera(cam)
        return s

# ---------------------------
# Single global instance (convenience)
# ---------------------------
_global_scene_manager: Optional[SceneManager] = None

def get_scene_manager() -> SceneManager:
    global _global_scene_manager
    if _global_scene_manager is None:
        _global_scene_manager = SceneManager()
    return _global_scene_manager

# ---------------------------
# Module test when run directly
# ---------------------------
if __name__ == "__main__":
    # quick smoke test
    sm = get_scene_manager()
    sm.create_scene("test")
    cam = Camera(name="main", position=(0,1.5,5))
    sm.register_camera(cam)
    e = sm.create_entity("cube01")
    e.add_component(Transform(position=(0,0,0)))
    e.add_component(MeshRenderer(mesh_name="cube", bounding_radius=0.5))
    sm.register_pipeline("testpipe", config={"passes":["gbuffer","lighting"]})
    out = sm.render_frame("testpipe", camera_name="main")
    print("SMOKE:", out)
