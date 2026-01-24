import requests
import json

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [{
        "agent": "AssetAgent",
        "action": "register_asset",
        "params": {"name": "Final_Scene", "local_path": "/sdcard/temp_render.mp4"}
    }]
}

try:
    r = requests.post(url, json=payload, timeout=5)
    print(f"📡 Status: {r.status_code}")
    print(f"✅ Response: {json.dumps(r.json(), indent=4)}")
except Exception as e:
    print(f"❌ Error: {e}")
