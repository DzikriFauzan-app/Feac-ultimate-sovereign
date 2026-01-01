class Material:
    """
    Material Node NeoEngine.
    Mengikat shader + uniform dictionary.
    """

    def __init__(self, name: str):
        self.name = name
        self.shader = None
        self.uniforms = {}

    def set_shader(self, shader):
        self.shader = shader

    def set_uniform(self, key, value):
        self.uniforms[key] = value


class MaterialManager:
    """
    Manajemen material global engine.
    """

    def __init__(self):
        self.materials = {}

    def create_material(self, name: str):
        mat = Material(name)
        self.materials[name] = mat
        return mat

    def get(self, name: str):
        return self.materials.get(name)

