import os
import json

class WorldAgent:
    def __init__(self, bus=None, db=None):
        self.name = "WorldAgent"
        self.base_path = "/sdcard/Buku saya/Fauzan engine/NeoEngine/storage/world_data"
        os.makedirs(self.base_path, exist_ok=True)

    async def process_task(self, task):
        params = task.get("params", {})
        project = params.get("project_name", "Global")
        world_type = params.get("world_type", "OpenWorld")
        
        # Logika pembentukan dunia
        world_config = {
            "type": world_type,
            "entities": [],
            "engine_target": params.get("engine", "Unity")
        }
        
        path = os.path.join(self.base_path, f"{project}_config.json")
        with open(path, "w") as f:
            json.dump(world_config, f, indent=4)
            
        return {"status": "world_defined", "path": path, "engine": world_config["engine_target"]}
