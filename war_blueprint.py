import sys
import os
sys.path.insert(0, os.path.expanduser("~/neo_internal"))
from core.world_registry import WorldRegistry

def setup_war_entities():
    # Definisikan Markas Utama (Base)
    WorldRegistry.register_region("Command_Center", "base", spatial={
        "coords": {"x": 550, "y": 650, "z": 20},
        "hp": 1000,
        "alignment": "PLAYER"
    })
    
    # Definisikan Garis Depan Musuh (Enemy Front)
    WorldRegistry.register_region("Enemy_Camp", "outpost", spatial={
        "coords": {"x": 550, "y": 950, "z": 15},
        "hp": 500,
        "alignment": "ENEMY"
    })
    print("⚔️  WAR BLUEPRINT: Combat Entities Deployed.")

if __name__ == "__main__":
    setup_war_entities()
