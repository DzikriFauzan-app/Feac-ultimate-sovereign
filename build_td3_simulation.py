import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {"agent": "GenesisAgent", "instruction": "Init TD3 Project Structure", "command": "process_task"},
        {"agent": "CodeAgent", "instruction": "Generate Tower Targeting System", "command": "process_task"},
        {"agent": "MapGeneratorAgent", "instruction": "Bake S-Curve Pathing", "command": "process_task"},
        {"agent": "AISupervisor", "instruction": "Logic Creep Wave 1-100", "command": "process_task"}
    ]
}

print("🏗️ Membangun Infrastruktur Tower Defense 3...")
start = time.time()
r = requests.post(url, json=payload, timeout=30)
print(f"✅ Build Dasar Selesai: {time.time() - start:.2f} detik")
