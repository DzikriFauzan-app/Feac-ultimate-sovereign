class BuildAgent:
    def __init__(self, agent_manager=None, config=None, extra=None):
        self.name = "BuildAgent"

    async def execute(self, task_data):
        return {"status": "success", "msg": "Build validation complete"}
