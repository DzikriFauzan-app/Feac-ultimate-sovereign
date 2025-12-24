import os
import re

manifest_path = "frontend/android/app/src/main/AndroidManifest.xml"

if os.path.exists(manifest_path):
    print(f"🔍 Memproses: {manifest_path}")
    
    with open(manifest_path, 'r') as f:
        content = f.read()

    # Regex untuk mencari dan menghapus attribute package="apapun"
    # Menangani variasi spasi agar rapi
    new_content = re.sub(r'\s*package="[^"]+"', '', content)

    # Cek apakah perubahan terjadi
    if len(new_content) != len(content):
        with open(manifest_path, 'w') as f:
            f.write(new_content)
        print("✅ SUKSES: Atribut 'package' dihapus sesuai standar Gradle 8.x.")
        print("   Namespace sekarang akan dikelola sepenuhnya oleh build.gradle.")
    else:
        print("⚠️ INFO: Tidak ditemukan atribut 'package'. File mungkin sudah bersih.")
else:
    print("❌ ERROR: File Manifest tidak ditemukan!")

