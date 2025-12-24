import requests

url = "http://127.0.0.1:8080/api/task"
# Payload lengkap untuk memicu Council of Agents
payload = {
    "id": "TASK-MLBB-001",
    "action": "execute",
    "command": "build_project",
    "params": {
        "project_name": "MLBB_Clone_Sovereign",
        "complexity": "MAX",
        "agents": "all"
    },
    "owner": "ARIES_SOVEREIGN",
    "apiKey": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"
}

print("🚀 Memicu Proyek MLBB melalui Neo Task Endpoint...")
try:
    r = requests.post(url, json=payload, timeout=10)
    print(f"STATUS: {r.status_code}")
    print(f"RESPONSE: {r.text}")
except Exception as e:
    print(f"❌ Error: {e}")
