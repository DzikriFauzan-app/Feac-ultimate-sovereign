import requests

url = "http://127.0.0.1:8080/api/task"
# Payload yang sudah disesuaikan dengan logika core/engine.py
payload = {
    "agent": "TaskAgent",  # Kunci vital yang sebelumnya hilang
    "instruction": "Build MLBB Clone Simulation",
    "command": "start_project",
    "auth": {
        "key": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"
    }
}

try:
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
