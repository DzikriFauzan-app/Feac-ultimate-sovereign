from core.policy.engine import PolicyEngine
from core.policy.risk_policy import RiskPolicy
from agents.BaseAgent import BaseAgent

class FEACBridge:
    @staticmethod
    def emit(agent_name: str, action: str, payload: dict):
        policy = PolicyEngine.evaluate(agent_name, action, payload)
        if not policy["allowed"]:
            return {"blocked": True, "stage": "POLICY", "violations": policy["violations"]}

        # Sekarang RiskPolicy menerima payload untuk evaluasi spesifik
        risk = RiskPolicy.evaluate(BaseAgent._world_graph, agent_name, action, payload)
        if not risk["allowed"]:
            return {"blocked": True, "stage": "RISK_FUSION", "rule": risk["rule"], "paths": risk["paths"]}

        return BaseAgent.emit_kernel_event(f"FEAC::{agent_name}", action, payload)
