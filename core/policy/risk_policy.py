from core.decision.recursive_reasoning import RecursiveReasoning

class RiskPolicy:
    @staticmethod
    def evaluate(world_graph, agent_name: str, action: str, payload: dict = None):
        snap = world_graph.snapshot()
        nodes = snap["nodes"]
        
        # Cari sejarah yang HANYA memiliki payload serupa (Contoh: qty yang sama)
        historical = [
            n for n in nodes 
            if n["data"].get("agent") == f"FEAC::{agent_name}" 
            and n["data"].get("action") == action
            and n["data"].get("payload") == payload # Pengecekan payload spesifik
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
                "description": "Aksi dengan payload ini terbukti memicu krisis",
                "paths": dangerous_paths
            }
        return {"allowed": True}
