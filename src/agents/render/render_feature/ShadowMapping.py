from NeoEngine.core.message_bus import MessageBus
from NeoEngine.render.pbr_deferred import DeferredRendererAgent, Scene, Camera
import your_backend_module as backend  # Ganti dengan backend Anda

class ShadowMapping:
    def __init__(self, message_bus: MessageBus, width, height):
        self.message_bus = message_bus
        self.width = width
        self.height = height
        self.backend = backend.OpenGLBackend()  # Inisialisasi backend di sini
        self.renderer_agent = None
        self.shadow_map_fbo = None
        self.shadow_map_texture = None

    def initialize(self):
        # Inisialisasi DeferredRendererAgent
        self.renderer_agent = DeferredRendererAgent(self.message_bus, self.backend, self.width, self.height)
        self.renderer_agent.initialize()

        # Buat shadow map framebuffer dan texture
        self.shadow_map_fbo = self.backend.create_framebuffer()
        self.shadow_map_texture = self.backend.create_texture(self.width, self.height, format='DEPTH_COMPONENT24')
        self.backend.attach_texture(self.shadow_map_fbo, self.shadow_map_texture, attachment='DEPTH')
        self.backend.check_framebuffer_complete(self.shadow_map_fbo)

        # Subscribe ke pesan render
        self.message_bus.subscribe('render.shadow_mapping.render', self.handle_render)

    def handle_render(self, message):
        scene = message.get('scene')
        camera = message.get('camera')
        light_pos = message.get('light_pos')
        self.render(scene, camera, light_pos)

    def render(self, scene, camera, light_pos):
        # 1. Render shadow map
        self.backend.bind_framebuffer(self.shadow_map_fbo)
        self.backend.set_viewport(0, 0, self.width, self.height)
        self.backend.clear(color=(0.0, 0.0, 0.0, 1.0), depth=1.0)
        self.render_shadow_map(scene, light_pos)
        self.backend.bind_framebuffer(None)

        # 2. Render scene dengan bayangan
        # Kirim pesan render ke DeferredRendererAgent dengan shadow map
        self.message_bus.publish('render.render_scene', {
            'scene': scene,
            'camera': camera,
            'shadow_map': self.shadow_map_texture,
            'light_pos': light_pos
        })

    def render_shadow_map(self, scene, light_pos):
        # TODO: Implementasikan rendering shadow map di sini
        # Ini melibatkan pembuatan shader shadow map, mengatur uniform, dan menggambar scene dari sudut pandang cahaya
        pass

# Contoh Penggunaan (di luar folder render):
"""
from NeoEngine.core.message_bus import MessageBus
from NeoEngine.render.render_feature.ShadowMapping import ShadowMapping, Scene, Camera

# Inisialisasi message bus
message_bus = MessageBus()

# Inisialisasi ShadowMapping
shadow_mapping = ShadowMapping(message_bus, 800, 600)
shadow_mapping.initialize()

# Buat scene dan camera
scene = Scene()
camera = Camera()

# Tentukan posisi cahaya
light_pos = [5.0, 5.0, 5.0]

# Render frame dengan shadow mapping (kirim pesan ke ShadowMapping)
message_bus.publish('render.shadow_mapping.render', {
    'scene': scene,
    'camera': camera,
    'light_pos': light_pos
})
"""
