import requests

try:
    # Mencoba mengambil logs terakhir dari NeoEngine
    response = requests.get('http://localhost:8080/api/logs')
    print("\n📜 RECENT COUNCIL LOGS:")
    print(response.text[-500:]) # Ambil 500 karakter terakhir
except:
    print("❌ Failed to fetch logs.")

try:
    # Cek status TaskAgent
    res_task = requests.get('http://localhost:8080/api/task')
    print("\n⚙️  ACTIVE TASKS:")
    print(res_task.json())
except:
    print("⚠️  No active task data returned.")
