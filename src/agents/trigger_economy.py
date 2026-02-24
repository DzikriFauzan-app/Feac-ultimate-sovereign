import requests

URL = "http://10.4.35.107:8080/api/task"

def setup_economy():
    payload = {
        "agent": "EconomyAgent",
        "action": "init_market_rates",
        "currency": "IDR_Sovereign",
        "base_prices": {
            "Martabak_Manis": 25000,
            "Es_Teh_Manis": 5000,
            "Tiket_Bianglala": 15000
        },
        "inflation_rate": 0.02
    }
    res = requests.post(URL, json=payload)
    print(f"💰 Economic System: {res.json()}")

if __name__ == "__main__":
    setup_economy()
