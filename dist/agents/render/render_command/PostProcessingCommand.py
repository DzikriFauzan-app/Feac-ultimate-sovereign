# main.py
from NeoEngine.core.message_bus import MessageBus
from NeoEngine.render.render_command.PostProcessingCommand import PostProcessingCommand, Scene, Camera

# Inisialisasi message bus
message_bus = MessageBus()

# Buat shader post-processing (contoh)
post_processing_shader = None  # Gantilah dengan shader yang sesuai

# Inisialisasi PostProcessingCommand
post_processing_command = PostProcessingCommand(message_bus, 800, 600, post_processing_shader)
post_processing_command.initialize()

# Buat scene dan camera
scene = Scene()
camera = Camera()

# Eksekusi render command
post_processing_command.execute(scene, camera)
