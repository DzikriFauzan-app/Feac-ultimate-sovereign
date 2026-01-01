import requests

URL = "http://10.4.35.107:8080/api/task"

def create_splash():
    payload = {
        "agent": "MarketingAgent",
        "action": "design_splash",
        "params": {
            "title": "JURAGAN MALAM",
            "subtitle": "Powered by NeoEngine Sovereign",
            "theme": "Neon_Jakarta_Night"
        }
    }
    res = requests.post(URL, json=payload)
    print(f"🖼️  Splash Screen Concept: {res.json()}")

if __name__ == "__main__":
    create_splash()
