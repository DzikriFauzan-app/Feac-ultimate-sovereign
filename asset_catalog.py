import json
import os

CATALOG_FILE = os.path.expanduser("~/neo_internal/core/asset_catalog.json")

def define_assets():
    catalog = {
        "structures": {
            "wall_stone_01": {"mesh": "stone_wall.obj", "texture": "gray_brick.png"},
            "roof_tile_01": {"mesh": "oriental_roof.obj", "texture": "clay_red.png"}
        },
        "props": {
            "elder_statue": {"mesh": "elder_venerated.obj", "scale": 5.0},
            "market_stall": {"mesh": "stall_wood.obj", "interactive": True}
        },
        "vegetation": {
            "pine_tree_01": {"mesh": "pine_low_poly.obj", "animation": "wind_sway"}
        }
    }
    
    with open(CATALOG_FILE, "w") as f:
        json.dump(catalog, f)
    print("💎 MICRO BLUEPRINT: Katalog Asset Terkecil Terdaftar.")

if __name__ == "__main__":
    define_assets()
