import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "CodeAgent",
            "instruction": "Compile Sudoku Logic to Executable",
            "command": "process_task"
        },
        {
            "agent": "PilotAgent",
            "instruction": "Solve Sudoku Puzzle 100x",
            "command": "process_task",
            "params": {"duration": 10}
        }
    ]
}

print("🎯 Mengetes Logika Permainan Sudoku...")
r = requests.post(url, json=payload, timeout=30)
res = r.json()['results'][1]
print(f"\n✅ LOGIKA SELESAI!")
print(f"🕹️ Solver Stability: {res['performance']}")
print(f"📊 Path: /Projects/Sovereign_Sudoku/")
