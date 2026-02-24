class EconomyAgent:
    def __init__(self):
        self.name = "EconomyAgent"
        self.initial_modal = 20000000
        
    async def execute(self, task):
        action = task.get("action")
        if action == "check_tier":
            assets = task.get("assets_value", 0)
            if assets >= 50000000000: return "CEO_Holding_Company"
            if assets >= 1000000000: return "Bos_Supermarket"
            if assets >= 100000000: return "Juragan_Lapak"
            return "PKL_Kere"
        return {"status": "Economy_Synced", "modal_awal": self.initial_modal}
