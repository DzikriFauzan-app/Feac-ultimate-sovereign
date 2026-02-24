import requests

URL = "http://10.4.35.107:8080/api/task"

def set_f2p_limits():
    payload = {
        "agent": "EconomyAgent",
        "action": "set_player_stat",
        "level": "Kayu_1",
        "stats": {
            "capacity_seats": 4,
            "max_daily_income": 400000,
            "wood_price": 50000,
            "grind_difficulty": "HARD"
        }
    }
    res = requests.post(URL, json=payload)
    print(f"📊 F2P Stats Set: {res.json()}")

if __name__ == "__main__":
    set_f2p_limits()
