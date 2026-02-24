class Texture:
    def __init__(self, image_path):
        self.image_path = image_path
        self.texture_id = None

    def load(self, backend):
        image = backend.load_image(self.image_path)
        self.texture_id = backend.create_texture(image)

    def bind(self, backend, slot=0):
        backend.bind_texture(self.texture_id, slot)
