import os
import shutil
import json

class ZeroPackager:
    def __init__(self):
        self.base_dir = os.getcwd()
        self.dist_dir = os.path.join(self.base_dir, "dist_sovereign")
        self.manifest_path = os.path.join(self.base_dir, "data/vault/manifest.json")

    def clean_dist(self):
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        os.makedirs(self.dist_dir)
        print("🧹 Dist folder dibersihkan.")

    def build_frontend(self):
        print("🎨 Mengompilasi Frontend FEAC (React)...")
        # Menjalankan build produksi agar node_modules tidak perlu ikut
        os.system("cd frontend && npm run build")
        
        # Copy hasil build (dist) ke folder distribusi utama
        src_frontend = os.path.join(self.base_dir, "frontend/dist")
        if os.path.exists(src_frontend):
            shutil.copytree(src_frontend, os.path.join(self.dist_dir, "www"))
            print("✅ Frontend terkompresi ke /www")

    def bundle_logic(self):
        print("🧠 Memaketkan Logika Aries & NeoEngine...")
        # Fokus pada file stress_task dan core engine saja
        logic_files = [f for f in os.listdir(self.base_dir) if f.startswith("stress_task") or f == "stress_neo.py"]
        
        os.makedirs(os.path.join(self.dist_dir, "logic"), exist_ok=True)
        for file in logic_files:
            shutil.copy(os.path.join(self.base_dir, file), os.path.join(self.dist_dir, "logic", file))
        
        # Copy Vault Data (Metadata)
        if os.path.exists("data/vault"):
            shutil.copytree("data/vault", os.path.join(self.dist_dir, "logic/vault"))
        print("✅ Logika Sovereign berhasil dipaketkan.")

    def create_installer_stub(self):
        # Membuat file pemicu build APK mandiri
        stub_content = """
import os
print('🚀 Sovereign Installer Aktif')
print('Membangun APK dari Template Lokal...')
os.system('npx cap sync android')
        """
        with open(os.path.join(self.dist_dir, "install_and_build.py"), "w") as f:
            f.write(stub_content)

    def run(self):
        print("🏗️ Memulai Proses Zero-Dependency Packaging...")
        self.clean_dist()
        self.build_frontend()
        self.bundle_logic()
        self.create_installer_stub()
        print(f"🎉 Selesai! Cek folder: {self.dist_dir}")

if __name__ == "__main__":
    packager = ZeroPackager()
    packager.run()
