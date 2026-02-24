import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "CodeAgent",
            "instruction": "Optimize Sudoku Solver with Heuristics",
            "command": "process_task"
        },
        {
            "agent": "PilotAgent",
            "instruction": "Solve 10 Verified Sudoku Puzzles",
            "command": "process_task",
            "params": {"duration": 15}
        }
    ]
}

print("🧠 Mengoptimalkan Logika Matematika Agen...")
try:
    # Naikkan timeout ke 60 detik agar agen punya ruang napas
    r = requests.post(url, json=payload, timeout=60)
    data = r.json()
    res = data['results'][1]
    print(f"\n✅ LOGIKA MATEMATIKA STABIL!")
    print(f"🕹️ Solver Performance: {res['performance']}")
except Exception as e:
    print(f"❌ Masih Timeout: {e}")
    print("💡 Saran: Jalankan 'pm2 restart all' untuk membersihkan cache logika yang tersangkut.")
