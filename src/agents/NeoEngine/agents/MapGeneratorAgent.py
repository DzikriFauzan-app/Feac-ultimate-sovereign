from .BaseAgent import BaseAgent

class MapGeneratorAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)
        self.name = "MapGeneratorAgent"
    
    async def process_task(self, task):
        await self.report_success(task['id'], "Map Generated: level_1.json")
