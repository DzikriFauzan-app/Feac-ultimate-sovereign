import requests

URL = "http://10.4.35.107:8080/api/task"

def generate_chatter():
    payload = {
        "agent": "NarrativeAgent",
        "action": "generate_dialogue",
        "context": {
            "location": "Gerobak Martabak",
            "characters": ["Pembeli_Lapar", "Penjual_Ramah"],
            "topic": "Martabak Telor vs Manis"
        }
    }
    res = requests.post(URL, json=payload)
    print(f"💬 Dialogue Generated: {res.json()}")

if __name__ == "__main__":
    generate_chatter()
