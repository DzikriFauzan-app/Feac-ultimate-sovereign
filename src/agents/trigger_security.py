import requests

URL = "http://10.4.35.107:8080/api/task"

def secure_player_balance():
    # Mengamankan Saldo 20 Juta
    payload = {
        "agent": "SecurityAgent",
        "action": "encrypt_stat",
        "value": 20000000
    }
    res = requests.post(URL, json=payload)
    print(f"🔒 Security Lock Applied: {res.json()}")

if __name__ == "__main__":
    secure_player_balance()
