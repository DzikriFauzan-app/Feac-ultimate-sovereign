import requests
import concurrent.futures

def trigger_agent(agent_name):
    # Sesuaikan dengan endpoint Neo Engine (Port 8080)
    url = "http://127.0.0.1:8080/execute"
    payload = {"action": "STRESS_TEST", "agent": agent_name}
    try:
        r = requests.post(url, json=payload, timeout=5)
        return f"{agent_name}: {r.status_code}"
    except:
        return f"{agent_name}: CONNECTION_FAILED"

agents = ["ResearchAgent", "ShellAgent", "CodeAgent", "RenderAgent", "LogicNodeAgent"]
print("🚀 Memulai Stress Test pada 39 Agen...")
with concurrent.futures.ThreadPoolExecutor(max_workers=39) as executor:
    results = list(executor.map(trigger_agent, agents * 5))
    for res in results:
        print(res)
