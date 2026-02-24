import asyncio
import uuid
from .message_bus import MessageBus
from .database import Database

class Scheduler:
    def __init__(self, bus: MessageBus, db: Database):
        self.bus = bus
        self.db = db
        self.queue = asyncio.Queue()
        self.active = True

    async def start(self):
        workers = [asyncio.create_task(self.worker(i)) for i in range(4)]
        await asyncio.gather(*workers)

    async def schedule_task(self, agent_name: str, command: str, params: dict):
        task_id = str(uuid.uuid4())
        task = {"id": task_id, "agent": agent_name, "command": command, "params": params}
        self.db.add_task(task_id, command, params)
        await self.queue.put(task)
        await self.bus.publish("task_scheduled", task)
        return task_id

    async def worker(self, worker_id):
        while self.active:
            try:
                task = await self.queue.get()
                await self.bus.publish("task_started", {"worker": worker_id, "task": task})
                event_name = f"{task['agent']}:execute"
                await self.bus.publish(event_name, task)
                self.queue.task_done()
            except Exception as e:
                print(f"Worker {worker_id} Error: {e}")
