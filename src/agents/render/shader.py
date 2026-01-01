import hashlib

class Shader:
    """
    Representasi shader tunggal.
    """

    def __init__(self, name: str, stage: str, source: str):
        self.name = name
        self.stage = stage
        self.source = source
        self.compiled = False
        self.compile_log = ""

    def compile(self):
        """
        Simulator kompilasi shader.
        Versi asli nanti memakai PyOpenGL atau backend NeoEngine.
        """
        if not self.source or len(self.source) < 5:
            self.compile_log = "Source terlalu pendek"
            self.compiled = False
            return False

        # Simulasi compile: hash sebagai ID
        self.shader_id = hashlib.sha1(self.source.encode()).hexdigest()
        self.compiled = True
        self.compile_log = f"Compiled OK: {self.shader_id}"
        return True


class ShaderManager:
    """
    Manajemen shader global engine.
    """

    def __init__(self):
        self.shaders = {}

    def create_shader(self, name: str, stage: str, source: str):
        shader = Shader(name, stage, source)
        shader.compile()
        self.shaders[name] = shader
        return shader

    def get(self, name: str):
        return self.shaders.get(name)

