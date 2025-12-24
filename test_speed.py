import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {"instruction": "Build MLBB Clone", "priority": "MAX"}

start_time = time.time()
try:
    r = requests.post(url, json=payload, timeout=5)
    end_time = time.time()
    print(f"🚀 RESPONS DITERIMA DALAM: {round(end_time - start_time, 4)} detik")
    print(f"STATUS: {r.status_code}")
    print(f"DATA: {r.text}")
except Exception as e:
    print(f"❌ Gagal: {e}")
