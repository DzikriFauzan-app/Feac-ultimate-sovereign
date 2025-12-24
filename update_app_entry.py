import os

def find_and_update_entry():
    # Daftar kemungkinan file entry utama
    possible_entries = ["src/App.tsx", "src/App.jsx", "src/main.tsx", "src/index.tsx"]
    entry_path = None

    for path in possible_entries:
        if os.path.exists(path):
            entry_path = path
            break
    
    if not entry_path:
        print("❌ File entry utama tidak ditemukan! Silakan jalankan 'ls src' untuk cek nama filenya.")
        return

    print(f"🎯 Entry ditemukan: {entry_path}")

    with open(entry_path, 'r') as f:
        content = f.read()

    # Injeksi Import
    import_line = "import SovereignDashboard from './components/Dashboard/SovereignDashboard';"
    if "SovereignDashboard" not in content:
        # Masukkan import di baris paling atas
        content = import_line + "\n" + content
        
        # Logika penggantian: Mencoba mengganti komponen Dashboard lama 
        # atau menjadikannya komponen default di Route
        if "Dashboard" in content:
            content = content.replace("Dashboard", "SovereignDashboard")
            print(f"✅ Berhasil mengganti 'Dashboard' dengan 'SovereignDashboard' di {entry_path}")
        else:
            print(f"⚠️ 'Dashboard' tidak ditemukan di {entry_path}. Kamu mungkin perlu memanggil <SovereignDashboard /> secara manual.")

    with open(entry_path, 'w') as f:
        f.write(content)
    print(f"🚀 Proses selesai. {entry_path} telah terhubung ke desain baru.")

if __name__ == "__main__":
    find_and_update_entry()
