from NeoEngine.core.message_bus import MessageBus
from NeoEngine.render.pbr_deferred import DeferredRendererAgent, Scene, Camera
import your_backend_module as backend  # Ganti dengan backend Anda

class DeferredPass:
    def __init__(self, message_bus: MessageBus, width, height):
        self.message_bus = message_bus
        self.width = width
        self.height = height
        self.backend = backend.OpenGLBackend()  # Inisialisasi backend di sini
        self.renderer_agent = None
        self.scene = None
        self.camera = None

    def initialize(self):
        # Inisialisasi DeferredRendererAgent
        self.renderer_agent = DeferredRendererAgent(self.message_bus, self.backend, self.width, self.height)
        self.renderer_agent.initialize()

        # Buat scene dan camera default
        self.scene = Scene()
        self.camera = Camera()

        # Subscribe ke pesan render
        self.message_bus.subscribe('render.deferred_pass.render', self.handle_render)

    def handle_render(self, message):
        scene = message.get('scene') or self.scene
        camera = message.get('camera') or self.camera
        self.render(scene, camera)

    def set_scene(self, scene):
        self.scene = scene

    def set_camera(self, camera):
        self.camera = camera

    def render(self, scene, camera):
        # Kirim pesan render ke DeferredRendererAgent
        self.message_bus.publish('render.render_scene', {
            'scene': scene,
            'camera': camera
        })

# Contoh Penggunaan (di luar folder render):
"""
from NeoEngine.core.message_bus import MessageBus
from NeoEngine.render.render_pass.DeferredPass import DeferredPass, Scene, Camera

# Inisialisasi message bus
message_bus = MessageBus()

# Inisialisasi DeferredPass
deferred_pass = DeferredPass(message_bus, 800, 600)
deferred_pass.initialize()

# Buat scene dan camera
scene = Scene()
camera = Camera()

# Set scene dan camera
# deferred_pass.set_scene(scene)
# deferred_pass.set_camera(camera)

# Render frame (kirim pesan ke DeferredPass)
message_bus.publish('render.deferred_pass.render', {
    'scene': scene,
    'camera': camera
})
"""
