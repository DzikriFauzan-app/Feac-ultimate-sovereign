from agents.BaseAgent import BaseAgent
from core.policy.engine import PolicyEngine

class FEACBridge:
    @staticmethod
    def emit(agent_name: str, action: str, payload: dict):
        # POLICY GATE (HARD LAW)
        policy = PolicyEngine.evaluate(
            agent=agent_name,
            action=action,
            payload=payload
        )

        if not policy["allowed"]:
            return {
                "blocked": True,
                "agent": agent_name,
                "action": action,
                "violations": policy["violations"]
            }

        # LEGAL ACTION -> EMIT EVENT
        return BaseAgent.emit_kernel_event(
            agent_name=f"FEAC::{agent_name}",
            action=action,
            payload=payload
        )
