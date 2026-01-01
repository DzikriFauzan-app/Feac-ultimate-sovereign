import os
import shutil
import zipfile
from datetime import datetime

class ExportAgent:
    def __init__(self, *args, **kwargs):
        self.base_dir = "/sdcard/Buku saya/Fauzan engine/NeoEngine/storage"
        self.export_dir = "/sdcard/Buku saya/Fauzan engine/NeoEngine/exports"
        os.makedirs(self.export_dir, exist_ok=True)

    def bundle_project(self, project_name):
        """Membungkus World, Assets, dan Code ke dalam satu ZIP"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        zip_filename = f"{project_name}_Export_{timestamp}.zip"
        zip_path = os.path.join(self.export_dir, zip_filename)
        
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # 1. Export World Data
                world_path = os.path.join(self.base_dir, "world_data")
                for root, dirs, files in os.walk(world_path):
                    for file in files:
                        if project_name in file:
                            zipf.write(os.path.join(root, file), os.path.join("World", file))
                
                # 2. Export Generated Code
                code_path = os.path.join(self.base_dir, "generated_code")
                for root, dirs, files in os.walk(code_path):
                    for file in files:
                        if project_name in file:
                            zipf.write(os.path.join(root, file), os.path.join("Scripts", file))

            return {"status": "success", "file": zip_filename, "path": zip_path}
        except Exception as e:
            return {"status": "error", "message": str(e)}

export_agent = ExportAgent()
