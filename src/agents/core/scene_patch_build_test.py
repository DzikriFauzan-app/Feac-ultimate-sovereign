# PATCH: Rebuild build_test_scene() untuk NeoEngine

from core.scene import Scene, Node, Spatial, Camera, MeshInstance, Light

def build_test_scene():
    """
    Membangun scene sederhana yang valid untuk RenderAgent.
    Tanpa s.start() karena Scene tidak memiliki metode start().
    """
    s = Scene("test_scene")

    # CAMERA WAJIB → RenderAgent butuh minimal 1 kamera
    cam = Camera("main_camera")
    cam.transform.position = (0, 2, 6)
    cam.transform.rotation_euler = (0, 0, 0)
    s.root.add_child(cam)

    # OPTIONAL SAMPLE OBJECT — boleh kamu tambah/ubah nanti
    mesh = MeshInstance("box")
    mesh.mesh_id = "default_cube"
    mesh.material_id = "default_mat"
    mesh.transform.position = (0, 0, 0)
    s.root.add_child(mesh)

    # OPTIONAL LIGHT
    light = Light("main_light", light_type="directional")
    light.intensity = 1.0
    light.transform.rotation_euler = (-45, 45, 0)
    s.root.add_child(light)

    # Aktivasi scene (pengganti .start())
    s.activate()

    return s
