#!/usr/bin/env python3
import asyncio
import json

class BaseAgent:
    def __init__(self, bus, db):
        # bus: MessageBus instance
        # db: Database instance
        self.bus = bus
        self.db = db
        self.name = self.__class__.__name__

    async def report_success(self, task_id: str, data: dict):
        """
        Standardize success reporting:
        - publish to bus if available
        - return payload so caller (engine/bridge) can forward immediately
        """
        payload = {
            "id": task_id,
            "agent": self.name,
            "status": "success",
            "result": data
        }
        # Try publish if bus implements it; ignore failures but log via print
        try:
            if hasattr(self.bus, "publish"):
                maybe = self.bus.publish("task_success", payload)
                # if publish is coroutine, await it
                if asyncio.iscoroutine(maybe):
                    await maybe
        except Exception as e:
            print(f"[BaseAgent] publish task_success failed: {e}")

        # Return payload for immediate forwarding by bridge
        return payload

    async def report_error(self, task_id: str, error: str):
        """
        Standardize error reporting:
        - publish to bus if available
        - return payload so caller (engine/bridge) can forward immediately
        """
        payload = {
            "id": task_id,
            "agent": self.name,
            "status": "failed",
            "error": str(error)
        }
        try:
            if hasattr(self.bus, "publish"):
                maybe = self.bus.publish("task_failed", payload)
                if asyncio.iscoroutine(maybe):
                    await maybe
        except Exception as e:
            print(f"[BaseAgent] publish task_failed failed: {e}")

        return payload
