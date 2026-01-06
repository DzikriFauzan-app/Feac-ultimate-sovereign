import os
import sys

def check_health():
    print("🛡️  FEAC SOVEREIGN HEALTH CHECK SYSTEM")
    print("-" * 40)
    
    # 1. Check Folder Engine di SDCard (Sesuai Laporan Genspark)
    engine_path = "/sdcard/Buku saya/Fauzan engine/NeoEngine/"
    print(f"[*] Checking NeoEngine path: {engine_path}")
    if os.path.exists(engine_path):
        print("    ✅ Folder Found!")
    else:
        print("    ❌ FOLDER MISSING! (Aplikasi akan Force Close)")
        print(f"    👉 Run: mkdir -p '{engine_path}'")

    # 2. Check Godot Binary (Sesuai Laporan Genspark)
    godot_path = "/data/data/com.termux/files/home/godot/Godot_v4.5.1-stable_linux_headless"
    print(f"[*] Checking Godot Headless: {godot_path}")
    if os.path.exists(godot_path):
        print("    ✅ Godot Binary Ready!")
    else:
        print("    ⚠️  GODOT MISSING! (Fitur Render tidak akan jalan)")

    # 3. Check .env (Sovereign Credentials)
    print("[*] Checking .env configuration...")
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            content = f.read()
            if "ARIES_OWNER_KEY" in content:
                print("    ✅ Sovereign Keys Detected (GOD_MODE Ready)")
            else:
                print("    ❌ Keys incomplete in .env")
    else:
        print("    ❌ .env FILE MISSING!")

    # 4. Check buildozer.spec Permissions
    print("[*] Checking Android Permissions in buildozer.spec...")
    if os.path.exists("buildozer.spec"):
        with open("buildozer.spec", "r") as f:
            spec = f.read()
            if "android.permissions = INTERNET" in spec:
                print("    ✅ Permissions Injected!")
            else:
                print("    ❌ PERMISSIONS MISSING! (Build ulang wajib dilakukan)")
    
    print("-" * 40)
    print("💡 Saran: Pastikan semua status '✅' sebelum menginstal APK baru.")

if __name__ == "__main__":
    check_health()
