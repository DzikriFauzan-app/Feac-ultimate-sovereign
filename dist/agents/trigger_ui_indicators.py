import requests

URL = "http://10.4.35.107:8080/api/task"

def setup_freshness_ui():
    payload = {
        "agent": "UIAgent",
        "action": "render_status_bar",
        "params": {
            "label": "Kesejukan Daging",
            "initial_value": 100, # 100% Segar
            "decay_logic": "Time_Based",
            "fridge_multiplier": 0.1, # Melambat 10x jika ada kulkas
            "warning_threshold": 30,
            "colors": {"high": "Green", "low": "Red"}
        }
    }
    res = requests.post(URL, json=payload)
    print(f"📊 UI Indicator Active: {res.json()}")

if __name__ == "__main__":
    setup_freshness_ui()
