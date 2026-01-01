import os

def force_patch():
    target = "src/components/Dashboard/SovereignDashboard.tsx"
    if not os.path.exists(target):
        print("❌ File Missing!")
        return

    with open(target, 'r') as f:
        content = f.read()

    # Paksa ganti status Unauthorized ke Dynamic Emerald (Hijau)
    # Mencari pola p tag yang mengandung UNAUTHORIZED
    import re
    new_content = re.sub(r'<p.*?>UNAUTHORIZED</p>', 
        '{process.env.ARIES_API_KEY ? <p className="text-emerald-400 animate-pulse font-black">AUTHORIZED</p> : <p className="text-red-500 font-black">UNAUTHORIZED</p>}', 
        content)
    
    # Tambahkan Glassmorphism & Glow .2M
    new_content = new_content.replace('.2M', '<span className="text-emerald-400 drop-shadow-[0_0_15px_rgba(52,211,153,0.6)]">.2M</span>')
    
    with open(target, 'w') as f:
        f.write(new_content)
    print("✅ Force Patch Applied: Dynamic Logic & Glow Effect Injected.")

if __name__ == "__main__":
    force_patch()
