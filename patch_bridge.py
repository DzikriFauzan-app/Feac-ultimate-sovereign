import os

bridge_path = "src/index.ts"
owner_key = "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"

if os.path.exists(bridge_path):
    with open(bridge_path, 'r') as f:
        content = f.read()

    # Logika Router untuk verifikasi Key Owner
    auth_logic = f"""
// --- ARIES AUTH SYSTEM ---
app.post('/auth/verify', (req, res) => {{
    const {{ key }} = req.body;
    if (key === '{owner_key}') {{
        console.log("🔓 Owner Access Granted");
        return res.json({{ status: 'authorized', role: 'OWNER', scope: '*' }});
    }}
    console.log("🔒 Unauthorized Access Attempt");
    return res.status(401).json({{ status: 'unauthorized' }});
}});
"""

    if '/auth/verify' not in content:
        # Masukkan sebelum app.listen atau di akhir file middleware
        if 'app.listen' in content:
            new_content = content.replace('app.listen', auth_logic + '\napp.listen')
            with open(bridge_path, 'w') as f:
                f.write(new_content)
            print("✅ Route /auth/verify berhasil di-patch ke src/index.ts")
        else:
            with open(bridge_path, 'a') as f:
                f.write(auth_logic)
            print("✅ Route ditambahkan di akhir file.")
    else:
        print("ℹ️ Route sudah ada.")
else:
    print("❌ src/index.ts tidak ditemukan!")
