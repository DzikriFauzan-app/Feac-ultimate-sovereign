from core.policy.engine import PolicyEngine
from core.policy.risk_policy import RiskPolicy
from agents.BaseAgent import BaseAgent

class FEACBridge:
    @staticmethod
    def emit(agent_name: str, action: str, payload: dict):
        # 1. HUKUM TERTULIS (STATIC)
        policy = PolicyEngine.evaluate(agent_name, action, payload)
        if not policy["allowed"]:
            return {"blocked": True, "stage": "POLICY_ENGINE", "violations": policy["violations"]}

        # 2. HUKUM PREDIKTIF (LOGIC)
        risk = RiskPolicy.evaluate(BaseAgent._world_graph, agent_name, action)
        if not risk["allowed"]:
            return {
                "blocked": True, 
                "stage": "RISK_POLICY", 
                "rule": risk["rule"], 
                "paths": risk["paths"]
            }

        # 3. EMIT FINAL
        return BaseAgent.emit_kernel_event(
            agent_name=f"FEAC::{agent_name}",
            action=action,
            payload=payload
        )
