import requests

URL = "http://10.4.35.107:8080/api/task"

def setup_rankings():
    rank_system = {
        "agent": "EconomyAgent",
        "action": "setup_progression",
        "tiers": [
            {"name": "PKL_Kere", "min_assets": 0},
            {"name": "Juragan_Lapak", "min_assets": 100000000}, # 100 Juta
            {"name": "Bos_Supermarket", "min_assets": 1000000000}, # 1 Milyar
            {"name": "CEO_Holding_Company", "min_assets": 50000000000} # 50 Milyar
        ],
        "leaderboard_metrics": ["Profit_Growth", "Health_Stability", "Visionary_Score"]
    }
    res = requests.post(URL, json=rank_system)
    print(f"🏆 Leaderboard & Tier System: {res.json()}")

if __name__ == "__main__":
    setup_rankings()
