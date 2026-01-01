from .BaseAgent import BaseAgent

class AssetGeneratorAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)
        self.name = "AssetGeneratorAgent"
    
    async def process_task(self, task):
        await self.report_success(task['id'], "Asset Generated: sprite.png")
