from ai.aicore_client import AICoreClient

class AutoMaterialGenerator:
    def __init__(self, message_bus, backend):
        self.message_bus = message_bus
        self.backend = backend
        self.ai_client = AICoreClient()

    def generate_material(self, prompt: str):
        albedo_texture = self.generate_texture(prompt + " albedo")
        normal_texture = self.generate_texture(prompt + " normal map")
        roughness_texture = self.generate_texture(prompt + " roughness")
        metallic_texture = self.generate_texture(prompt + " metallic")
        ao_texture = self.generate_texture(prompt + " ambient occlusion")

        material = self.backend.create_material()
        if albedo_texture:
            self.backend.set_material_texture(material, "albedo", albedo_texture)
        if normal_texture:
            self.backend.set_material_texture(material, "normal", normal_texture)
        if roughness_texture:
            self.backend.set_material_texture(material, "roughness", roughness_texture)
        if metallic_texture:
            self.backend.set_material_texture(material, "metallic", metallic_texture)
        if ao_texture:
            self.backend.set_material_texture(material, "ao", ao_texture)

        return material

    def generate_texture(self, prompt: str):
        # Panggil API AI melalui client
        texture_url = self.ai_client.generate_texture(prompt)
        if texture_url:
            # Muat tekstur ke backend dan kembalikan resource
            texture_resource = self.backend.load_texture_from_url(texture_url)
            return texture_resource
        else:
            print("Failed to generate texture. Returning None.")
            return None
