import requests

URL = "http://10.4.35.107:8080/api/task"

def buy_assets():
    # Pemain memutuskan investasi kulkas agar daging tidak mubazir
    payload = {
        "agent": "InventoryAgent",
        "action": "buy_fridge",
        "cost": 2000000
    }
    res = requests.post(URL, json=payload)
    print(f"❄️ Asset Purchase: {res.json()}")

if __name__ == "__main__":
    buy_assets()
