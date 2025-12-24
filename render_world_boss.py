import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "RenderAgent",
            "instruction": "Render 1000 Players & Giant Boss",
            "command": "process_task",
            "params": {
                "render_mode": "modern",
                "particle_physics": "enabled",
                "lod_bias": "aggressive"
            }
        }
    ]
}

print("🎨 Rendering 1000 Players & Effects (Ini akan berat)...")
start = time.time()
r = requests.post(url, json=payload, timeout=60)
print(f"✅ Render Arena Selesai: {time.time() - start:.2f} detik")
