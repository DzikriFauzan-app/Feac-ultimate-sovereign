"""
GBufferPass:
- For GPU mode: executes a fullscreen geometry pass (requires real GL & engine geometry).
- For non-GPU: produces structured buffers: normals, albedo, depth (as numpy-compatible summaries).
"""
import time
try:
    import numpy as _np
    HAVE_NUMPY = True
except Exception:
    HAVE_NUMPY = False

class GbufferPass:
    def __init__(self):
        self.name = "GBuffer"

    def run(self, camera, resources):
        # If we had mesh & lights, we'd output full textures.
        # For now, produce structured summaries.
        out = {}
        t = time.time()
        out["gbuffer_normals_summary"] = {"mean": None, "note": "no geometry in headless test"}
        out["gbuffer_albedo_summary"] = {"dominant_color": [0.5, 0.5, 0.5]}
        out["gbuffer_depth_summary"] = {"min": 0.0, "max": 1000.0}
        out["gbuffer_timestamp"] = t
        return out

