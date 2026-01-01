class Mesh:
    def __init__(self, vertices, indices, normals=None, uvs=None):
        self.vertices = vertices
        self.indices = indices
        self.normals = normals
        self.uvs = uvs
        self.vertex_buffer = None
        self.index_buffer = None

    def load(self, backend):
        self.vertex_buffer = backend.create_vertex_buffer(self.vertices)
        self.index_buffer = backend.create_index_buffer(self.indices)
        if self.normals:
            self.normal_buffer = backend.create_vertex_buffer(self.normals)
        if self.uvs:
            self.uv_buffer = backend.create_vertex_buffer(self.uvs)

    def bind(self, backend):
        backend.bind_vertex_buffer(self.vertex_buffer)
        backend.bind_index_buffer(self.index_buffer)
        if self.normals:
            backend.bind_normal_buffer(self.normal_buffer)
        if self.uvs:
            backend.bind_uv_buffer(self.uv_buffer)

    def draw(self, backend):
        backend.draw_indexed(len(self.indices))
