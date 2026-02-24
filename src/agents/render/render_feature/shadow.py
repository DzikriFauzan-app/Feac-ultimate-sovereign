class ShadowMapping:
    def __init__(self, shadow_map_size):
        self.shadow_map_size = shadow_map_size
        self.shadow_map = None
        self.shadow_shader = None
        self.depth_shader = None

    def initialize(self, backend):
        # Buat shadow map
        self.shadow_map = backend.create_texture(self.shadow_map_size, self.shadow_map_size, format="DEPTH_COMPONENT", type="FLOAT")
        backend.set_texture_filter(self.shadow_map, min_filter="LINEAR", mag_filter="LINEAR")
        backend.set_texture_wrap(self.shadow_map, wrap_s="CLAMP_TO_EDGE", wrap_t="CLAMP_TO_EDGE")
        # Shader shader
        vertex_shader_source = """#version 330 core
layout (location = 0) in vec3 aPos;
uniform mat4 lightSpaceMatrix;
uniform mat4 model;
void main() {
    gl_Position = lightSpaceMatrix * model * vec4(aPos, 1.0);
}"""
        fragment_shader_source = """#version 330 core
void main() {
    // Nothing to do here, output depth
}"""
        self.depth_shader = Shader(vertex_shader_source, fragment_shader_source)
        self.depth_shader.compile(backend)

        # Shader untuk shadow map
        shadow_vertex_shader_source = """
        #version 330 core
        layout (location = 0) in vec3 aPos;
        layout (location = 1) in vec2 aTexCoords;
        layout (location = 2) in vec3 aNormal;
        out vec2 TexCoords;
        out vec3 Normal;
        out vec3 FragPos;
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;
        uniform mat4 lightSpaceMatrix;
        void main() {
            TexCoords = aTexCoords;
            Normal = mat3(transpose(inverse(model))) * aNormal;
            FragPos = vec3(model * vec4(aPos, 1.0));
            gl_Position = projection * view * model * vec4(aPos, 1.0);
        }"""
        shadow_fragment_shader_source = """
        #version 330 core
        in vec2 TexCoords;
        in vec3 Normal;
        in vec3 FragPos;
        uniform sampler2D shadowMap;
        uniform vec3 lightPos;
        uniform vec3 viewPos;
        float ShadowCalculation(vec3 fragPos, vec3 normal, vec3 lightPos, sampler2D shadowMap, vec3 viewPos) {
            vec3 fragToLight = normalize(lightPos - fragPos);
            float diff = max(dot(normal, fragToLight), 0.0);
            float ambientStrength = 0.3;
            float diffuseStrength = 0.7;
            float ambient = ambientStrength;
            float diffuse = diffuseStrength * diff;
            float shadow = 0.0;
            vec3 fragToView = normalize(viewPos - fragPos);
            vec3 reflectDir = reflect(-fragToLight, normal);
            float spec = pow(max(dot(fragToView, reflectDir), 0.0), 32);
            float specularStrength = 0.5;
            float lightDistance = length(lightPos - fragPos);
            vec3 fragPosToLight = fragPos - lightPos;
            float depth = fragPosToLight.z / lightDistance;
            if (depth < texture(shadowMap, fragPosToLight.xy).r) {
                shadow = 0.5;
            }
            return shadow;
        }
        out vec4 FragColor;
        void main() {
            vec3 normal = normalize(Normal);
            vec3 lightColor = vec3(1.0);
            vec3 ambient = 0.3 * lightColor;
            vec3 lightDir = normalize(lightPos - FragPos);
            float diff = max(dot(normal, lightDir), 0.0);
            vec3 diffuse = diff * lightColor;
            float spec = pow(max(dot(normalize(-lightDir), normalize(-FragPos)), 0.0), 32);
            vec3 specular = vec3(0.5) * spec * lightColor;
            float shadow = ShadowCalculation(FragPos, normal, lightPos, shadowMap, viewPos);
            vec3 color = ambient + (1.0 - shadow) * (diffuse + specular);
            FragColor = texture(texture_diffuse1, TexCoords) * vec4(color, 1.0);
        }"""
        self.shadow_shader = Shader(shadow_vertex_shader_source, shadow_fragment_shader_source)
        self.shadow_shader.compile(backend)

    def render_shadow_map(self, scene, light, backend):
        backend.set_render_target(self.shadow_map)
        backend.clear_render_target()
        backend.set_view_matrix(light.get_view_matrix())
        backend.set_projection_matrix(light.get_projection_matrix())
        for mesh in scene.meshes:
            self.depth_shader.bind(backend)
            backend.set_uniform(self.depth_shader.program, "lightSpaceMatrix", light.get_light_space_matrix())
            backend.set_uniform(self.depth_shader.program, "model", mesh.model_matrix)
            mesh.bind(backend)
            mesh.draw(backend)

    def apply_shadows(self, backend, scene, camera, light):
        backend.set_uniform(self.shadow_shader.program, "shadowMap", self.shadow_map)
        backend.set_uniform(self.shadow_shader.program, "lightSpaceMatrix", light.get_light_space_matrix())
        backend.active_texture(0)
        backend.bind_texture(self.shadow_map)
