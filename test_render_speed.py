import requests
import time

url = "http://127.0.0.1:8080/api/task"

payload = {
    "tasks": [
        {
            "agent": "RenderAgent",
            "instruction": "Render 1.5M Terrain Nodes with PBR Shaders",
            "command": "process_task",
            "params": {
                "render_mode": "modern",
                "shader_complexity": "high",
                "nodes_count": 1500000
            }
        }
    ]
}

print("🎨 Memulai Simulasi Render Modern (1.5M Nodes)...")
print("⚠️ Ini akan memacu GPU/CPU HP Anda secara maksimal.")
start_time = time.time()

try:
    r = requests.post(url, json=payload, timeout=300)
    duration = time.time() - start_time
    print(f"\n✅ RENDER SIMULATION COMPLETE!")
    print(f"⏱️ Waktu Render: {duration:.2f} detik")
    print(f"📊 Status: {r.status_code}")
except Exception as e:
    print(f"❌ Render Overload: {e}")
