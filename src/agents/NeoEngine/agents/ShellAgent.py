import asyncio
from .BaseAgent import BaseAgent

class ShellAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)
        self.name = "ShellAgent"
        self.capabilities = ["run_command"]

    async def process_task(self, task):
        cmd = task['params'].get('cmd')
        task_id = task['id']
        try:
            proc = await asyncio.create_subprocess_shell(
                cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()
            result = {"stdout": stdout.decode().strip(), "stderr": stderr.decode().strip()}
            await self.report_success(task_id, result)
        except Exception as e:
            await self.report_error(task_id, e)
