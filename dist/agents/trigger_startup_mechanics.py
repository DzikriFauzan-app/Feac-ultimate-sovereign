import requests

URL = "http://10.4.35.107:8080/api/task"

def setup_new_player():
    setup = {
        "agent": "EconomyAgent",
        "action": "init_player_account",
        "initial_balance": 20000000,
        "tutorial_steps": [
            "1. Pilih Gerobak (Kayu 1 vs Besi)",
            "2. Survey Lokasi (Ruko vs Kaki Lima)",
            "3. Beli Inventori (Daging, Tepung, Gas)",
            "4. Manajemen Skill (Peluang Ramai)"
        ],
        "risk_factors": {
            "salah_lokasi": "Bangkrut dalam 7 hari",
            "over_spending": "Gagal bayar kontrakan bulan ke-2"
        }
    }
    res = requests.post(URL, json=setup)
    print(f"💼 Startup Protocol: {res.json()}")

if __name__ == "__main__":
    setup_new_player()
