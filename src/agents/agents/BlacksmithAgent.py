class BlacksmithAgent:
    def __init__(self):
        self.name = "BlacksmithAgent"
        self.materials = ["Kayu", "Paku", "Cat", "Besi", "Emas"]

    async def execute(self, task):
        action = task.get("action")
        current_level = task.get("current_level", 1)
        material_type = task.get("type", "Kayu")

        if action == "calculate_upgrade":
            # Logika kenaikan biaya eksponensial agar F2P sulit
            needed_wood = 10 * current_level
            needed_nails = 50 * current_level
            needed_paint = 3 * current_level
            return {
                "status": "UPGRADE_REQUIREMENT",
                "needs": {"Kayu": needed_wood, "Paku": needed_nails, "Cat": needed_paint},
                "next_level": f"{material_type} {current_level + 1}"
            }
