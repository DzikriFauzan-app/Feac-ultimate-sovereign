import os

# 1. Target file logic dashboard
dashboard_file = "src/components/Dashboard/SovereignDashboard.tsx"
owner_key = "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"

if os.path.exists(dashboard_file):
    with open(dashboard_file, 'r') as f:
        content = f.read()

    # Paksa state awal langsung berisi Owner Key
    if "useState('')" in content:
        content = content.replace("useState('')", f"useState('{owner_key}')")
    
    # Injeksi auto-login logic
    if "useEffect" in content:
        auto_auth = """
  React.useEffect(() => {
    // Auto-trigger verification if bridge is reachable
    const autoLogin = async () => {
      try {
        const res = await fetch('http://localhost:3001/auth/verify', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ key: '""" + owner_key + """' })
        });
        const data = await res.json();
        if (data.status === 'authorized') console.log("Sovereign Verified");
      } catch (e) { console.error("Bridge unreachable"); }
    };
    autoLogin();
  }, []);
"""
        content = content.replace("return (", auto_auth + "\n  return (")

    with open(dashboard_file, 'w') as f:
        f.write(content)
    print("✅ UI Dashboard berhasil di-inject dengan Owner Key.")
else:
    print("❌ File Dashboard tidak ditemukan!")
