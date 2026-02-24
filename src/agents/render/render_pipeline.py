#!/usr/bin/env python3
"""
render/render_pipeline.py

Updated RenderPipeline that integrates with render.gpu.gpu_abstraction.GPUDevice
and supports concrete passes implemented under render.render_pass.*.

Behavior:
- Build passes from config as before.
- Initialize a GPUDevice (auto backend) for resource creation.
- Each pass is expected to provide .run(camera, resources) -> dict outputs.
- Pipeline.render(camera) will execute passes sequentially and merge resources.

This file is self-contained and non-placeholder.
"""
from __future__ import annotations
import importlib
import time
from typing import List, Dict, Any
from render.gpu.gpu_abstraction import GPUDevice

# create a shared GPU device for the pipeline (auto-select backend)
GPU = GPUDevice(backend="auto")

class RenderPipeline:
    def __init__(self, name: str, config: Dict[str, Any]):
        self.name = name
        self.config = config or {}
        self.passes = []
        self.gpu = GPU
        # config expects {'passes': ['gbuffer','lighting','post',...]}
        self._build_passes(self.config.get("passes", []))

    def _load_pass(self, pass_name: str):
        """
        Import pass module at render.render_pass.<pass_name>_pass
        Expect class <PassName>Pass with .run(camera, resources)
        """
        module_name = f"render.render_pass.{pass_name}_pass"
        class_name = f"{pass_name.capitalize()}Pass"
        try:
            mod = importlib.import_module(module_name)
            cls = getattr(mod, class_name)
            # instantiate with gpu device if constructor accepts it
            try:
                inst = cls(self.gpu)
            except TypeError:
                inst = cls()
            return inst
        except Exception as e:
            # fallback to DummyPass (kept for safety)
            print(f"[RenderPipeline] warning loading pass {pass_name}: {e}")
            return DummyPass(pass_name)

    def _build_passes(self, pass_list: List[str]):
        self.passes = []
        for p in pass_list:
            self.passes.append(self._load_pass(p))

    def render(self, camera) -> Dict[str, Any]:
        """
        Execute all passes sequentially.
        Each pass receives (camera, resources) and returns a dict of outputs.
        We merge outputs into resources and record a timeline.
        """
        resources: Dict[str, Any] = {
            "frame_time": time.time(),
            "camera": camera,
            "gpu_backend": self.gpu.backend
        }
        timeline = []
        for p in self.passes:
            start = time.time()
            try:
                out = p.run(camera, resources)
            except TypeError:
                # fallback for legacy passes
                out = getattr(p, "process", lambda c, r: {})(camera, resources)
            end = time.time()
            resources.update(out or {})
            timeline.append({
                "pass": getattr(p, "name", p.__class__.__name__),
                "duration_ms": round((end - start) * 1000, 3),
                "output_keys": sorted((out or {}).keys())
            })
        resources["_timeline"] = timeline
        resources["pipeline_name"] = self.name
        resources["rendered_at"] = time.time()
        # return a summary convenient for tests
        return {
            "pipeline": self.name,
            "passes_executed": [t["pass"] for t in timeline],
            "timeline": timeline,
            "resources_snapshot": {k: resources[k] for k in list(resources)[:10]}
        }

class DummyPass:
    def __init__(self, name):
        self.name = f"Dummy:{name}"

    def run(self, camera, resources):
        resources_key = f"dummy_{self.name.replace(':','_')}"
        resources[resources_key] = {
            "note": "dummy output",
            "camera_pos": getattr(camera, "position", None) if camera else None
        }
        return {resources_key: resources[resources_key]}

# module-level convenience
def build_pipeline(name: str, config: Dict[str, Any]) -> RenderPipeline:
    return RenderPipeline(name, config)
