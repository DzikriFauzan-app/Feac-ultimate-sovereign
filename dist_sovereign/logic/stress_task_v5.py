import requests
import time

url = "http://127.0.0.1:8080/api/task"
headers = {
    "X-API-Key": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1",
    "Content-Type": "application/json"
}

payload = {
    "task_id": f"MLBB-{int(time.time())}",
    "type": "command",
    "metadata": {
        "owner": "Fauzan",
        "api_key": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"
    },
    "payload": {
        "action": "build",
        "target": "mobile_legends_clone",
        "params": {"priority": "max"}
    }
}

print("🚀 Menjalankan Protokol MLBB (Payload V5 - Deep Auth)...")
try:
    r = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"STATUS: {r.status_code}")
    print(f"RESPONSE: {r.text}")
except Exception as e:
    print(f"❌ Error: {e}")
