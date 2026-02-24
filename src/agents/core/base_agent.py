#!/usr/bin/env python3

class BaseAgent:
    def __init__(self, bus, db):
        self.bus = bus
        self.db = db
        self.name = self.__class__.__name__

    async def report_success(self, task_id, data):
        await self.bus.emit("task_success", {
            "id": task_id,
            "agent": self.name,
            "data": data
        })

    async def report_error(self, task_id, error):
        await self.bus.emit("task_failed", {
            "id": task_id,
            "agent": self.name,
            "error": error
        })
