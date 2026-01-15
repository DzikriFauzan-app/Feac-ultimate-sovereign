import sys
import os
sys.path.insert(0, os.path.expanduser("~/neo_internal"))
from core.world_registry import WorldRegistry

def generate_world_blueprint():
    # Menanamkan koordinat langsung saat registrasi
    WorldRegistry.register_region("City_A", "city", spatial={
        "coords": {"x": 550, "y": 650, "z": 20},
        "size": 500,
        "biome": "Capital_Plains"
    })
    
    WorldRegistry.register_region("Forest_B", "forest", spatial={
        "coords": {"x": 550, "y": 950, "z": 15},
        "size": 800,
        "biome": "Deciduous_Forest"
    })
    print("🗺️  MACRO BLUEPRINT: Spasial Data Injected.")

if __name__ == "__main__":
    generate_world_blueprint()
