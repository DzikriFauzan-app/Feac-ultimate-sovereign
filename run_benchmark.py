import requests
import json

payload = {
    "tasks": [{
        "agent": "BenchmarkAgent",
        "action": "run_simulation",
        "params": {"target_fps": 60, "entities": 1000}
    }]
}
r = requests.post("http://127.0.0.1:8080/api/task", json=payload)
print(json.dumps(r.json(), indent=4))
