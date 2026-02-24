class PostProcessing:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = None
        self.color_texture = None
        self.depth_texture = None
        self.post_processing_shader = None

    def initialize(self, backend):
        self.framebuffer = backend.create_framebuffer()
        self.color_texture = backend.create_texture(self.width, self.height, format="RGBA")
        backend.attach_texture_to_framebuffer(self.framebuffer, self.color_texture, color_attachment=0)
        self.depth_texture = backend.create_texture(self.width, self.height, format="DEPTH_COMPONENT")
        backend.attach_texture_to_framebuffer(self.framebuffer, self.depth_texture, depth_attachment=True)
        vertex_shader_source = """
        #version 330 core
        layout (location = 0) in vec3 aPos;
        layout (location = 1) in vec2 aTexCoords;
        out vec2 TexCoords;
        void main() {
            TexCoords = aTexCoords;
            gl_Position = vec4(aPos, 1.0);
        }"""
        fragment_shader_source = """
        #version 330 core
        in vec2 TexCoords;
        uniform sampler2D screenTexture;
        out vec4 FragColor;
        void main() {
            vec4 color = texture(screenTexture, TexCoords);
            // Contoh: Invert warna
            FragColor = vec4(1.0 - color.r, 1.0 - color.g, 1.0 - color.b, 1.0);
        }"""
        self.post_processing_shader = Shader(vertex_shader_source, fragment_shader_source)
        self.post_processing_shader.compile(backend)

    def apply_post_processing(self, backend, scene, camera):
        backend.bind_framebuffer(self.framebuffer)
        backend.clear_render_target()
        view_matrix = camera.get_view_matrix()
        projection_matrix = camera.get_projection_matrix()
        backend.set_view_matrix(view_matrix)
        backend.set_projection_matrix(projection_matrix)
        for mesh in scene.meshes:
            self.post_processing_shader.bind(backend)
            backend.set_uniform(self.post_processing_shader.program, "model", mesh.model_matrix)
            backend.set_uniform(self.post_processing_shader.program, "view", view_matrix)
            backend.set_uniform(self.post_processing_shader.program, "projection", projection_matrix)
            mesh.bind(backend)
            mesh.draw(backend)
        backend.bind_framebuffer(None)
        backend.draw_texture(self.color_texture)
