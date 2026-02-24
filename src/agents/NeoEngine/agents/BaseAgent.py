class BaseAgent:
    def __init__(self, bus, db):
        self.bus = bus
        self.db = db
        self.name = "BaseAgent"
        self.capabilities = []

    def start(self):
        self.db.log_agent(self.name, "ONLINE", self.capabilities)
        self.bus.subscribe(f"{self.name}:execute", self.process_task)

    async def process_task(self, task):
        pass

    async def report_success(self, task_id, result):
        self.db.update_task(task_id, "COMPLETED", result)
        await self.bus.publish("task_completed", {"id": task_id, "agent": self.name, "result": result})

    async def report_error(self, task_id, error):
        self.db.update_task(task_id, "FAILED", {"error": str(error)})
        await self.bus.publish("task_failed", {"id": task_id, "agent": self.name, "error": str(error)})
