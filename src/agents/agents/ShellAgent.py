from agents.BaseAgent import BaseAgent
import subprocess

class ShellAgent(BaseAgent):
    def __init__(self, bus, db):
        super().__init__(bus, db)

    async def process_task(self, task: dict):
        tid = task.get("id")
        cmd = task.get("command")
        params = task.get("params", {})

        if cmd == "echo":
            text = params.get("text", "")
            return await self.report_success(tid, {"output": text})

        if cmd == "ls":
            path = params.get("path", ".")
            try:
                proc = subprocess.run(["ls", "-la", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                out = proc.stdout.strip() if proc.stdout else proc.stderr.strip()
                return await self.report_success(tid, {"output": out})
            except Exception as e:
                return await self.report_error(tid, str(e))

        return await self.report_error(tid, f"Unknown command: {cmd}")
