"""
PostPass:
- tone mapping, simple exposure, and optional bloom metadata.
"""
import time

class PostPass:
    def __init__(self):
        self.name = "Post"

    def run(self, camera, resources):
        t = time.time()
        # produce metadata rather than actual image in headless mode
        final = {
            "exposure": 1.0,
            "tonemapped": True,
            "bloom_applied": False,
            "frame_id": f"frame-{int(t*1000)}",
            "produced_at": t
        }
        # if image framebuffer existed, would write file and return path
        return {"final_frame_meta": final}

