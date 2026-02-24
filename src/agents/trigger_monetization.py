import requests

URL = "http://10.4.35.107:8080/api/task"

def setup_whale_bundle():
    payload = {
        "agent": "WhaleRetentionAgent",
        "action": "activate_gold_bundle",
        "price": 49990,
        "perks": {
            "inflation_resistance": "100%",
            "deflation_resistance": "100%",
            "sell_price_bonus": "+20%",
            "hpp_reduction": "-20%",
            "tax_reduction": "-20%",
            "consumer_stability": "MAX"
        }
    }
    res = requests.post(URL, json=payload)
    print(f"💎 Premium Bundle: {res.json()}")

if __name__ == "__main__":
    setup_whale_bundle()
