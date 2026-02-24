import requests
import time

URL = "http://10.4.35.107:8080/api/task"

def start_dynamic_crowd():
    # Total target 300 NPC dalam 1 hari game (10 menit)
    # Dibagi menjadi 5 gelombang (Pagi, Siang, Sore, Malam, Larut)
    waves = ["Pagi", "Siang_Ramai", "Sore", "Malam_Puncak", "Larut"]
    
    for wave in waves:
        payload = {
            "agent": "CrowdSimulationAgent",
            "action": "spawn_wave",
            "params": {
                "wave_name": wave,
                "count": 60, # Total 300 NPC (5 wave x 60)
                "entry_speed": "gradual",
                "target_booth": "Bakso_Master"
            }
        }
        res = requests.post(URL, json=payload)
        print(f"🌊 Wave {wave} Injected: {res.json().get('status')}")
        # Dalam realitas game, ini akan dipicu oleh internal clock setiap 2 menit
