import os
from .BaseAgent import BaseAgent

class CodeAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)
        self.name = "CodeAgent"
        self.capabilities = ["write_file", "scan_files"]

    async def process_task(self, task):
        cmd = task['command']
        params = task['params']
        task_id = task['id']
        
        if cmd == "write_file":
            try:
                with open(params['filename'], 'w') as f:
                    f.write(params['content'])
                await self.report_success(task_id, "File written successfully")
            except Exception as e:
                await self.report_error(task_id, e)
        elif cmd == "scan_files":
             files = [f for f in os.listdir('.') if os.path.isfile(f)]
             await self.report_success(task_id, {"files": files})
