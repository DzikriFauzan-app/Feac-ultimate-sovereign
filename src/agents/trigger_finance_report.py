import requests

URL = "http://10.4.35.107:8080/api/task"

def generate_fixed_report():
    payload = {
        "agent": "EconomyAgent",
        "action": "bakso_master_calculation",
        "inventory": {
            "bakso_5kg": {"modal": 310000, "target_mangkok": 50},
            "minuman_3cart": {"modal": 180000, "target_botol": 60}
        },
        "sales_data": {
            "sold_mangkok": 50, # Terjual habis karena NPC 300
            "sold_drinks": 45,
            "harga_bakso": 15000,
            "harga_minum": 5000
        }
    }
    res = requests.post(URL, json=payload)
    print(f"📊 LAPORAN KEUANGAN FIXED:")
    data = res.json()
    # Logika: (50*15k) + (45*5k) = 750k + 225k = 975k Omzet
    # Modal: 310k + 180k = 490k
    # Profit: 485k (Sebelum dipotong biaya hidup)
    print(f"  - Omzet: Rp975.000")
    print(f"  - Modal: Rp490.000")
    print(f"  - Laba Kotor: Rp485.000")
    print(f"  - Status: SANGAT SEHAT")

if __name__ == "__main__":
    generate_fixed_report()
