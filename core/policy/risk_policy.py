from core.decision.recursive_reasoning import RecursiveReasoning

class RiskPolicy:
    """
    PREVENT_CHAIN_COLLAPSE — Predictive Law: Mencegah takdir buruk berulang.
    """
    @staticmethod
    def evaluate(world_graph, agent_name: str, action: str):
        snap = world_graph.snapshot()
        nodes = snap["nodes"]
        # Cari pola aksi serupa di masa lalu
        historical = [
            n for n in nodes 
            if n["data"].get("agent") == f"FEAC::{agent_name}" 
            and n["data"].get("action") == action
        ]
        
        dangerous_paths = []
        for ev in historical:
            result = RecursiveReasoning.trace_effects(world_graph, ev["id"])
            if result["negative_detected"]:
                dangerous_paths.extend(result["paths"])
        
        if dangerous_paths:
            return {
                "allowed": False,
                "rule": "PREVENT_CHAIN_COLLAPSE",
                "description": "Aksi serupa di masa lalu terbukti memicu krisis",
                "paths": dangerous_paths
            }
        return {"allowed": True}
