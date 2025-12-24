import requests
import time

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {
            "agent": "ScriptAgent",
            "instruction": "Generate 2000 Detailed Scenes for PW Lore",
            "command": "process_task",
            "params": {"scene_count": 2000, "detail_level": "cinematic"}
        },
        {
            "agent": "NarratorAgent",
            "instruction": "Calculate Voice-over Duration & Emotional Tone",
            "command": "process_task"
        }
    ]
}

print("🎙️ Memproses 2.000 Scene Narasi Perfect World...")
print("⏳ Mengalkulasi alur cerita dari Penciptaan Pangu hingga Perang Wraith...")
start = time.time()
r = requests.post(url, json=payload, timeout=120)
duration = time.time() - start

print(f"\n✅ NARRATIVE GENERATION COMPLETE!")
print(f"⏱️ Waktu Proses: {duration:.2f} detik")
print(f"📄 Estimasi Durasi Video: ~180 Menit (3 Jam Narasi)")
