import requests

url = "http://127.0.0.1:8080/api/task"
# Payload dengan penambahan 'type' dan 'request_id'
payload = {
    "type": "command",
    "request_id": "SOVEREIGN-SIG-001",
    "task": {
        "id": "MLBB-BUILD-INIT",
        "action": "execute",
        "instruction": "create_mobile_legends_clone",
        "parameters": {
            "mode": "full_deployment",
            "agents_priority": "high_compute"
        }
    },
    "auth": {
        "user": "Fauzan",
        "role": "OWNER",
        "key": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"
    }
}

print("🚀 Menjalankan Protokol MLBB (Payload V3)...")
try:
    r = requests.post(url, json=payload, timeout=10)
    print(f"STATUS: {r.status_code}")
    print(f"RESPONSE: {r.text}")
except Exception as e:
    print(f"❌ Error: {e}")
