import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "PilotAgent",
            "instruction": "Simulate TD3 Wave 50 (High Load)",
            "command": "process_task",
            "params": {"duration": 60, "enemy_count": 500}
        }
    ]
}

print("🕹️ PilotAgent memasuki medan perang TD3...")
r = requests.post(url, json=payload, timeout=75)
res = r.json()['results'][0]

print("\n📊 HASIL PERFORMA TD3:")
print(f"🕹️ Avg FPS: {res['avg_fps']:.2f}")
print(f"🏆 Rank: {res['performance']}")
