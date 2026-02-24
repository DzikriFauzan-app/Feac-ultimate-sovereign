import re

TARGET = "/sdcard/Buku saya/Fauzan engine/NeoEngine/core/scene.py"

with open(TARGET, "r") as f:
    data = f.readlines()

fixed = []
for i, line in enumerate(data, start=1):

    # Hapus s.start() dan s.activate() bersih tanpa merusak indent
    if "s.start()" in line or "s.activate()" in line:
        continue

    # Perbaikan khusus line 477: hapus karakter tidak valid
    if i == 477:
        # remove stray commas, invalid tokens, unmatched parentheses
        clean = re.sub(r"[,;]+$", "", line)          # buang koma atau titik koma di akhir
        clean = re.sub(r"[^\w\s\(\)\[\]\{\}\.\:\=]+", "", clean)  # buang karakter liar
        # Jika baris kosong jadikan comment agar tidak error
        if clean.strip() == "":
            clean = "    # patched empty line\n"
        fixed.append(clean)
        continue

    fixed.append(line)

with open(TARGET, "w") as f:
    f.writelines(fixed)

print("PATCH APPLIED: scene.py line 477 cleaned")
