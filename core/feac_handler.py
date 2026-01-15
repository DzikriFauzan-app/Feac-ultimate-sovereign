from core.world_registry import WorldRegistry

class FEACHandler:
    @staticmethod
    def process_action(agent_name, action, payload):
        region_name = agent_name.replace("FEAC::", "")
        region = WorldRegistry.get_all().get(region_name)
        
        if not region:
            return {"status": "REJECTED", "reason": "REGION_NOT_FOUND"}
            
        if action == "produce" and payload.get("qty") == 0:
            WorldRegistry.regions[region_name]["status"] = "CRISIS"
            return {"status": "ALERT", "msg": f"{region_name} entering CRISIS state"}
            
        return {"status": "SUCCESS"}
