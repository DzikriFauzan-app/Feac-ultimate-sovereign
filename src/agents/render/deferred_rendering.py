import sys

class DeferredRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gbuffer = None
        self.gbuffer_shader = None
        self.lighting_shader = None
        self.quad_vao = None
        self.light_pos = [0.0, 5.0, 5.0]
        self.light_color = [1.0, 1.0, 1.0]

    def initialize(self, backend):
        # Inisialisasi G-Buffer
        self.gbuffer = GBuffer(self.width, self.height)
        self.gbuffer.init(backend)

        # Kompilasi shader G-Buffer
        self.gbuffer_shader = Shader(gbuffer_vertex_shader, gbuffer_fragment_shader)
        self.gbuffer_shader.compile(backend)

        # Kompilasi shader pencahayaan
        self.lighting_shader = Shader(lighting_vertex_shader, lighting_fragment_shader)
        self.lighting_shader.compile(backend)

        # Buat VAO untuk quad layar penuh
        self.quad_vao = backend.create_vao()
        vertices = [
            -1.0,  1.0,
            -1.0, -1.0,
             1.0,  1.0,
             1.0, -1.0
        ]
        backend.set_vao_buffer(self.quad_vao, 0, vertices, 2)

    def render(self, backend, scene, camera):
        # 1. Render ke G-Buffer
        self.gbuffer.bind(backend)
        backend.clear(color=(0.0, 0.0, 0.0, 1.0), depth=1.0)
        self.render_scene_to_gbuffer(backend, scene, camera)
        self.gbuffer.unbind(backend)

        # 2. Render pencahayaan
        backend.clear(color=(0.0, 0.0, 0.0, 1.0), depth=1.0)
        self.render_lighting(backend, camera)

    def render_scene_to_gbuffer(self, backend, scene, camera):
        self.gbuffer_shader.bind(backend)

        view_matrix = camera.get_view_matrix()
        projection_matrix = camera.get_projection_matrix()

        for mesh in scene.meshes:
            model_matrix = mesh.model_matrix
            backend.set_uniform(self.gbuffer_shader.program, "model", model_matrix)
            backend.set_uniform(self.gbuffer_shader.program, "view", view_matrix)
            backend.set_uniform(self.gbuffer_shader.program, "projection", projection_matrix)

            # Asumsi: setiap mesh punya tekstur albedo
            backend.active_texture(0)
            backend.bind_texture(mesh.material.albedo_texture)
            backend.set_uniform(self.gbuffer_shader.program, "texture_albedo", 0)

            mesh.draw(backend)

    def render_lighting(self, backend, camera):
        self.lighting_shader.bind(backend)

        # Set tekstur G-Buffer
        backend.active_texture(0)
        backend.bind_texture(self.gbuffer.position_tex)
        backend.set_uniform(self.lighting_shader.program, "gPosition", 0)

        backend.active_texture(1)
        backend.bind_texture(self.gbuffer.normal_tex)
        backend.set_uniform(self.lighting_shader.program, "gNormal", 1)

        backend.active_texture(2)
        backend.bind_texture(self.gbuffer.albedo_tex)
        backend.set_uniform(self.lighting_shader.program, "gAlbedo", 2)

        # Set uniform pencahayaan
        backend.set_uniform(self.lighting_shader.program, "lightPos", self.light_pos)
        backend.set_uniform(self.lighting_shader.program, "lightColor", self.light_color)
        backend.set_uniform(self.lighting_shader.program, "viewPos", camera.position)

        # Render quad layar penuh
        backend.bind_vao(self.quad_vao)
        backend.draw_arrays(0, 4)

# --- G-Buffer Framebuffer Setup ---
class GBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fbo = None
        self.position_tex = None
        self.normal_tex = None
        self.albedo_tex = None
        self.depth_tex = None

    def init(self, backend):
        self.fbo = backend.create_framebuffer()

        # Buat tekstur posisi
        self.position_tex = backend.create_texture(self.width, self.height, format='RGB16F')
        backend.attach_texture(self.fbo, self.position_tex, attachment='COLOR0')

        # Buat tekstur normal
        self.normal_tex = backend.create_texture(self.width, self.height, format='RGB16F')
        backend.attach_texture(self.fbo, self.normal_tex, attachment='COLOR1')

        # Buat tekstur albedo (warna dasar)
        self.albedo_tex = backend.create_texture(self.width, self.height, format='RGBA')
        backend.attach_texture(self.fbo, self.albedo_tex, attachment='COLOR2')

        # Buat depth buffer
        self.depth_tex = backend.create_texture(self.width, self.height, format='DEPTH_COMPONENT24')
        backend.attach_texture(self.fbo, self.depth_tex, attachment='DEPTH')

        # Periksa status framebuffer
        backend.check_framebuffer_complete(self.fbo)

    def bind(self, backend):
        backend.bind_framebuffer(self.fbo)
        backend.set_viewport(0, 0, self.width, self.height)

    def unbind(self, backend):
        backend.bind_framebuffer(None)

# --- Shader untuk Mengisi G-Buffer ---
# gbuffer.vert
gbuffer_vertex_shader = """
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec2 aTexCoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec3 FragPos;
out vec3 Normal;
out vec2 TexCoords;

void main()
{
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    TexCoords = aTexCoords;

    gl_Position = projection * view * model * vec4(aPos, 1.0);
}
"""

# gbuffer.frag
gbuffer_fragment_shader = """
#version 330 core
layout (location = 0) out vec3 gPosition;
layout (location = 1) out vec3 gNormal;
layout (location = 2) out vec4 gAlbedo;

in vec3 FragPos;
in vec3 Normal;
in vec2 TexCoords;

uniform sampler2D texture_albedo;

void main()
{
    gPosition = FragPos;
    gNormal = normalize(Normal);
    gAlbedo = texture(texture_albedo, TexCoords);
}
"""

# --- Shader untuk Pencahayaan dari G-Buffer ---
# lighting.vert
lighting_vertex_shader = """
#version 330 core
layout (location = 0) in vec2 aPos;
out vec2 TexCoords;

void main()
{
    TexCoords = aPos * 0.5 + 0.5;
    gl_Position = vec4(aPos, 0.0, 1.0);
}
"""

# lighting.frag
lighting_fragment_shader = """
#version 330 core
out vec4 FragColor;

in vec2 TexCoords;

uniform sampler2D gPosition;
uniform sampler2D gNormal;
uniform sampler2D gAlbedo;

uniform vec3 lightPos;
uniform vec3 lightColor;
uniform vec3 viewPos;

void main()
{
    vec3 FragPos = texture(gPosition, TexCoords).rgb;
    vec3 Normal = normalize(texture(gNormal, TexCoords).rgb);
    vec3 Albedo = texture(gAlbedo, TexCoords).rgb;

    // Ambient
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;

    // Diffuse
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(Normal, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // Specular
    float specularStrength = 0.5;
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;

    vec3 color = (ambient + diffuse + specular) * Albedo;
    FragColor = vec4(color, 1.0);
}
"""

# Minimal shader class, replace with your engine's shader class
class Shader:
    def __init__(self, vertex_source, fragment_source):
        self.vertex_source = vertex_source
        self.fragment_source = fragment_source
        self.program = None

    def compile(self, backend):
        self.program = backend.create_shader_program(self.vertex_source, self.fragment_source)

    def bind(self, backend):
        backend.bind_shader(self.program)

# Minimal scene and camera classes, replace with your engine's equivalents
class Scene:
    def __init__(self):
        self.meshes = []

class Camera:
    def __init__(self, position, target, fov, aspect, near, far):
        self.position = position
        self.target = target
        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

    def get_view_matrix(self):
        # Replace with your engine's view matrix calculation
        return look_at(self.position, self.target, [0.0, 1.0, 0.0])

    def get_projection_matrix(self):
        # Replace with your engine's projection matrix calculation
        return perspective(self.fov, self.aspect, self.near, self.far)

# Dummy look_at and perspective functions, replace with your engine's math library
def look_at(eye, target, up):
    # Replace with your engine's look_at implementation
    return [[1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]]

def perspective(fov, aspect, near, far):
    # Replace with your engine's perspective implementation
    return [[1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]]
