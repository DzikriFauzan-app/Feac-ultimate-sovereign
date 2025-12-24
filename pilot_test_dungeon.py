import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "PilotAgent",
            "instruction": "Kill All Monsters & Boss Simulation",
            "command": "process_task",
            "params": {
                "duration": 60, 
                "kill_rate_per_sec": 5,
                "track_respawn": True,
                "track_loot_drops": True
            }
        }
    ]
}

print("🕹️ PilotAgent memasuki Dungeon. Memulai pembantaian...")
r = requests.post(url, json=payload, timeout=75)
res = r.json()['results'][0]

print("\n📊 HASIL PERFORMA DUNGEON:")
print(f"🕹️ Avg FPS: {res['avg_fps']:.2f}")
print(f"📦 Total Items Dropped: {int(res['total_frames'] * 0.1)}")
print(f"🏆 Status: {res['performance']}")
