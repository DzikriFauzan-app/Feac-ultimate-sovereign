class TaskAgent:
    def __init__(self, bus=None, db=None, memory_agent=None):
        self.bus = bus
        self.db = db
        self.memory = memory_agent

    async def process_task(self, task):
        return {"status": "task_processed", "agent": "TaskAgent"}
