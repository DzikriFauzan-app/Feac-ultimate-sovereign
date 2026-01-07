from typing import Dict
from core.world_graph.query import WorldGraphQuery

NEGATIVE_ACTIONS = {"fail", "error", "crisis", "collapse"}

class DecisionFeedback:
    """
    Kernel-level Decision Feedback Loop: Mencegah kegagalan berulang.
    """
    @staticmethod
    def evaluate(graph, agent_name: str, action: str, payload: Dict) -> Dict:
        snapshot = graph.snapshot()
        nodes = snapshot["nodes"]
        
        similar_events = [
            n for n in nodes
            if n["data"].get("agent") == agent_name
            and n["data"].get("action") == action
        ]

        risk = False
        reasons = []

        for ev in similar_events:
            effects = WorldGraphQuery.get_effects(graph, ev["id"])
            for eff_id in effects:
                eff_node = next((x for x in nodes if x["id"] == eff_id), None)
                if eff_node:
                    act = eff_node["data"].get("action", "").lower()
                    if act in NEGATIVE_ACTIONS:
                        risk = True
                        reasons.append(f"Past action led to negative effect: {act}")

        return {
            "agent": agent_name,
            "action": action,
            "historical_events": len(similar_events),
            "risk_detected": risk,
            "advice": "BLOCK" if risk else "ALLOW",
            "reasons": reasons
        }
