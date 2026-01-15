import requests

URL = "http://localhost:3001/api/v1/auth/verify"
PAYLOAD = {
    "apiKey": "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1",
    "action": "BRIDGE_CONNECT",
    "target_node": {
        "name": "NEO_ENGINE_SOVEREIGN",
        "url": "http://localhost:8080",
        "status": "ACTIVE_MANDATORY"
    }
}

try:
    response = requests.post(URL, json=PAYLOAD)
    print(f"📡 Aries Response: {response.json()}")
except Exception as e:
    print(f"❌ Bridge Failure: {e}")
