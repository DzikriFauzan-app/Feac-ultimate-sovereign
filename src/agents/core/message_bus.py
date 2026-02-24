import asyncio

class MessageBus:
    def __init__(self):
        self.listeners = {}  # event → callback

    def subscribe(self, event, callback):
        self.listeners[event] = callback

    async def publish(self, event, payload):
        if event in self.listeners:
            cb = self.listeners[event]
            if asyncio.iscoroutinefunction(cb):
                await cb(payload)
            else:
                cb(payload)
