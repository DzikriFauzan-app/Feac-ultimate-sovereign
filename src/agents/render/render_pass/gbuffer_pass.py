#!/usr/bin/env python3
"""
render/render_pass/gbuffer_pass.py

G-Buffer pass:
- Creates (or reuses) a framebuffer with multiple attachments (albedo, normal, material)
- In a real GL backend it would bind resources and run geometry shader; here we create textures
  and return references that downstream passes will consume.
"""
from __future__ import annotations
import time
from typing import Dict, Any
from render.gpu.gpu_abstraction import GPUDevice, GPUError, Texture, Framebuffer

class GbufferPass:
    def __init__(self, gpu: GPUDevice):
        self.name = "gbuffer"
        self.gpu = gpu
        self._fb: Framebuffer | None = None
        self._albedo: Texture | None = None
        self._normal: Texture | None = None
        self._material: Texture | None = None
        self._width = 1024
        self._height = 1024
        self._initialized = False

    def _ensure_resources(self):
        if self._initialized:
            return
        # create textures
        self._albedo = self.gpu.create_texture(self._width, self._height, fmt="rgba8")
        self._normal = self.gpu.create_texture(self._width, self._height, fmt="rgba8")
        self._material = self.gpu.create_texture(self._width, self._height, fmt="rgba8")
        # create framebuffer (mock or GL)
        self._fb = self.gpu.create_framebuffer(self._width, self._height)
        self._initialized = True

    def run(self, camera, resources: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate rendering geometry to g-buffer. In GL backend, the shader would write to attachments.
        For mock backend we just ensure textures exist and set metadata.
        """
        self._ensure_resources()
        # simulate render by writing small metadata to textures (mock will accept)
        try:
            # write a tiny pattern if possible
            w, h = self._width, self._height
            sample = bytes([128] * (4 * 4))  # small placeholder for "draw"
            # update textures minimally (no full upload to avoid heavy ops)
            self._albedo.update(sample)
            self._normal.update(sample)
            self._material.update(sample)
        except Exception:
            # ignore non-critical resource update errors in mock
            pass

        out = {
            "gbuffer_albedo": getattr(self._albedo, "id", None),
            "gbuffer_normal": getattr(self._normal, "id", None),
            "gbuffer_material": getattr(self._material, "id", None),
            "gbuffer_fbo": getattr(self._fb, "id", None),
            "gbuffer_size": (self._width, self._height),
            "gbuffer_created_at": time.time()
        }
        return out
