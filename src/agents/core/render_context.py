#!/usr/bin/env python3
"""
RenderContext
--------------
Objek ringan yang dipakai Renderer → RenderPipeline.

Tujuan:
- Menyatukan semua data hasil query Scene (camera, mesh, light).
- Mengemasnya menjadi satu objek sebelum dikirim ke RenderPipeline.render().
- Agar RenderPipeline tetap bersih dan modular.
"""

from typing import Dict, List, Any

class RenderContext:
    def __init__(self):
        self.cameras: List[Dict[str, Any]] = []
        self.renderables: List[Dict[str, Any]] = []
        self.lights: List[Dict[str, Any]] = []
        self.metadata: Dict[str, Any] = {}  # tambahan, bebas (statistik, debug, dsb)

    def clear(self):
        self.cameras.clear()
        self.renderables.clear()
        self.lights.clear()
        self.metadata.clear()

    def to_dict(self):
        return {
            "cameras": self.cameras,
            "renderables": self.renderables,
            "lights": self.lights,
            "metadata": self.metadata
        }
