import requests
import time

url = "http://127.0.0.1:8080/api/task"

print("🗺️ Generating 1,500,000 Terrain Nodes (Perfect World Scale)...")
# Membuat koordinat X, Y, Z untuk 1.5 juta titik
terrain_nodes = [{"x": i, "y": i*0.5, "z": i%100} for i in range(1500000)]

payload = {
    "tasks": [
        {
            "agent": "MapGeneratorAgent",
            "instruction": "Initialize Open World Terrain",
            "command": "process_task",
            "params": {"nodes": terrain_nodes}
        }
    ]
}

print("🔥 Injecting World Map to Neo Engine...")
start_time = time.time()

try:
    # Timeout 120 detik karena data sangat masif
    r = requests.post(url, json=payload, timeout=120)
    duration = time.time() - start_time
    print(f"\n✅ WORLD GENERATION COMPLETE!")
    print(f"⏱️ Waktu Eksekusi: {duration:.2f} detik")
    print(f"📊 Status: {r.status_code}")
except Exception as e:
    print(f"❌ System Overload: {e}")
