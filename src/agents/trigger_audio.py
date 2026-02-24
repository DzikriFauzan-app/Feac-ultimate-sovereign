import requests

URL = "http://10.4.35.107:8080/api/task"

def setup_audio():
    payload = {
        "agent": "AudioAgent",
        "action": "synthesize_ambience",
        "params": {
            "environment": "Pasar_Malam_Crowded",
            "layers": ["Spatula_Sound", "Child_Laughter", "Motorcycle_Far"],
            "music_style": "Keroncong_Lofi_Beats"
        }
    }
    res = requests.post(URL, json=payload)
    print(f"🔊 Audio Layering: {res.json()}")

if __name__ == "__main__":
    setup_audio()
