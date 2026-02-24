"""
OpenGLContext wrapper:
- tries to import PyOpenGL and create a headless EGL or GL context.
- provides:
    - available (bool)
    - compile_shader_source(source, stage) -> dict
    - render_pipeline_to_image(pipeline, camera, w, h) -> (image_path, meta)
If environment lacks proper libs, available=False and methods raise informative exceptions or return structured 'butuh riset lanjutan' info.
"""

import os, hashlib, time, tempfile, traceback
try:
    from OpenGL import GL
    # optional helper for EGL/OS-specific context creation. This environment-dependent.
    HAVE_GL = True
except Exception:
    HAVE_GL = False

class OpenGLContext:
    def __init__(self):
        self.available = False
        self.ctx_info = {}
        if HAVE_GL:
            try:
                # Try basic operations to check GL readiness.
                # Note: full EGL context creation is environment-specific (Termux/Android)
                # Here we perform a shallow check: presence of GL module.
                # Real headless EGL creation requires additional libraries.
                self.available = True
                self.ctx_info = {"backend": "PyOpenGL detected", "init_time": time.time()}
            except Exception as e:
                self.available = False
                self.ctx_info = {"error": str(e)}
        else:
            self.available = False
            self.ctx_info = {"reason": "PyOpenGL missing"}

    def compile_shader_source(self, source: str, stage: str):
        """
        Try to compile shader source using GL shader compile routines.
        If full GL context is not created, raise Exception or return structured result.
        """
        if not self.available:
            return {"ok": False, "reason": "GPU unavailable - butuh riset lanjutan"}

        # Minimal compile attempt (requires an active GL context). If not present, return details.
        try:
            # Here we attempt to create a shader object and compile.
            shader_type = GL.GL_FRAGMENT_SHADER if stage.startswith("frag") or stage == "fragment" else GL.GL_VERTEX_SHADER
            shader = GL.glCreateShader(shader_type)
            GL.glShaderSource(shader, source)
            GL.glCompileShader(shader)
            compiled = GL.glGetShaderiv(shader, GL.GL_COMPILE_STATUS)
            info_log = GL.glGetShaderInfoLog(shader).decode() if hasattr(GL.glGetShaderInfoLog(shader), 'decode') else str(GL.glGetShaderInfoLog(shader))
            ok = bool(compiled)
            return {"ok": ok, "info": info_log}
        except Exception as e:
            return {"ok": False, "error": f"compile exception: {e}", "trace": traceback.format_exc()}

    def render_pipeline_to_image(self, pipeline, camera, w, h):
        """
        High-level: render pipeline to an image file using GPU.
        Real implementation requires an active GL/EGL context and framebuffers.
        Here we attempt a conservative approach:
          - If environment supports GL but no context management, raise meaningful error.
          - Otherwise, return placeholder path or data.
        """
        if not self.available:
            raise RuntimeError("GPU unavailable - butuh riset lanjutan")

        # Attempt naive render - environment-specific. For now: produce a small PNG from CPU fallback if GL context not fully usable.
        try:
            # If GL context can be used to draw, user environment must provide it. We cannot create a cross-platform EGL here robustly.
            # So we raise until complete EGL support implementation is provided on-device.
            raise RuntimeError("Headless GPU render not implemented in this environment. Install EGL and ensure PyOpenGL has a valid context.")
        except Exception as e:
            raise

