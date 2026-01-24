import requests

url = "http://127.0.0.1:8080/api/task"
# Menggunakan 'action' (sesuai engine.py baris 41) bukan 'command'
payload = {
    "tasks": [
        {
            "agent": "AssetAgent", 
            "action": "process_task", # INI KUNCI PERBAIKANNYA
            "params": {"format": "4K", "fps": 60, "scenes": 2000}
        }
    ]
}

try:
    r = requests.post(url, json=payload, timeout=10)
    print(f"📡 [NEO_ENGINE_ACK]: {r.status_code}")
    print(f"✅ [RESPONSE]: {r.text}")
except Exception as e:
    print(f"❌ [CONNECTION_ERROR]: {e}")
