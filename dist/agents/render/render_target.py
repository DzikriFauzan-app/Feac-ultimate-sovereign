class RenderTarget:
    def __init__(self, width, height, color_format, depth_format):
        self.width = width
        self.height = height
        self.color_format = color_format
        self.depth_format = depth_format
        self.framebuffer_id = None
        self.color_texture = None
        self.depth_texture = None

    def create(self, backend):
        self.framebuffer_id = backend.create_framebuffer()
        self.color_texture = backend.create_texture(self.width, self.height, self.color_format)
        self.depth_texture = backend.create_texture(self.width, self.height, self.depth_format)
        backend.attach_texture_to_framebuffer(self.framebuffer_id, self.color_texture, color_attachment=0)
        backend.attach_texture_to_framebuffer(self.framebuffer_id, self.depth_texture, depth_attachment=True)

    def bind(self, backend):
        backend.bind_framebuffer(self.framebuffer_id)

    def unbind(self, backend):
        backend.bind_framebuffer(None)
