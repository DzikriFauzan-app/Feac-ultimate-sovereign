from agents.BaseAgent import BaseAgent

class AssetGeneratorAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)

    async def process_task(self, task: dict):
        cmd = task.get("command")
        params = task.get("params", {})
        tid = task.get("id")

        # Debug fallback
        await self.report_error(tid, f"Command not implemented: {cmd}")
