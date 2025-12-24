import requests

url = "http://127.0.0.1:8080/api/task"
# Kirim payload minimalis karena ensure_id akan menambah ID otomatis
payload = {
    "command": "build",
    "target": "mlbb_simulation",
    "auth_token": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"
}

try:
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
