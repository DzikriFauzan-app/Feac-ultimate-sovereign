import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "RenderAgent",
            "instruction": "Assemble 2000 Narrative Scenes to Video Timeline",
            "command": "process_task",
            "params": {"format": "4K", "fps": 60, "scenes": 2000}
        }
    ]
}

print("🎬 Menyusun 2.000 Scene ke dalam Timeline Video 4K...")
start = time.time()
r = requests.post(url, json=payload, timeout=300)
print(f"✅ Video Assembly Selesai: {time.time() - start:.2f} detik")
