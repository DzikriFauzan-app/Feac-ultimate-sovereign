class Reflection:
    def __init__(self, reflection_map_size):
        self.reflection_map_size = reflection_map_size
        self.reflection_map = None
        self.reflection_shader = None

    def initialize(self, backend):
        self.reflection_map = backend.create_texture(self.reflection_map_size, self.reflection_map_size, format="RGBA")
        backend.set_texture_filter(self.reflection_map, min_filter="LINEAR", mag_filter="LINEAR")
        backend.set_texture_wrap(self.reflection_map, wrap_s="CLAMP_TO_EDGE", wrap_t="CLAMP_TO_EDGE")
        vertex_shader_source = """
        #version 330 core
        layout (location = 0) in vec3 aPos;
        layout (location = 1) in vec3 aNormal;
        out vec3 Normal;
        out vec3 FragPos;
        out vec3 EyePos;
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;
        uniform vec3 eyePos;
        void main() {
            Normal = mat3(transpose(inverse(model))) * aNormal;
            FragPos = vec3(model * vec4(aPos, 1.0));
            EyePos = eyePos;
            gl_Position = projection * view * model * vec4(aPos, 1.0);
        }"""
        fragment_shader_source = """
        #version 330 core
        in vec3 Normal;
        in vec3 FragPos;
        in vec3 EyePos;
        uniform samplerCube environmentMap;
        uniform float roughness;
        out vec4 FragColor;
        void main() {
            vec3 normal = normalize(Normal);
            vec3 viewDir = normalize(EyePos - FragPos);
            vec3 reflectDir = reflect(-viewDir, normal);
            vec3 envColor = texture(environmentMap, reflectDir).rgb;
            FragColor = vec4(envColor, 1.0);
        }"""
        self.reflection_shader = Shader(vertex_shader_source, fragment_shader_source)
        self.reflection_shader.compile(backend)

    def render_reflection_map(self, scene, camera, backend):
        backend.set_render_target(self.reflection_map)
        backend.clear_render_target()
        view_matrix = camera.get_view_matrix()
        projection_matrix = camera.get_projection_matrix()
        backend.set_view_matrix(view_matrix)
        backend.set_projection_matrix(projection_matrix)
        for mesh in scene.meshes:
            self.reflection_shader.bind(backend)
            backend.set_uniform(self.reflection_shader.program, "model", mesh.model_matrix)
            backend.set_uniform(self.reflection_shader.program, "view", view_matrix)
            backend.set_uniform(self.reflection_shader.program, "projection", projection_matrix)
            mesh.bind(backend)
            mesh.draw(backend)

    def apply_reflection(self, backend, scene):
        backend.set_uniform(self.reflection_shader.program, "reflectionMap", self.reflection_map)
        backend.active_texture(1)
        backend.bind_texture(self.reflection_map)
