from agents.BaseAgent import BaseAgent

class AISupervisor(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)

    async def process_task(self, task: dict):
        cmd = task.get("command")
        params = task.get("params", {})
        tid = task.get("id")

        # Debug fallback
        return {"status": "error", "msg": f"Command {cmd} not implemented by Supervisor", "tid": tid}
