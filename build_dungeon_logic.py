import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "AISupervisor",
            "instruction": "Create Dungeon Entity Loop",
            "command": "process_task",
            "params": {
                "monster_count": 100,
                "boss_entities": 1,
                "respawn_time": 10,
                "loot_system": "enabled",
                "drop_rate": 0.5
            }
        },
        {
            "agent": "CodeAgent",
            "instruction": "Script Death & Loot Event",
            "command": "process_task"
        }
    ]
}

print("🏰 Membangun Ekosistem Dungeon (101 Entities)...")
start = time.time()
r = requests.post(url, json=payload, timeout=30)
print(f"✅ Logika Dungeon Selesai: {time.time() - start:.2f} detik")
