class RenderBuffer:
    def __init__(self, width, height, format):
        self.width = width
        self.height = height
        self.format = format
        self.buffer_id = None
    def create(self, backend):
        self.buffer_id = backend.create_renderbuffer(self.width, self.height, self.format)
    def bind(self, backend):
        backend.bind_renderbuffer(self.buffer_id)
    def unbind(self, backend):
        backend.bind_renderbuffer(None)
