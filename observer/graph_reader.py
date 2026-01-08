from agents.BaseAgent import BaseAgent
class GraphSnapshotReader:
    @staticmethod
    def snapshot():
        wg = BaseAgent._world_graph
        snap = wg.snapshot()
        return {"nodes": snap.get("nodes", []), "edges": snap.get("edges", [])}
