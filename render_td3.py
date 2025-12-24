import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "RenderAgent",
            "instruction": "Render TD3 Map with Particle Effects",
            "command": "process_task",
            "params": {"render_mode": "modern", "vfx_intensity": "high"}
        }
    ]
}

print("🎨 Melakukan Rendering Map TD3 & Asset Visual...")
start = time.time()
r = requests.post(url, json=payload, timeout=60)
print(f"✅ Render Selesai dalam: {time.time() - start:.2f} detik")
