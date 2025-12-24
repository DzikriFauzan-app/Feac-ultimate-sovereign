import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {"agent": "CodeAgent", "instruction": "Create base MOBA controller", "command": "generate_code"},
        {"agent": "AssetAgent", "instruction": "Generate low-poly hero model", "command": "process_task"},
        {"agent": "NarrativeAgent", "instruction": "Draft lore", "command": "process_task"}
    ]
}

print("🔥 Memulai sinkronisasi dengan Neo Engine...")
for i in range(10):
    try:
        r = requests.post(url, json=payload, timeout=5)
        if r.status_code == 200:
            print(f"✅ KONEKSI BERHASIL PADA PERCOBAAN KE-{i+1}!")
            print(f"Council Response: {r.text}")
            break
    except Exception:
        print(f"⏳ Port 8080 belum siap (Percobaan {i+1}/10)...")
        time.sleep(3)
