#!/usr/bin/env python3
"""
core/renderer.py

Renderer Manager untuk NeoEngine.
Menghubungkan:
    Scene → RenderContext → RenderPipeline

Tugas:
- Mengambil camera, renderable, light dari Scene.
- Menyiapkan RenderContext.
- Menjalankan pipeline.render().
- Mengembalikan hasil (sementara dict; nanti bisa GPU buffer, image, frame, dsb).

Module ini sudah siap untuk:
- CPU raster minimal
- Software renderer
- Integrasi GPU (Vulkan/Metal/OpenGL) nanti
"""

from __future__ import annotations
from typing import Any, Dict
from .render_context import RenderContext
from .scene import Scene
from ..render.render_pipeline import RenderPipeline


class Renderer:
    def __init__(self):
        self.pipeline = RenderPipeline()
        self.context = RenderContext()

    def render_scene(self, scene: Scene) -> Dict[str, Any]:
        """
        Render satu frame based on Scene aktif.
        Mengembalikan output dict dari RenderPipeline.render().
        """

        if not scene.is_active():
            return {"status": "no-scene"}

        # reset context
        self.context.clear()

        # isi context (data dari Scene)
        self.context.cameras = scene.get_cameras()
        self.context.renderables = scene.get_renderables()
        self.context.lights = scene.get_lights()

        # metadata
        self.context.metadata["camera_count"] = len(self.context.cameras)
        self.context.metadata["renderable_count"] = len(self.context.renderables)
        self.context.metadata["light_count"] = len(self.context.lights)

        # jalankan pipeline
        result = self.pipeline.render(
            cameras=self.context.cameras,
            renderables=self.context.renderables,
            lights=self.context.lights
        )

        # merge metadata into result
        result["metadata"] = self.context.metadata
        return result
