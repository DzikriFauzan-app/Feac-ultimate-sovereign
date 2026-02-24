#!/usr/bin/env python3
"""
render/gpu/gpu_abstraction.py

GPU Abstraction Layer for NeoEngine.

Public API:
- GPUDevice(backend="auto"|"mock"|"gl")
    - create_buffer(data=None, usage="static")
    - create_texture(width, height, data=None, fmt="rgba8")
    - create_shader_program(vertex_src, fragment_src)
    - create_framebuffer(width, height)
    - present()  # optional, no-op in mock

- Buffer: upload(data), bind()
- Texture: update(data), bind(unit)
- ShaderProgram: use(), set_uniform(name, value)
- Framebuffer: bind(), unbind(), read_pixels()

Design goals:
- Single, small, dependency-light module that supplies consistent API for the rest of engine.
- GLBackend uses PyOpenGL if present; otherwise falls back to MockBackend.
- MockBackend simulates behavior and stores resources in-memory for unit testing or headless runs.
"""

from __future__ import annotations
import sys
import time
import hashlib
import typing as T
from dataclasses import dataclass, field

# ---------------------------
# Low-level helpers
# ---------------------------
def _hash_bytes(b: bytes) -> str:
    return hashlib.sha1(b).hexdigest()

# ---------------------------
# Abstract interface classes
# ---------------------------
class GPUError(Exception):
    pass

class Buffer:
    def upload(self, data: bytes) -> None:
        raise NotImplementedError

    def bind(self) -> None:
        raise NotImplementedError

class Texture:
    def update(self, data: bytes) -> None:
        raise NotImplementedError

    def bind(self, unit: int = 0) -> None:
        raise NotImplementedError

class ShaderProgram:
    def use(self) -> None:
        raise NotImplementedError

    def set_uniform(self, name: str, value) -> None:
        raise NotImplementedError

class Framebuffer:
    def bind(self) -> None:
        raise NotImplementedError

    def unbind(self) -> None:
        raise NotImplementedError

    def read_pixels(self) -> bytes:
        raise NotImplementedError

# ---------------------------
# Mock Backend (pure python)
# ---------------------------
@dataclass
class _MockBuffer(Buffer):
    usage: str = "static"
    data: bytes | None = None
    created_at: float = field(default_factory=time.time)
    id: str = field(init=False)

    def __post_init__(self):
        self.id = f"mockbuf_{_hash_bytes(str(time.time()).encode())[:8]}"

    def upload(self, data: bytes) -> None:
        if not isinstance(data, (bytes, bytearray)):
            raise GPUError("MockBuffer.upload requires bytes")
        self.data = bytes(data)

    def bind(self) -> None:
        # no-op for mock, but keep interface
        print(f"[MockBuffer] bind {self.id} (size={len(self.data) if self.data else 0})")

@dataclass
class _MockTexture(Texture):
    width: int = 0
    height: int = 0
    fmt: str = "rgba8"
    data: bytes | None = None
    id: str = field(init=False)

    def __post_init__(self):
        self.id = f"mocktex_{_hash_bytes(str(time.time()).encode())[:8]}"

    def update(self, data: bytes) -> None:
        if not isinstance(data, (bytes, bytearray)):
            raise GPUError("MockTexture.update requires bytes")
        # minimal validation: expected size = width*height*4 for rgba8
        expected = self.width * self.height * (4 if self.fmt == "rgba8" else 3)
        if len(data) != expected:
            # allow variable sizes but warn
            print(f"[MockTexture] warning: data size {len(data)} != expected {expected}")
        self.data = bytes(data)

    def bind(self, unit: int = 0) -> None:
        print(f"[MockTexture] bind {self.id} to unit {unit}")

@dataclass
class _MockShaderProgram(ShaderProgram):
    vertex_src: str = ""
    fragment_src: str = ""
    compiled: bool = False
    id: str = field(init=False)
    uniforms: dict = field(default_factory=dict)

    def __post_init__(self):
        self.id = f"mockprog_{_hash_bytes((self.vertex_src + self.fragment_src).encode())[:8]}"

    def use(self) -> None:
        if not self.compiled:
            raise GPUError("MockShaderProgram: not compiled")
        print(f"[MockShaderProgram] use {self.id}")

    def set_uniform(self, name: str, value) -> None:
        self.uniforms[name] = value
        print(f"[MockShaderProgram] set_uniform {name} = {value}")

    def compile(self) -> dict:
        # very light validation: ensure keywords exist
        errs = []
        if "void main" not in self.vertex_src and "main(" not in self.vertex_src:
            errs.append("vertex shader missing 'main' function")
        if "void main" not in self.fragment_src and "main(" not in self.fragment_src:
            errs.append("fragment shader missing 'main' function")
        self.compiled = len(errs) == 0
        return {"ok": self.compiled, "errors": errs, "warnings": []}

@dataclass
class _MockFramebuffer(Framebuffer):
    width: int
    height: int
    color_tex: _MockTexture | None = None
    id: str = field(init=False)
    bound: bool = False

    def __post_init__(self):
        self.id = f"mockfb_{_hash_bytes(str(time.time()).encode())[:8]}"
        self.color_tex = _MockTexture(self.width, self.height, fmt="rgba8")

    def bind(self) -> None:
        self.bound = True
        print(f"[MockFramebuffer] bind {self.id}")

    def unbind(self) -> None:
        self.bound = False
        print(f"[MockFramebuffer] unbind {self.id}")

    def read_pixels(self) -> bytes:
        # return dummy bytes (RGBA black)
        return bytes([0] * (self.width * self.height * 4))

# ---------------------------
# GL Backend (best-effort)
# ---------------------------
class _GLBackendAvailable:
    """Helper to lazily detect OpenGL availability."""
    available = False
    reason = None

    @classmethod
    def probe(cls):
        if cls.available or cls.reason:
            return cls.available
        try:
            # try imports
            import OpenGL.GL as gl  # type: ignore
            import OpenGL.error as glerr  # type: ignore
            cls.available = True
            return True
        except Exception as e:
            cls.available = False
            cls.reason = str(e)
            return False

class _GLBuffer(Buffer):
    def __init__(self, usage="static"):
        from OpenGL import GL as gl  # type: ignore
        self.gl = gl
        # create buffer id
        self._id = gl.glGenBuffers(1)
        self.usage = usage

    def upload(self, data: bytes) -> None:
        gl = self.gl
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self._id)
        from ctypes import c_void_p, c_char
        import numpy as _np  # optional; we will accept bytes too
        # accept bytes -> create GL array
        gl.glBufferData(gl.GL_ARRAY_BUFFER, len(data), data, gl.GL_STATIC_DRAW)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def bind(self) -> None:
        self.gl.glBindBuffer(self.gl.GL_ARRAY_BUFFER, self._id)

class _GLTexture(Texture):
    def __init__(self, width: int, height: int, fmt: str = "rgba8"):
        from OpenGL import GL as gl  # type: ignore
        self.gl = gl
        self.width = width
        self.height = height
        self.fmt = fmt
        self._id = gl.glGenTextures(1)

    def update(self, data: bytes) -> None:
        gl = self.gl
        gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)
        # minimal format handling; expects RGBA8
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, self.width, self.height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, data)
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    def bind(self, unit: int = 0) -> None:
        gl = self.gl
        gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)

class _GLShaderProgram(ShaderProgram):
    def __init__(self, vertex_src: str, fragment_src: str):
        from OpenGL import GL as gl  # type: ignore
        self.gl = gl
        self.vertex_src = vertex_src
        self.fragment_src = fragment_src
        self._program = None

    def compile(self) -> dict:
        gl = self.gl
        def _compile(src, typ):
            shader = gl.glCreateShader(typ)
            gl.glShaderSource(shader, src)
            gl.glCompileShader(shader)
            ok = gl.glGetShaderiv(shader, gl.GL_COMPILE_STATUS)
            if not ok:
                log = gl.glGetShaderInfoLog(shader)
                raise GPUError(f"shader compile error: {log}")
            return shader

        try:
            vs = _compile(self.vertex_src, gl.GL_VERTEX_SHADER)
            fs = _compile(self.fragment_src, gl.GL_FRAGMENT_SHADER)
            prog = gl.glCreateProgram()
            gl.glAttachShader(prog, vs)
            gl.glAttachShader(prog, fs)
            gl.glLinkProgram(prog)
            ok = gl.glGetProgramiv(prog, gl.GL_LINK_STATUS)
            if not ok:
                log = gl.glGetProgramInfoLog(prog)
                raise GPUError(f"program link error: {log}")
            self._program = prog
            return {"ok": True, "errors": [], "warnings": []}
        except Exception as e:
            return {"ok": False, "errors": [str(e)], "warnings": []}

    def use(self) -> None:
        if not self._program:
            raise GPUError("GL program not compiled/linked")
        self.gl.glUseProgram(self._program)

    def set_uniform(self, name: str, value) -> None:
        # simplistic: only handle float and int; robust impl would query uniform location & type
        gl = self.gl
        loc = gl.glGetUniformLocation(self._program, name)
        if loc == -1:
            # silently ignore missing uniform in release
            print(f"[GLShaderProgram] uniform {name} not found")
            return
        if isinstance(value, float):
            gl.glUniform1f(loc, value)
        elif isinstance(value, int):
            gl.glUniform1i(loc, value)
        elif isinstance(value, (tuple, list)) and len(value) == 3:
            gl.glUniform3f(loc, *value)
        else:
            raise GPUError("unsupported uniform type")

class _GLFramebuffer(Framebuffer):
    def __init__(self, width: int, height: int):
        from OpenGL import GL as gl  # type: ignore
        self.gl = gl
        self.width = width
        self.height = height
        self._fbo = gl.glGenFramebuffers(1)
        self._tex = _GLTexture(width, height, fmt="rgba8")
        # bind & attach
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self._fbo)
        self._tex.bind(0)
        gl.glFramebufferTexture2D(gl.GL_FRAMEBUFFER, gl.GL_COLOR_ATTACHMENT0, gl.GL_TEXTURE_2D, self._tex._id, 0)
        status = gl.glCheckFramebufferStatus(gl.GL_FRAMEBUFFER)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)
        if status != gl.GL_FRAMEBUFFER_COMPLETE:
            raise GPUError("incomplete framebuffer")

    def bind(self) -> None:
        self.gl.glBindFramebuffer(self.gl.GL_FRAMEBUFFER, self._fbo)

    def unbind(self) -> None:
        self.gl.glBindFramebuffer(self.gl.GL_FRAMEBUFFER, 0)

    def read_pixels(self) -> bytes:
        gl = self.gl
        self.bind()
        size = self.width * self.height * 4
        data = gl.glReadPixels(0, 0, self.width, self.height, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE)
        self.unbind()
        return data

# ---------------------------
# GPUDevice wrapper / factory
# ---------------------------
class GPUDevice:
    """
    GPUDevice selects a backend and exposes simple creation APIs.
    backend: "auto" (try GL then mock), "gl" (force GL - raises if unavailable), "mock" (force mock)
    """
    def __init__(self, backend: str = "auto"):
        backend = backend.lower()
        self._backend_name = backend
        self._backend = None
        if backend == "auto":
            if _GLBackendAvailable.probe():
                try:
                    self._init_gl()
                    self._backend_name = "gl"
                except Exception:
                    self._init_mock()
                    self._backend_name = "mock"
            else:
                self._init_mock()
                self._backend_name = "mock"
        elif backend == "gl":
            if not _GLBackendAvailable.probe():
                raise GPUError(f"GL backend unavailable: {_GLBackendAvailable.reason}")
            self._init_gl()
            self._backend_name = "gl"
        elif backend == "mock":
            self._init_mock()
            self._backend_name = "mock"
        else:
            raise ValueError("unknown backend")

    def _init_mock(self):
        self._backend = "mock"
        print("[GPUDevice] using MockBackend")

    def _init_gl(self):
        if not _GLBackendAvailable.probe():
            raise GPUError("GL backend probe failed")
        # importing here to allow failure captured by probe earlier
        import OpenGL.GL as _gl  # type: ignore
        self._backend = "gl"
        print("[GPUDevice] using GLBackend")

    @property
    def backend(self) -> str:
        return self._backend

    # creation APIs
    def create_buffer(self, data: bytes | None = None, usage: str = "static") -> Buffer:
        if self._backend == "gl":
            return _GLBuffer(usage=usage)
        else:
            buf = _MockBuffer(usage=usage)
            if data is not None:
                buf.upload(data)
            return buf

    def create_texture(self, width: int, height: int, data: bytes | None = None, fmt: str = "rgba8") -> Texture:
        if self._backend == "gl":
            tex = _GLTexture(width, height, fmt=fmt)
            if data is not None:
                tex.update(data)
            return tex
        else:
            tex = _MockTexture(width=width, height=height, fmt=fmt)
            if data is not None:
                tex.update(data)
            return tex

    def create_shader_program(self, vertex_src: str, fragment_src: str) -> ShaderProgram:
        if self._backend == "gl":
            prog = _GLShaderProgram(vertex_src, fragment_src)
            res = prog.compile()
            if not res.get("ok"):
                raise GPUError("GL shader compile failed: " + ";".join(res.get("errors", [])))
            return prog
        else:
            prog = _MockShaderProgram(vertex_src=vertex_src, fragment_src=fragment_src)
            res = prog.compile()
            if not res.get("ok"):
                # still return it but compiled flag false to allow debug
                print("[GPUDevice] mock shader compile warnings/errors:", res)
            return prog

    def create_framebuffer(self, width: int, height: int) -> Framebuffer:
        if self._backend == "gl":
            return _GLFramebuffer(width, height)
        else:
            return _MockFramebuffer(width=width, height=height)

    # convenience
    def present(self) -> None:
        # present is a no-op for now; in GL it might swap buffers via host windowing system
        if self._backend == "gl":
            # Attempt to swap window buffers only if window context management is present externally
            print("[GPUDevice] present (GL) - swap buffer must be handled by host window/context manager")
        else:
            print("[GPUDevice] present (mock) - no-op")

# ---------------------------
# Module test / usage example
# ---------------------------
if __name__ == "__main__":
    # Basic smoke test for offline / Termux environment
    print("GPU Abstraction self-test")
    try:
        dev = GPUDevice(backend="auto")
        print("Selected backend:", dev.backend)

        # Buffer test
        b = dev.create_buffer(b"hello world", usage="static")
        b.bind()
        print("Buffer created:", getattr(b, "id", "<glbuf?>"))

        # Texture test
        tex = dev.create_texture(4, 4, data=bytes([255] * 4 * 4 * 4), fmt="rgba8")
        tex.bind(0)
        print("Texture created:", getattr(tex, "id", "<gltex?>"))

        # Shader test
        vs = "void main() { /* vertex */ }"
        fs = "void main() { /* fragment */ }"
        prog = dev.create_shader_program(vs, fs)
        # in mock prog, compile may be False; attempt use only if compiled
        if hasattr(prog, "compiled") and not getattr(prog, "compiled"):
            print("Mock shader not fully compiled (expected in minimal test).")
        else:
            prog.use()
            prog.set_uniform("u_time", 1.23)

        # FBO test
        fb = dev.create_framebuffer(8, 8)
        fb.bind()
        fb.unbind()
        px = fb.read_pixels()
        print("Read pixels len:", len(px))

        dev.present()
        print("GPU self-test finished OK")
    except Exception as e:
        print("GPU self-test error:", e)
        raise
