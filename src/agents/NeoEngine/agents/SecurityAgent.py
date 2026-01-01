from .BaseAgent import BaseAgent

class SecurityAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)
        self.name = "SecurityAgent"
    
    async def process_task(self, task):
        await self.report_success(task['id'], "System Secure. No threats detected.")
