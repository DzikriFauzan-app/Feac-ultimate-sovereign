import requests
import time
import sys

url = "http://127.0.0.1:8080/api/task"

# Simulasi 500.000 entri data (500k)
print("📦 Menyiapkan 500,000 data entri...")
large_data = [{"id": i, "meta": "asset_data_simulation_mlbb_modern_render"} for i in range(500000)]

payload = {
    "tasks": [
        {
            "agent": "OptiAgent",
            "instruction": "Stress Test Memory 500k",
            "command": "process_task",
            "params": {"data_stream": large_data}
        }
    ]
}

print("🔥 Mengirim 500k entri ke Neo Engine...")
start_time = time.time()

try:
    # Timeout diperpanjang karena payload sangat besar
    r = requests.post(url, json=payload, timeout=60)
    duration = time.time() - start_time
    print(f"✅ Berhasil! Waktu proses: {duration:.2f} detik")
    print(f"Response: {r.status_code}")
except Exception as e:
    print(f"❌ Gagal atau Terputus: {e}")
