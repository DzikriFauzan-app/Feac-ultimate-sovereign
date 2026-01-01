class Light:
    def __init__(self, light_type, color, intensity):
        self.light_type = light_type
        self.color = color
        self.intensity = intensity

    def bind(self, backend, index):
        backend.set_light(index, self.light_type, self.color, self.intensity)
