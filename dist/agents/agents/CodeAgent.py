import os

class CodeAgent:
    def __init__(self, agent_manager=None, db=None):
        self.name = "CodeAgent"
        self.output_dir = "/data/data/org.feac.ultimate.feac_sovereign/files/NeoEngine/storage/generated_code"
        os.makedirs(self.output_dir, exist_ok=True)

    async def execute(self, task_data):
        # Fitur Multi-Engine Injection
        params = task_data.get("params", {})
        engine_target = params.get("engine", "neo").lower() # unity, unreal, godot, neo
        task = params.get("task", "logic_module")
        
        exts = {"unreal": ".cpp", "unity": ".cs", "godot": ".gd", "neo": ".py"}
        ext = exts.get(engine_target, ".py")
        
        filename = f"Project_{engine_target}_{task}{ext}"
        path = os.path.join(self.output_dir, filename)
        
        # Logika Template Sesuai Engine (Multi-Capabilities)
        template = f"// Generated for {engine_target.upper()}\n"
        if engine_target == "unity":
            template += "using UnityEngine;\npublic class NewLogic : MonoBehaviour {}"
        elif engine_target == "unreal":
            template += "#include \"CoreMinimal.h\"\n// Unreal logic here"
            
        with open(path, "w") as f:
            f.write(template)
            
        return {"status": "success", "file": filename, "engine": engine_target}
