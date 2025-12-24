import requests

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "AISupervisor", 
            "instruction": "Initiate MLBB Project",
            "command": "deploy"
        },
        {
            "agent": "ResearchAgent",
            "instruction": "Analyze MLBB Mechanics",
            "command": "research"
        }
    ]
}

try:
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
