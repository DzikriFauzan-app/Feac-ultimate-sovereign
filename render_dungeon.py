import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "RenderAgent",
            "instruction": "Render High-Poly Boss & 100 Monsters",
            "command": "process_task",
            "params": {"render_mode": "modern", "ambient_occlusion": "high"}
        }
    ]
}

print("🎨 Rendering Dungeon & Entities...")
start = time.time()
r = requests.post(url, json=payload, timeout=60)
print(f"✅ Render Dungeon Selesai: {time.time() - start:.2f} detik")
