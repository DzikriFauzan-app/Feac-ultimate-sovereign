import subprocess
from .BaseAgent import BaseAgent

class RepoAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)
        self.name = "RepoAgent"
        self.capabilities = ["git_status", "git_push"]

    async def process_task(self, task):
        cmd = task['command']
        task_id = task['id']
        try:
            if cmd == "git_status":
                res = subprocess.run(["git", "status"], capture_output=True, text=True)
                await self.report_success(task_id, res.stdout)
            elif cmd == "git_push":
                res = subprocess.run(["git", "push"], capture_output=True, text=True)
                await self.report_success(task_id, res.stdout)
        except Exception as e:
            await self.report_error(task_id, e)
