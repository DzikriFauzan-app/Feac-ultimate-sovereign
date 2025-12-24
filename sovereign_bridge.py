import os
import json

def prepare_self_build():
    print("🚀 Sovereign Bridge: Menyiapkan aset Aries untuk kompilasi FEAC...")
    # 1. Baca manifest dari Vault
    with open('data/vault/manifest.json', 'r') as f:
        manifest = json.load(f)
    
    # 2. Sinkronisasi dengan Frontend (Vite/React)
    # Di sini kita memicu build frontend agar siap dibungkus Capacitor
    os.system("cd frontend && npm run build")
    
    # 3. Trigger Capacitor untuk Android
    print("📦 Membungkus ke dalam Template Android...")
    os.system("npx cap sync android")

if __name__ == "__main__":
    prepare_self_build()
