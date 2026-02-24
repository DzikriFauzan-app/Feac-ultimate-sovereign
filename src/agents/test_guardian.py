import requests

URL = "http://10.4.35.107:8080/api/task"

def test_guard():
    payload = {
        "agent": "SyntaxGuardianAgent",
        "action": "validate_and_backup",
        "file_path": "/sdcard/Buku saya/Fauzan engine/NeoEngine/engine_server.py"
    }
    res = requests.post(URL, json=payload)
    print(f"🛡️  Guardian Status: {res.json()}")

if __name__ == "__main__":
    test_guard()
