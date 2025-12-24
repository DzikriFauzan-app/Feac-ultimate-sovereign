import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "PilotAgent",
            "instruction": "Stress Test Playback 2000 Narrative Scenes",
            "command": "process_task",
            "params": {"mode": "scan_all_scenes", "expected_count": 2000}
        }
    ]
}

print("🎞️ Memeriksa integritas 2.000 scene narasi...")
start = time.time()
r = requests.post(url, json=payload, timeout=90)
res = r.json()['results'][0]

print(f"\n📊 HASIL PEMERIKSAAN SCENE:")
print(f"✅ Scene Terverifikasi: {res.get('total_frames', 0)} / 2000")
print(f"⏱️ Waktu Verifikasi: {time.time() - start:.2f} detik")
print(f"🏆 Status: {res.get('performance')}")
