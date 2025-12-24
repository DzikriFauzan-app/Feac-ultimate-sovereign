import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "AISupervisor",
            "instruction": "Init World Boss Logic",
            "command": "process_task",
            "params": {
                "boss_hp": 10000000,
                "player_entities": 1000,
                "sync_rate": "real-time",
                "damage_calculation": "distributed"
            }
        },
        {
            "agent": "CodeAgent",
            "instruction": "Create Multi-hit Optimization",
            "command": "process_task"
        }
    ]
}

print("🏗️ Membangun Arena World Boss (10M HP & 1000 Players)...")
start = time.time()
r = requests.post(url, json=payload, timeout=30)
print(f"✅ Infrastruktur Arena Selesai: {time.time() - start:.2f} detik")
