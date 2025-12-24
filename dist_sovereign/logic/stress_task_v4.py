import requests
import time

url = "http://127.0.0.1:8080/api/task"
# Mencoba format flat yang sering digunakan oleh ShellAgent/TaskAgent
payload = {
    "id": f"MLBB-{int(time.time())}",
    "type": "command",
    "command": "build_project",
    "instruction": "create_mobile_legends_clone",
    "project_name": "Sovereign_MLBB",
    "priority": 10,
    "owner_key": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1",
    "data": "{}" # Kadang perlu string JSON kosong untuk menghindari 'None'
}

print("🚀 Menjalankan Protokol MLBB (Payload V4 - Flat)...")
try:
    r = requests.post(url, json=payload, timeout=10)
    print(f"STATUS: {r.status_code}")
    print(f"RESPONSE: {r.text}")
except Exception as e:
    print(f"❌ Error: {e}")
