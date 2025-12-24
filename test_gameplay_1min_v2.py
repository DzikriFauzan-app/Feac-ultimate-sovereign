import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "PilotAgent",
            "instruction": "Live Gameplay Stress Test 1 Min",
            "command": "process_task",
            "params": {"duration": 60}
        }
    ]
}

print("🎮 [RE-TRY] MEMULAI SIMULASI PLAYABLE (60 DETIK)...")
print("🔥 Sistem telah di-restart. Menghubungi PilotAgent...")

try:
    r = requests.post(url, json=payload, timeout=75)
    data = r.json()
    
    # Debugging: Cek struktur response asli
    result = data.get('results', [{}])[0]
    
    if result.get('status') == 'success':
        fps = result.get('avg_fps', 0)
        print("\n📊 HASIL STRESS TEST FINAL:")
        print(f"🕹️ Average FPS: {fps:.2f}")
        print(f"🎞️ Total Frames: {result.get('total_frames', 0)}")
        print(f"🏆 Rank: {result.get('performance', 'Unknown')}")
        
        if fps >= 55:
            print("✅ KUALITAS: WORLD CLASS (Siap Build MLBB/Perfect World)")
        else:
            print("⚠️ KUALITAS: BUTUH OPTIMASI (Frame drop terdeteksi)")
    else:
        print(f"❌ Agen Gagal Merespons: {result.get('msg', 'Error Unknown')}")

except Exception as e:
    print(f"❌ Koneksi Error: {e}")
