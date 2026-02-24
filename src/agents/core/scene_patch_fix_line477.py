import re

PATH = "/sdcard/Buku saya/Fauzan engine/NeoEngine/core/scene.py"

with open(PATH, "r") as f:
    lines = f.readlines()

fixed = []

for i, line in enumerate(lines, start=1):

    if i == 477:
        # Replace broken line with correct two lines
        fixed.append("    s.root.add_child(sun)\n")
        fixed.append("    return s\n")
        continue

    fixed.append(line)

with open(PATH, "w") as f:
    f.writelines(fixed)

print("PATCH APPLIED: line 477 corrected (split into two valid statements)")
