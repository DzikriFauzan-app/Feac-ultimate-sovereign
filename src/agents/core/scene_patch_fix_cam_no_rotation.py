PATH = "/sdcard/Buku saya/Fauzan engine/NeoEngine/core/scene.py"

with open(PATH, "r") as f:
    lines = f.readlines()

output = []
inserted = False

for line in lines:
    output.append(line)

    # Tambah kamera setelah Sun
    if "sun = Light" in line and not inserted:
        output.append(
            "    # Camera default untuk test render\n"
            "    cam = Camera(name=\"MainCamera\")\n"
            "    cam.transform.position = (0.0, 2.0, -5.0)\n"
            "    # Transform tidak memiliki rotation, jadi tidak diset\n"
            "    s.root.add_child(cam)\n"
        )
        inserted = True

with open(PATH, "w") as f:
    f.writelines(output)

print("PATCH APPLIED: camera ditambahkan tanpa rotation")
