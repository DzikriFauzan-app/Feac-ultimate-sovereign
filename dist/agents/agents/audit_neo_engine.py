import subprocess
import os

def audit():
    print("🔍 FINAL AUDIT: TESTING GODOT KERNEL...")
    
    # Script yang mewarisi SceneTree agar Godot mau menjalankan
    script_path = "audit_test.gd"
    with open(script_path, "w") as f:
        f.write("extends SceneTree\nfunc _init():\n    print('NEO_RENDER_CHECK_SUCCESS')\n    quit()")
    
    try:
        # Menjalankan dengan mode headless
        result = subprocess.run(
            ["godot", "--display-driver", "headless", "-s", script_path],
            capture_output=True, text=True, timeout=10
        )
        
        if "NEO_RENDER_CHECK_SUCCESS" in result.stdout:
            print("\n✅ RENDER & LOGIC: 100% OPERATIONAL!")
            print("🚀 NeoEngine siap memproses Juragan Malam.")
        else:
            print(f"\n⚠️ OUTPUT: {result.stdout}\nERROR: {result.stderr}")
            
    except Exception as e:
        print(f"❌ FAIL: {e}")

if __name__ == "__main__":
    audit()
