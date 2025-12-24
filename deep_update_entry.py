import os

def deep_scan_and_inject():
    target_component = "SovereignDashboard"
    import_path = "./components/Dashboard/SovereignDashboard"
    
    # Cari semua file .tsx atau .jsx di folder src
    found_files = []
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith((".tsx", ".jsx")) and file != "SovereignDashboard.tsx":
                found_files.append(os.path.join(root, file))

    if not found_files:
        print("❌ Tidak ada file React ditemukan di src/!")
        return

    # Cari file yang mengandung kata 'Routes', 'IonRouterOutlet', atau 'App'
    entry_file = None
    for file_path in found_files:
        with open(file_path, 'r') as f:
            content = f.read()
            if "IonRouterOutlet" in content or "Route" in content or "export default App" in content:
                entry_file = file_path
                break
    
    if not entry_file:
        entry_file = next((f for f in found_files if "App" in f), found_files[0])

    print(f"🎯 Entry Point Terdeteksi: {entry_file}")

    with open(entry_file, 'r') as f:
        content = f.read()

    # Injeksi Import di baris paling atas
    new_import = f"import {target_component} from '{import_path}';\n"
    if target_component not in content:
        content = new_import + content
        
        # Ganti komponen Dashboard lama dengan yang baru (Case Sensitive)
        if "Dashboard" in content:
            content = content.replace("Dashboard", target_component)
            print(f"✅ Dashboard lama telah di-overhaul menjadi {target_component}")
        else:
            print(f"⚠️ Komponen Dashboard tidak ditemukan. Menambahkan {target_component} sebagai fallback.")

    with open(entry_file, 'w') as f:
        f.write(content)
    
    print(f"🚀 SELESAI. Silakan jalankan 'ionic serve' atau 'npm run dev' untuk melihat tampilan mewahmu.")

if __name__ == "__main__":
    deep_scan_and_inject()
