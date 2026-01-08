import uuid
import time

class WorldNode:
    def __init__(self, agent: str, action: str, data: dict):
        self.id = str(uuid.uuid4())
        self.agent = agent
        self.action = action
        self.data = data
        self.timestamp = time.time()

    def serialize(self):
        return {
            "id": self.id,
            "agent": self.agent,
            "action": self.action,
            "data": self.data,
            "timestamp": self.timestamp
        }
