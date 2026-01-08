from core.decision.recursive_reasoning import RecursiveReasoning

class RiskPolicy:
    @staticmethod
    def evaluate(world_graph, agent_name, action, payload):
        # Aksi produktif tidak boleh nol (Aksiom Sovereign)
        if any(isinstance(v, (int, float)) and v == 0 for v in payload.values()):
            return {"blocked": True, "rule": "ZERO_GUARD"}

        # Pengecekan Sejarah Berantai
        snap = world_graph.snapshot()
        historical = [n for n in snap["nodes"] if n["data"].get("action") == action and n["data"].get("payload") == payload]
        for ev in historical:
            if RecursiveReasoning.trace_effects(world_graph, ev["id"]).get("negative_detected"):
                return {"blocked": True, "rule": "PREVENT_CHAIN_COLLAPSE"}
        
        return {"allowed": True}
