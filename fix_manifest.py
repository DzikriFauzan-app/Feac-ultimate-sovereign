import os

manifest_path = "frontend/android/app/src/main/AndroidManifest.xml"

if os.path.exists(manifest_path):
    with open(manifest_path, 'r') as f:
        lines = f.readlines()

    # Membersihkan karakter aneh atau spasi berlebih yang sering merusak parsing
    cleaned_lines = [line.rstrip() + '\n' for line in lines if line.strip()]
    
    # Pastikan file dimulai dengan deklarasi XML yang benar
    if not cleaned_lines[0].startswith("<?xml"):
        cleaned_lines.insert(0, '<?xml version="1.0" encoding="utf-8"?>\n')

    with open(manifest_path, 'w') as f:
        f.writelines(cleaned_lines)
    
    print(f"✅ {manifest_path} has been sanitized and fixed.")
else:
    print(f"❌ Manifest tidak ditemukan di {manifest_path}. Cek struktur folder frontend kamu.")

