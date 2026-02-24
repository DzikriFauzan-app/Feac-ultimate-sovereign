#!/usr/bin/env python3
"""
render/render_pass/lighting_pass.py

Lighting pass:
- Consumes g-buffer textures and produces a shaded color texture.
- Uses GPUDevice shaders when available; falls back to metadata synthesis in Mock.
"""
from __future__ import annotations
import time
from typing import Dict, Any
from render.gpu.gpu_abstraction import GPUDevice, GPUError

class LightingPass:
    def __init__(self, gpu: GPUDevice):
        self.name = "lighting"
        self.gpu = gpu
        self._out_texture = None
        self._shader = None
        self._width = 1024
        self._height = 1024
        self._initialized = False

    def _init(self):
        if self._initialized:
            return
        # simple shader sources (these are tiny but contain 'void main')
        vs = "void main() { /* vs */ }"
        fs = "void main() { /* fs */ }"
        try:
            self._shader = self.gpu.create_shader_program(vs, fs)
        except GPUError:
            self._shader = None
        # create output texture
        self._out_texture = self.gpu.create_texture(self._width, self._height, fmt="rgba8")
        self._initialized = True

    def run(self, camera, resources: Dict[str, Any]) -> Dict[str, Any]:
        self._init()
        # read gbuffer references (ids) from resources; in real GL we'd bind them
        albedo_id = resources.get("gbuffer_albedo")
        normal_id = resources.get("gbuffer_normal")
        material_id = resources.get("gbuffer_material")

        # attempt to 'apply' shader (mock: set uniform metadata)
        try:
            if self._shader:
                # in mock shader the set_uniform is a no-op for complex types
                try:
                    self._shader.set_uniform("u_time", time.time())
                except Exception:
                    pass
        except Exception:
            pass

        # create a small result marker update
        try:
            self._out_texture.update(bytes([200] * 4 * 4))
        except Exception:
            pass

        out = {
            "lit_color": getattr(self._out_texture, "id", None),
            "lit_size": (self._width, self._height),
            "lighting_used_shader": getattr(self._shader, "id", None)
        }
        return out
