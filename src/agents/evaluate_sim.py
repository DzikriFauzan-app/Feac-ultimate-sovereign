import requests
URL = "http://10.4.35.107:8080/api/task"
payload = {
    "agent": "SentienceEvaluatorAgent",
    "has_inflation": True,
    "has_health_risk": True,
    "has_household_cost": True,
    "time_scale": "10min/day"
}
res = requests.post(URL, json=payload)
print(f"⚖️  SIMULATION AUDIT: {res.json()}")
