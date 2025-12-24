import requests
import time

url = "http://127.0.0.1:8080/api/task"

payload = {
    "tasks": [
        {
            "agent": "PilotAgent",
            "instruction": "Simulate 1 minute gameplay in 1.5M node map",
            "command": "process_task",
            "params": {"duration": 60, "complexity": "high"}
        }
    ]
}

print("🎮 MEMULAI SIMULASI PLAYABLE (60 DETIK)...")
print("🚀 Pilot sedang menavigasi World Map Anda...")

try:
    # Timeout 70 detik untuk memberi ruang proses 60 detik
    r = requests.post(url, json=payload, timeout=70)
    res = r.json()
    
    print("\n📊 HASIL SIMULASI 1 MENIT:")
    print(f"🕹️ Average FPS: {res['results'][0]['avg_fps']:.2f}")
    print(f"🎞️ Total Frames Processed: {res['results'][0]['total_frames']}")
    print(f"🏆 Quality Rank: {res['results'][0]['performance']}")
    
    if res['results'][0]['avg_fps'] < 30:
        print("⚠️ Warning: Hasil render terlalu berat untuk dimainkan (Laggy).")
    else:
        print("✅ Status: REAL WORLD CLASS. Engine stabil dan lancar.")

except Exception as e:
    print(f"❌ Gameplay Crash: {e}")
