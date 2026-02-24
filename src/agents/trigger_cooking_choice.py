import requests

URL = "http://10.4.35.107:8080/api/task"

def start_cooking(source_type):
    # source_type: 'fresh_meat' atau 'decaying_meat'
    payload = {
        "agent": "EconomyAgent",
        "action": "start_production",
        "params": {
            "source": source_type,
            "impact_rating": 1.0 if source_type == "fresh_meat" else 0.4,
            "poison_risk": 0.0 if source_type == "fresh_meat" else 0.6
        }
    }
    res = requests.post(URL, json=payload)
    print(f"🍳 Memasak menggunakan {source_type}: {res.json()}")

if __name__ == "__main__":
    # Contoh pemain nekat pakai daging layu karena sayang dibuang
    start_cooking("decaying_meat")
