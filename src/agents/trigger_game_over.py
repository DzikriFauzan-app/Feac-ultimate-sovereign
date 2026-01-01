import requests

URL = "http://10.4.35.107:8080/api/task"

def check_bankruptcy():
    payload = {
        "agent": "DestinyAgent",
        "action": "check_status",
        "current_balance": -500000, # Contoh pemain hutang
        "assets": []
    }
    res = requests.post(URL, json=payload)
    # Jika balance minus dan tidak ada aset yang bisa dijual
    if res.json().get("current_balance", 0) < 0:
        print("💀 STATUS: BANGKRUT! Menghapus data pemain... Silakan Restart.")
    else:
        print("✅ Masih bisa bertahan.")

if __name__ == "__main__":
    check_bankruptcy()
