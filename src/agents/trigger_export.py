import os
import zipfile
import requests

URL = "http://10.4.35.107:8080/api/task"

def perform_export():
    project_dir = "/sdcard/Buku saya/Fauzan engine/NeoEngine"
    export_name = "/sdcard/Buku saya/Fauzan engine/NeoEngine_GOLD_MASTER_2025.zip"
    
    print(f"📦 MENGOMPRES SELURUH EKOSISTEM NEOENGINE...")
    
    with zipfile.ZipFile(export_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                # Jangan masukkan file log besar atau zip itu sendiri
                if not file.endswith(('.log', '.zip', '.pyc')):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, project_dir)
                    zip_ref.write(file_path, arcname)
    
    print(f"✅ EXPORT SELESAI!")
    print(f"📂 Lokasi File: {export_name}")
    print(f"⚖️ Status: GOLD MASTER READY FOR REDMI 12")

if __name__ == "__main__":
    perform_export()
