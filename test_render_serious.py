import requests
import time
import random

url = "http://127.0.0.1:8080/api/task"

# Menambahkan noise unik agar tidak bisa di-cache
print("🎨 Menyiapkan 1.5M Unique Shader Points...")
unique_nodes = [{"id": i, "roughness": random.random(), "metallic": random.random()} for i in range(1500000)]

payload = {
    "tasks": [
        {
            "agent": "RenderAgent",
            "instruction": "Force Re-render 1.5M PBR",
            "command": "process_task",
            "params": {
                "render_mode": "modern",
                "force_bypass_cache": True,
                "nodes": unique_nodes
            }
        }
    ]
}

print("🔥 Mengirim perintah Render Serius ke Neo Engine...")
start_time = time.time()

try:
    r = requests.post(url, json=payload, timeout=300)
    duration = time.time() - start_time
    print(f"\n✅ ACTUAL RENDER COMPLETED!")
    print(f"⏱️ Waktu Render Sebenarnya: {duration:.2f} detik")
    print(f"📊 Status: {r.status_code}")
except Exception as e:
    print(f"❌ Render Overload: {e}")
