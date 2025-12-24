import os
import subprocess
import shutil

def get_termux_aapt2():
    res = subprocess.run(["find", os.environ.get("ANDROID_HOME", ""), "-name", "aapt2"], capture_output=True, text=True)
    paths = [p for p in res.stdout.strip().split('\n') if p]
    return paths[0] if paths else None

def poison_cache(termux_aapt2):
    print("🧪 Memulai Total Cache Poisoning...")
    # Target folder spesifik yang terus menerus error
    target_dir = "/data/data/com.termux/files/home/.gradle/caches/8.14.3/transforms/514c296624e193fba87763b67440dda2/transformed/aapt2-8.13.0-13719691-linux"
    target_bin = os.path.join(target_dir, "aapt2")

    if os.path.exists(target_dir):
        # Berikan izin tulis jika sebelumnya terkunci
        os.system(f"chmod -R 777 {target_dir}")
        # Hapus binari lama
        if os.path.exists(target_bin):
            os.remove(target_bin)
        
        # Copy binari termux ke lokasi tersebut
        shutil.copy(termux_aapt2, target_bin)
        os.chmod(target_bin, 0o755)
        
        # KUNCI FOLDER (Immutable) - Agar Gradle tidak bisa menghapus/menimpa
        # Di Android/Termux kita gunakan chmod agar tidak bisa diwrite
        os.system(f"chmod 555 {target_bin}")
        os.system(f"chmod 555 {target_dir}")
        print(f"🔒 Folder dipatch dan dikunci: {target_dir}")
    else:
        print("⚠️ Folder target tidak ditemukan, menjalankan build normal untuk memancing...")

def run_sovereign_build():
    termux_aapt2 = get_termux_aapt2()
    if not termux_aapt2:
        print("❌ Error: AAPT2 Termux tidak ditemukan.")
        return

    poison_cache(termux_aapt2)
    
    print("🏗️ Memulai Build Terakhir (Poisoned Cache Mode)...")
    # Gunakan --offline agar Gradle tidak mencoba memvalidasi ulang ke server Maven
    gradle_args = ["./gradlew", "assembleDebug", "--offline", "--no-daemon"]
    
    try:
        process = subprocess.Popen(gradle_args)
        process.wait()
        
        if process.returncode == 0:
            print("\n🎉 AKHIRNYA! BUILD SUCCESSFUL.")
        else:
            print("\n❌ Masih gagal. Sepertinya kita harus bypass AAPT2 di tingkat Gradle Script.")
    except Exception as e:
        print(f"🔥 Error: {e}")

if __name__ == "__main__":
    run_sovereign_build()
