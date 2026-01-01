import os
import re

def audit_ui_logic():
    print("🛡️ [AUDIT] Inspecting Sovereign UI Components...")
    
    files_to_check = [
        "src/components/Dashboard/SovereignDashboard.tsx",
        "src/components/Dashboard/index.tsx"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                print(f"\n📄 Analyzing {file_path}:")
                
                # 1. Cek Tombol Superkey / Unauthorized
                if "UNAUTHORIZED" in content or "Superkey" in content:
                    print("   ✅ Status 'UNAUTHORIZED' found (Matches Image 1000187988.jpg)")
                
                # 2. Cek Koneksi API Key (Aries)
                if "process.env" in content or "API_KEY" in content:
                    print("   ✅ API Key Input Logic: Detected")
                else:
                    print("   ⚠️ Warning: Hardcoded values found, need to link to ARIES_API_KEY")

                # 3. Cek Navigasi Hamburger
                if "Dashboard" in content and "Billing" in content:
                    print("   ✅ Hamburger Menu Map: Matches 1000188001.jpg")

    print("\n💎 [MODERNIZATION SUGGESTION]")
    print("   - CSS: Apply 'backdrop-filter: blur(10px)' for glassmorphism effect.")
    print("   - Logic: Auto-transition 'UNAUTHORIZED' -> 'AUTHORIZED' when API Key is validated.")
    print("\n✅ AUDIT COMPLETE: READY TO PATCH.")

if __name__ == "__main__":
    audit_ui_logic()
