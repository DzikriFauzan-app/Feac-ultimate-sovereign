import requests

URL = "http://10.4.35.107:8080/api/task"

def discard_bad_meat():
    payload = {
        "agent": "InventoryAgent",
        "action": "discard_stock",
        "target": "decaying_meat",
        "qty": 5
    }
    res = requests.post(URL, json=payload)
    print(f"🗑️ Membersihkan Dapur: {res.json()}")

if __name__ == "__main__":
    discard_bad_meat()
