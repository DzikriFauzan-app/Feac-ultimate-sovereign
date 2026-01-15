import sys
import os
import json

STATE_FILE = os.path.expanduser("~/neo_internal/core/city_blueprint.json")

def create_archosaur_layout():
    blueprint = {
        "city_name": "Archosaur City",
        "sectors": {
            "North_Gate": {"offset": [0, 250], "type": "fortification"},
            "South_Gate": {"offset": [0, -250], "type": "fortification"},
            "Elder_Platform": {"offset": [0, 0], "type": "central_hub"},
            "Market_District": {"offset": [150, 150], "type": "commercial"}
        },
        "style": "Ancient_Oriental_High_Fantasy"
    }
    
    with open(STATE_FILE, "w") as f:
        json.dump(blueprint, f)
    print("🏛️  MESO BLUEPRINT: Struktur Archosaur City Dirancang.")

if __name__ == "__main__":
    create_archosaur_layout()
