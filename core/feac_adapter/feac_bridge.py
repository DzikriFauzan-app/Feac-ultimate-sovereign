from agents.BaseAgent import BaseAgent

class FEACBridge:
    """
    Satu-satunya gerbang resmi FEAC Agent menuju NeoEngine Kernel.
    """
    @staticmethod
    def emit(agent_name: str, action: str, payload: dict):
        return BaseAgent.emit_kernel_event(
            agent_name=f"FEAC::{agent_name}",
            action=action,
            payload=payload
        )
