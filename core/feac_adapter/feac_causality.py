from core.world_graph.edge import WorldEdge
from agents.BaseAgent import BaseAgent

class FEACCausality:
    """
    Utility untuk menghubungkan aksi antar Agent FEAC secara kausal.
    """
    @staticmethod
    def depends_on(source_event_id: str, target_event_id: str, reason: str):
        edge = WorldEdge(
            source_id=source_event_id,
            target_id=target_event_id,
            relation="DEPENDS_ON",
            meta={"reason": reason}
        )
        BaseAgent._world_graph.add_edge(edge)
        return edge.id
