import requests

URL = "http://10.4.35.107:8080/api/task"

def render_visuals():
    payload = {
        "agent": "GodotAgent",
        "action": "apply_visual_shader",
        "target": "Gerobak_Kayu_01",
        "shader_params": {
            "glow_intensity": "High",
            "neon_color": "Cyan_Magenta",
            "dirt_texture": "Realistic_Mud",
            "smoke_particle": "Sate_Grill_Vapor"
        },
        "quality_score": 100
    }
    try:
        res = requests.post(URL, json=payload)
        print(f"🎨 Visual Synthesis: {res.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    render_visuals()
