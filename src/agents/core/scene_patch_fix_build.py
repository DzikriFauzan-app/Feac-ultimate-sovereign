#!/usr/bin/env python3
# Patch untuk memperbaiki build_test_scene() di scene.py

import re
import sys

target = "/sdcard/Buku saya/Fauzan engine/NeoEngine/core/scene.py"

with open(target, "r") as f:
    txt = f.read()

# ganti s.start() menjadi s.activate()
patched = re.sub(r"s\.start\s*\(\s*\)", "s.activate()", txt)

with open(target, "w") as f:
    f.write(patched)

print("BUILD_TEST_SCENE PATCH APPLIED: start() -> activate()")
