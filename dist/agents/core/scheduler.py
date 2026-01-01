import asyncio
import uuid
from core.database import Database

class Scheduler:
    def __init__(self, bus, db: Database):
        self.bus = bus
        self.db = db
        self.queue = asyncio.Queue()
        self.active = True
        self.workers = []

    async def start(self):
        # start worker pool
        for i in range(4):
            w = asyncio.create_task(self.worker(i))
            self.workers.append(w)
        # keep alive
        await asyncio.gather(*self.workers)

    async def schedule_task(self, agent_name: str, command: str, params: dict):
        task_id = str(uuid.uuid4())
        task = {
            "id": task_id,
            "agent": agent_name,
            "command": command,
            "params": params
        }
        self.db.add_task(task_id, agent_name, command, params)
        await self.queue.put(task)
        await self.bus.publish("task_scheduled", task)
        return task_id

    async def worker(self, worker_id):
        while self.active:
            try:
                task = await self.queue.get()
                await self.bus.publish("task_started", {"worker": worker_id, "task": task})
                # notify agent channel: "<AgentName>:execute"
                event_name = f"{task['agent']}:execute"
                await self.bus.publish(event_name, task)
                # no direct result handling here; agents call db/report via bus
                self.queue.task_done()
            except Exception as e:
                print(f"[Scheduler Worker {worker_id}] error: {e}")
