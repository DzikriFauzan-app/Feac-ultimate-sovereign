from typing import List, Dict

class WorldGraphQuery:
    """
    Edge Query API: Navigasi sebab-akibat deterministik untuk FEAC.
    """
    @staticmethod
    def get_causes(graph, event_id: str) -> List[str]:
        return [e.get("target") for e in graph.edges if e.get("source") == event_id]

    @staticmethod
    def get_effects(graph, event_id: str) -> List[str]:
        return [e.get("source") for e in graph.edges if e.get("target") == event_id]

    @staticmethod
    def explain(graph, event_id: str) -> Dict:
        return {
            "event": event_id,
            "caused_by": WorldGraphQuery.get_causes(graph, event_id),
            "leads_to": WorldGraphQuery.get_effects(graph, event_id)
        }
