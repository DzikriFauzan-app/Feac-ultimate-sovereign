import requests

URL = "http://10.4.35.107:8080/api/task"

def run_stress_test():
    payload = {
        "agent": "SentientTesterAgent",
        "action": "spawn_crowd",
        "count": 50,
        "behavior": "wandering_and_buying"
    }
    res = requests.post(URL, json=payload)
    print(f"👥 NPC Stress Test: {res.json()}")

if __name__ == "__main__":
    run_stress_test()
