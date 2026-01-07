import time
import uuid
from typing import Dict, Any

class WorldEdge:
    def __init__(self, source_id: str, target_id: str, relation: str, meta: Dict[str, Any] = None):
        self.id = str(uuid.uuid4())
        self.source = source_id
        self.target = target_id
        self.relation = relation
        self.meta = meta or {}
        self.timestamp = time.time()

    def serialize(self):
        return {
            "id": self.id,
            "source": self.source,
            "target": self.target,
            "relation": self.relation,
            "meta": self.meta,
            "timestamp": self.timestamp
        }
