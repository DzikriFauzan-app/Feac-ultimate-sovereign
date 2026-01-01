PATH = "/sdcard/Buku saya/Fauzan engine/NeoEngine/core/scene.py"

with open(PATH, "r") as f:
    lines = f.readlines()

output = []
inserted = False

for line in lines:
    output.append(line)

    # deteksi posisi setelah pembuatan sun light
    if "sun = Light" in line and not inserted:
        output.append(
            "    # Camera default untuk test render\n"
            "    cam = Camera(name=\"MainCamera\")\n"
            "    cam.transform.position = (0.0, 2.0, -5.0)\n"
            "    cam.transform.rotation = (0.0, 0.0, 0.0)\n"
            "    s.root.add_child(cam)\n"
        )
        inserted = True

with open(PATH, "w") as f:
    f.writelines(output)

print("PATCH APPLIED: default camera added to build_test_scene()")
