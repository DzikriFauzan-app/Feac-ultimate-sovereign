import requests

# Kita coba tembak port 8080 (Neo Master)
url = "http://127.0.0.1:8080/api/task"
payload = {
    "task": "SIMULATION_BUILD_MLBB",
    "owner": "ARIES_SOVEREIGN",
    "priority": "ULTIMATE"
}

print("🚀 Testing Neo Engine Task Endpoint...")
try:
    r = requests.post(url, json=payload, timeout=5)
    print(f"Status Code: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"❌ Koneksi gagal: {e}")
    print("💡 Kemungkinan besar websocket_server.py belum berjalan di port 8080.")
