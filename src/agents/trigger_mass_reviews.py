import requests

URL = "http://10.4.35.107:8080/api/task"

def simulate_reputation():
    # 490 Orang Puas (Rasio 1:1 Daging Segar)
    for _ in range(49): # Kita ringkas skalanya untuk simulasi cepat
        requests.post(URL, json={
            "agent": "MarketingAgent",
            "action": "generate_review",
            "daging_ratio": 1, "tepung_ratio": 1, "is_fresh": True
        })
    
    # 10 Orang Kecewa (Daging Tidak Segar)
    requests.post(URL, json={
        "agent": "MarketingAgent",
        "action": "generate_review",
        "is_fresh": False
    })

    # Cek Multiplier Traffic
    res = requests.post(URL, json={"agent": "MarketingAgent", "action": "get_traffic_multiplier"})
    print(f"📈 Reputasi Toko: {res.json()}")

if __name__ == "__main__":
    simulate_reputation()
