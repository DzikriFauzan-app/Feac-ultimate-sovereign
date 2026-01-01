#!/usr/bin/env python3
"""
render_manager.py
High-level rendering manager:
- shader cache
- material registry
- pipeline builder
- bake utilities (shadow / GI placeholders)
"""
import asyncio
from typing import Dict, Any, Optional
from .render_context import RenderContext, RenderContextError

class RenderManagerError(Exception):
    pass

class RenderManager:
    def __init__(self, db=None, bus=None, backend: str = "opengl"):
        self.db = db
        self.bus = bus
        self.context = RenderContext(backend=backend)
        self.context.init()
        self.shader_cache: Dict[str, Dict[str, Any]] = {}
        self.materials: Dict[str, Dict[str, Any]] = {}
        self.pipelines: Dict[str, Dict[str, Any]] = {}

    async def compile_shader(self, name: str, source: str, stage: str = "fragment"):
        shader = await self.context.compile_shader(name, source, stage)
        self.shader_cache[name] = shader
        return shader

    def create_material(self, name: str, params: Dict[str, Any]):
        mat = {"name": name, "params": params, "version": 1}
        self.materials[name] = mat
        return mat

    def build_pipeline(self, pipeline_name: str, config: Dict[str, Any]):
        pipeline = self.context.create_pipeline(pipeline_name, config)
        self.pipelines[pipeline_name] = pipeline
        return pipeline

    async def reload_pipeline(self, pipeline_name: str, new_config: Dict[str, Any]):
        if pipeline_name not in self.pipelines:
            raise RenderManagerError("pipeline missing")
        pipeline = self.context.create_pipeline(pipeline_name, new_config)
        self.pipelines[pipeline_name] = pipeline
        # broadcast via bus if available
        if self.bus:
            await self.bus.publish("pipeline_reloaded", {"name": pipeline_name, "id": pipeline["id"]})
        return pipeline

    async def dispatch(self, pipeline_name: str, inputs: Dict[str, Any], target: Optional[str] = None):
        return await self.context.dispatch(pipeline_name, inputs, target)

    async def capture(self, fb_name: str):
        return await self.context.capture(fb_name)

    async def bake_shadow_map(self, scene_desc: Dict[str, Any], size: int = 2048):
        # placeholder simulate bake
        await asyncio.sleep(0.1)
        return {"status": "ok", "size": size, "file": f"shadow_{size}.exr"}

    async def bake_gi_probe(self, scene_desc: Dict[str, Any], quality: str = "low"):
        await asyncio.sleep(0.2)
        return {"status": "ok", "quality": quality}
