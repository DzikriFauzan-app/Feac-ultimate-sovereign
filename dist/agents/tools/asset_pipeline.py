#!/usr/bin/env python3
"""
tools/asset_pipeline.py

Asset Pipeline lengkap untuk NeoEngine:
 - AssetWatcher: memonitor changes di assets/
 - AssetIndexer: menata ulang, memvalidasi, dan mensinkronkan resource index
 - AssetPipelineCLI: interface CLI untuk developer

Fitur:
 - Pendeteksian file baru, deleted, dan updated (berbasis SHA1 per file)
 - Auto-import (mesh OBJ, texture, material JSON) terhubung ke ResourceManager
 - Output log terstruktur untuk BuildAgent / Bridge
"""

from __future__ import annotations
import os
import time
import json
import threading
from typing import Dict, Callable, List, Optional

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
INDEX_EXPORT = os.path.join(ASSETS_DIR, "assets_export.json")

# import resource manager
from core.resource_manager import ResourceManager, file_sha1


# -------------------------------------------------------
# Utility
# -------------------------------------------------------
def walk_files(base: str) -> List[str]:
    out = []
    for root, dirs, files in os.walk(base):
        for fn in files:
            out.append(os.path.join(root, fn))
    return out


# -------------------------------------------------------
# AssetIndexer
# -------------------------------------------------------
class AssetIndexer:
    """
    Menghasilkan index file original, resource id, jenis file, dan metadata lainnya.
    Dapat dipakai editor (UI) atau untuk debugging.
    """
    def __init__(self, rm: ResourceManager):
        self.rm = rm

    def build_export(self):
        export = {
            "root": ASSETS_DIR,
            "resources": [],
            "files": [],
        }

        # file list
        for f in walk_files(ASSETS_DIR):
            export["files"].append({
                "path": f,
                "size": os.path.getsize(f)
            })

        # resource list
        for r in self.rm.list_resources():
            export["resources"].append(r)

        with open(INDEX_EXPORT, "w", encoding="utf-8") as f:
            json.dump(export, f, indent=2, sort_keys=True)
        return INDEX_EXPORT


# -------------------------------------------------------
# AssetWatcher
# -------------------------------------------------------
class AssetWatcher(threading.Thread):
    """
    Watching manual tanpa library eksternal.
    Loop 1 detik untuk mendeteksi:
      - File baru
      - File terhapus
      - File berubah hash
    """
    def __init__(self, rm: ResourceManager, callback: Optional[Callable[[Dict],None]] = None):
        super().__init__(daemon=True)
        self.rm = rm
        self.callback = callback
        self.running = False
        self.state: Dict[str, str] = {}  # {path: sha1}

    def scan_once(self):
        current_files = {}
        report = {
            "created": [],
            "deleted": [],
            "modified": [],
            "timestamp": time.time()
        }

        # scan
        for f in walk_files(ASSETS_DIR):
            try:
                h = file_sha1(f)
                current_files[f] = h
            except Exception:
                pass

        # detect created
        for f, h in current_files.items():
            if f not in self.state:
                report["created"].append(f)
            else:
                if self.state[f] != h:
                    report["modified"].append(f)

        # detect deleted
        for f in list(self.state.keys()):
            if f not in current_files:
                report["deleted"].append(f)

        # update state
        self.state = current_files

        return report

    def process_report(self, rpt: Dict):
        """Menggunakan ResourceManager untuk import otomatis."""
        created = rpt["created"]
        modified = rpt["modified"]
        deleted = rpt["deleted"]

        events = []

        # created & modified -> import ulang
        for f in created + modified:
            low = f.lower()
            try:
                if low.endswith(".obj"):
                    mesh = self.rm.import_mesh_obj(f)
                    events.append({"type": "mesh", "file": f, "id": mesh.id})
                elif low.endswith((".png", ".jpg", ".jpeg", ".webp")):
                    tex = self.rm.import_texture(f)
                    events.append({"type": "texture", "file": f, "id": tex.id})
                elif low.endswith(".json"):
                    mat = self.rm.import_material_from_json(f)
                    events.append({"type": "material", "file": f, "id": mat.id})
            except Exception as e:
                events.append({"type": "error", "file": f, "error": str(e)})

        # deleted -> resource tidak langsung dihapus (index tetap)
        for f in deleted:
            events.append({"type": "deleted", "file": f})

        if self.callback:
            for e in events:
                self.callback(e)

    def run(self):
        self.running = True
        while self.running:
            rpt = self.scan_once()
            self.process_report(rpt)
            time.sleep(1.0)

    def stop(self):
        self.running = False


# -------------------------------------------------------
# AssetPipelineCLI
# -------------------------------------------------------
class AssetPipelineCLI:
    """
    Perintah CLI:
      - scan     : scan full dan impor semua
      - watch    : jalankan watcher realtime
      - list     : list resource
      - export   : buat assets_export.json
      - clear    : hapus semua resource index
    """
    def __init__(self):
        self.rm = ResourceManager()
        self.indexer = AssetIndexer(self.rm)

    def cmd_scan(self):
        print("Scanning assets...")
        files = walk_files(ASSETS_DIR)
        for f in files:
            low = f.lower()
            try:
                if low.endswith(".obj"):
                    m = self.rm.import_mesh_obj(f)
                    print("Imported mesh:", m.id, os.path.basename(f))
                elif low.endswith((".png", ".jpg", ".jpeg", ".webp")):
                    t = self.rm.import_texture(f)
                    print("Imported texture:", t.id, os.path.basename(f))
                elif low.endswith(".json"):
                    mat = self.rm.import_material_from_json(f)
                    print("Imported material:", mat.id, os.path.basename(f))
            except Exception as e:
                print("Error:", f, e)
        print("Done.")

    def cmd_watch(self):
        print("Starting AssetWatcher...")
        def cb(ev):
            print("[EVENT]", ev)
        w = AssetWatcher(self.rm, callback=cb)
        w.start()
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Stopping watcher...")
            w.stop()

    def cmd_list(self):
        print("Resources:")
        for r in self.rm.list_resources():
            print("-", r["type"], r["id"], r.get("source", ""))

    def cmd_export(self):
        path = self.indexer.build_export()
        print("Export saved to:", path)

    def cmd_clear(self):
        confirm = input("Clear all resource index? [y/N] ")
        if confirm.lower() == "y":
            self.rm.clear()
            print("Index cleared.")

    def run(self, argv: List[str]):
        if not argv:
            print("Usage: asset_pipeline.py [scan|watch|list|export|clear]")
            return

        cmd = argv[0]

        if cmd == "scan":
            self.cmd_scan()
        elif cmd == "watch":
            self.cmd_watch()
        elif cmd == "list":
            self.cmd_list()
        elif cmd == "export":
            self.cmd_export()
        elif cmd == "clear":
            self.cmd_clear()
        else:
            print("Unknown command:", cmd)
            print("Valid: scan, watch, list, export, clear")


# -------------------------------------------------------
# Main CLI Runner
# -------------------------------------------------------
if __name__ == "__main__":
    import sys
    cli = AssetPipelineCLI()
    cli.run(sys.argv[1:])
