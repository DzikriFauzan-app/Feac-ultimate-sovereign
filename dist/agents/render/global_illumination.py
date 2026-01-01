import random

class SSGI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ssgi_shader = None
        self.noise_texture = None
        self.ssao_kernel = []

    def initialize(self, backend):
        self.create_ssgi_shader(backend)
        self.create_noise_texture(backend)
        self.create_ssao_kernel()
        self.set_ssao_uniforms(backend)

    def create_ssgi_shader(self, backend):
        vertex_shader_source = """
        #version 330 core
        layout (location = 0) in vec3 aPos;
        layout (location = 1) in vec2 aTexCoords;

        out vec2 TexCoords;

        void main()
        {
            TexCoords = aTexCoords;
            gl_Position = vec4(aPos, 1.0);
        }
        """

        fragment_shader_source = """
        #version 330 core
        in vec2 TexCoords;

        uniform sampler2D gPosition;
        uniform sampler2D gNormal;
        uniform sampler2D texNoise;

        uniform mat4 projection;
        uniform vec3 viewPos;

        out vec4 FragColor;

        const int kernelSize = 64;
        uniform vec3 ssaoKernel[kernelSize];

        float SSAO(vec3 fragPos, vec3 normal)
        {
            float radius = 0.5;
            float bias   = 0.025;
            vec3 randomVec = normalize(texture(texNoise, TexCoords).xyz);
            vec3 tangent   = normalize(cross(normal, randomVec));
            vec3 bitangent = cross(normal, tangent);
            mat3 TBN = mat3(tangent, bitangent, normal);

            float occlusion = 0.0;
            for(int i = 0; i < kernelSize; ++i)
            {
                vec3 samplePos = TBN * ssaoKernel[i];
                samplePos = fragPos + samplePos * radius;

                vec4 offset = projection * vec4(samplePos, 1.0);
                offset = offset / offset.w;
                offset = offset * 0.5 + 0.5;

                float sampleDepth = texture(gPosition, offset.xy).r;
                float rangeCheck = smoothstep(0.0, 1.0, radius / abs(fragPos.z - sampleDepth));
                occlusion += (sampleDepth >= offset.z + bias ? 1.0 : 0.0) * rangeCheck;
            }
            return 1.0 - (occlusion / kernelSize);
        }

        void main()
        {
            vec3 fragPos = texture(gPosition, TexCoords).xyz;
            vec3 normal = normalize(texture(gNormal, TexCoords).xyz);
            float ambientOcclusion = SSAO(fragPos, normal);

            FragColor = vec4(vec3(ambientOcclusion), 1.0);
        }
        """

        from NeoEngine.render.shader import Shader  # Import Shader class
        self.ssgi_shader = Shader(vertex_shader_source, fragment_shader_source)
        self.ssgi_shader.compile(backend)

    def create_noise_texture(self, backend):
        self.noise_texture = backend.create_texture(4, 4, format="RGBA", type="FLOAT")
        backend.set_texture_filter(self.noise_texture, min_filter="NEAREST", mag_filter="NEAREST")
        backend.set_texture_wrap(self.noise_texture, wrap_s="REPEAT", wrap_t="REPEAT")

        noise_data = []
        for _ in range(4 * 4):
            noise_data.extend([
                random.uniform(0.0, 1.0),
                random.uniform(0.0, 1.0),
                0.0,
                1.0
            ])
        backend.update_texture(self.noise_texture, noise_data)

    def create_ssao_kernel(self):
        for i in range(64):
            sample = [
                random.uniform(-1.0, 1.0),
                random.uniform(-1.0, 1.0),
                random.uniform(0.0, 1.0)
            ]
            sample = self.normalize(sample)
            scale = float(i) / 64.0
            scale = self.lerp(0.1, 1.0, scale * scale)
            sample = [s * scale for s in sample]
            self.ssao_kernel.append(sample)

    def set_ssao_uniforms(self, backend):
        self.ssgi_shader.bind(backend)
        backend.set_uniform(self.ssgi_shader.program, "ssaoKernel", self.ssao_kernel)

    def apply_ssgi(self, backend, gPosition, gNormal, projection, viewPos):
        self.ssgi_shader.bind(backend)

        backend.active_texture(0)
        backend.bind_texture(gPosition)
        backend.set_uniform(self.ssgi_shader.program, "gPosition", 0)

        backend.active_texture(1)
        backend.bind_texture(gNormal)
        backend.set_uniform(self.ssgi_shader.program, "gNormal", 1)

        backend.active_texture(2)
        backend.bind_texture(self.noise_texture)
        backend.set_uniform(self.ssgi_shader.program, "texNoise", 2)

        backend.set_uniform(self.ssgi_shader.program, "projection", projection)
        backend.set_uniform(self.ssgi_shader.program, "viewPos", viewPos)

        backend.draw_screen_quad()

    def lerp(self, a, b, f):
        return a + f * (b - a)

    def normalize(self, v):
        length = (v[0] * v[0] + v[1] * v[1] + v[2] * v[2]) ** 0.5
        return [v[0] / length, v[1] / length, v[2] / length]

# Contoh penggunaan di render pipeline
# from NeoEngine.render.global_illumination import SSGI
# ssgi = SSGI(width, height)
# ssgi.initialize(backend)

# Di dalam render loop:
# ssgi.apply_ssgi(backend, gPosition, gNormal, projection, viewPos)
