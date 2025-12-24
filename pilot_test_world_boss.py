import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "PilotAgent",
            "instruction": "Simulate 1000 Player Raid",
            "command": "process_task",
            "params": {
                "duration": 60,
                "dps_per_player": 500,
                "visual_complexity": "extreme"
            }
        }
    ]
}

print("🕹️ PilotAgent memimpin 1000 Player menyerang Boss...")
r = requests.post(url, json=payload, timeout=75)
res = r.json()['results'][0]

print("\n📊 HASIL WORLD BOSS RAID:")
print(f"🕹️ Avg FPS: {res['avg_fps']:.2f}")
print(f"🩸 Boss HP Remaining: {max(0, 10000000 - (1000 * 500 * 60))} (Simulated)")
print(f"🏆 Status: {res['performance']}")
