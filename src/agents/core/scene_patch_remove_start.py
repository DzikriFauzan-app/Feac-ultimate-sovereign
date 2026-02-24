#!/usr/bin/env python3
# Patch final: hapus s.start() atau s.activate() dari build_test_scene()

import re

target = "/sdcard/Buku saya/Fauzan engine/NeoEngine/core/scene.py"

with open(target, "r") as f:
    txt = f.read()

# hapus s.start() atau s.activate()
patched = re.sub(r"\s*s\.(start|activate)\s*\(\s*\)\s*", "", txt)

with open(target, "w") as f:
    f.write(patched)

print("PATCH APPLIED: Removed s.start()/s.activate() from build_test_scene()")
