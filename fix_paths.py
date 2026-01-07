import os
import glob

# Daftar file yang dideteksi Blackbox mengandung hardcoded path
files_to_fix = glob.glob("./dist/agents/agents/*.py") + ["main.py"]

old_path = "/sdcard/Buku saya/Fauzan engine/NeoEngine"
# Gunakan path internal Android yang aman
new_path = "/data/data/org.feac.ultimate.feac_sovereign/files/NeoEngine"

for file_path in files_to_fix:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        if old_path in content:
            print(f"Fixing paths in: {file_path}")
            new_content = content.replace(old_path, new_path)
            with open(file_path, 'w') as f:
                f.write(new_content)

print("✅ Semua path telah dikonversi ke sistem dinamis.")
