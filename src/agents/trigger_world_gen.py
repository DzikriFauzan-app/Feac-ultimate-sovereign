import requests

URL = "http://10.4.35.107:8080/api/task"

def build_world():
    payload = {
        "agent": "MapGeneratorAgent",
        "action": "generate_layout",
        "params": {
            "theme": "Pasar_Malam_Indonesia",
            "assets": ["Gerobak_Martabak", "Bianglala_Ancient", "Lampu_Kelap_Kelip"],
            "density": 0.8
        }
    }
    res = requests.post(URL, json=payload)
    print(f"🏗️  World Gen Status: {res.json()}")

if __name__ == "__main__":
    build_world()
