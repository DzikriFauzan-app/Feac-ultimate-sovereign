import requests

URL = "http://10.4.35.107:8080/api/task"

def build_package():
    payload = {
        "agent": "PlayStoreAgent",
        "action": "prepare_production_build",
        "params": {
            "app_name": "Juragan Malam: Sovereign",
            "version": "1.0.0-PROD",
            "optimization": "Redmi_12_Extreme",
            "include_agents": 41,
            "security_level": "High_SHA256",
            "assets": "Neon_Jakarta_Night"
        }
    }
    res = requests.post(URL, json=payload)
    print(f"📦 BUILD PROCESS STARTED:")
    print(f"  - Status: {res.json().get('status')}")
    print(f"  - Message: Menyiapkan APK untuk pengujian internal Master.")

if __name__ == "__main__":
    build_package()
