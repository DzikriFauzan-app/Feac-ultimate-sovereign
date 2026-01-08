from core.policy.engine import PolicyEngine
from core.policy.risk_policy import RiskPolicy
from agents.BaseAgent import BaseAgent

class FEACBridge:
    @staticmethod
    def emit(agent_name: str, action: str, payload: dict):
        # Sinkronisasi urutan: (world_graph, agent_name, action, payload)
        
        # 1. Evaluasi Hukum Tertulis
        policy = PolicyEngine.evaluate(agent_name, action, payload)
        if not policy["allowed"]:
            return {"blocked": True, "stage": "POLICY"}

        # 2. Evaluasi Risiko Prediktif (Sesuai kesuksesan v1.9.1)
        risk = RiskPolicy.evaluate(BaseAgent._world_graph, agent_name, action, payload)
        if isinstance(risk, dict) and risk.get("blocked"):
            return {"blocked": True, "stage": "RISK_FUSION"}

        # 3. Emit ke Kernel Event
        return BaseAgent.emit_kernel_event(f"FEAC::{agent_name}", action, payload)
