import re
import os

def audit_ui():
    UI_PATH = 'index.html'
    print("\n=== [FEAC DASHBOARD FRONTEND AUDIT] ===")
    
    if not os.path.exists(UI_PATH):
        print("❌ ERROR: index.html tidak ditemukan di folder ini!")
        return

    with open(UI_PATH, 'r') as f:
        content = f.read()

    # 1. Cek Endpoint Target
    endpoint = re.search(r"fetch\(['\"](.*?)['\"]", content)
    target = endpoint.group(1) if endpoint else "NOT FOUND"
    print(f"🔗 Target Endpoint: {target}")

    # 2. Cek Struktur Header Authorization
    auth_header = "Authorization" in content
    bearer_format = "Bearer" in content
    print(f"🛡️ Header Otoritas : {'TERPASANG' if auth_header else 'HILANG!'}")
    print(f"🔑 Format Bearer   : {'BENAR' if bearer_format else 'SALAH/TIDAK ADA'}")

    # 3. Cek Potensi Kerusakan String (Trim)
    has_trim = ".trim()" in content
    print(f"🧹 Input Sanitasi  : {'AKTIF (Aman)' if has_trim else 'NON-AKTIF (Rentan Spasi)'}")

    if target != "http://localhost:3333/":
        print("\n⚠️ PERINGATAN: Endpoint tidak mengarah ke Aries Bridge (Port 3333)!")
    
    if not auth_header or not bearer_format:
        print("\n❌ KESIMPULAN: Frontend gagal mengirimkan kredensial secara benar.")
    else:
        print("\n✅ KESIMPULAN: Struktur UI secara kode sudah benar.")

if __name__ == "__main__":
    audit_ui()
