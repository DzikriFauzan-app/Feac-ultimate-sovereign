import os

def apply_sovereign_patch():
    target = "src/components/Dashboard/SovereignDashboard.tsx"
    if not os.path.exists(target):
        print("❌ Target file not found!")
        return

    with open(target, 'r') as f:
        code = f.read()

    print("🛠️ Applying Modernization & Logic Patch...")
    
    # 1. Patch Status: UNAUTHORIZED -> Dynamic Authorization
    # Kita buat statusnya mengecek key dari environment
    code = code.replace(
        '<p className="text-red-500">UNAUTHORIZED</p>', 
        '{process.env.ARIES_API_KEY ? <p className="text-emerald-400 animate-pulse">AUTHORIZED</p> : <p className="text-red-500">UNAUTHORIZED</p>}'
    )

    # 2. Patch Visual: Menambahkan Glassmorphism ke container utama
    code = code.replace(
        'className="bg-slate-900"', 
        'className="bg-slate-900/80 backdrop-blur-xl border border-white/10 shadow-2xl"'
    )

    # 3. Patch Revenue: Membuat angka .2M bersinar (Glow effect)
    code = code.replace(
        'text-emerald-400', 
        'text-emerald-400 drop-shadow-[0_0_10px_rgba(52,211,153,0.5)]'
    )

    with open(target, 'w') as f:
        f.write(code)
    
    print("✅ Patch Applied: Logic is now Dynamic and UI is Modernized.")

if __name__ == "__main__":
    apply_sovereign_patch()
