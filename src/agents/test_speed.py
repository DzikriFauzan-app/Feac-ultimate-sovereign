import requests

url = "http://127.0.0.1:8080/api/task"
payload = {
    "instruction": "build_mlbb_clone",
    "command": "execute",
    "metadata": {
        "priority": "ULTIMATE",
        "sender": "ARIES_SOVEREIGN"
    },
    "auth_key": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1"
}

try:
    r = requests.post(url, json=payload, timeout=5)
    print(f"STATUS: {r.status_code} | DATA: {r.text}")
except Exception as e:
    print(f"❌ Gagal: {e}")
