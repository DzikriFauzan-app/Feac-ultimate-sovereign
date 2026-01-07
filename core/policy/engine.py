from typing import Dict
from core.policy.rules import POLICIES

class PolicyEngine:
    @staticmethod
    def evaluate(agent: str, action: str, payload: Dict) -> Dict:
        context = {"agent": agent, "action": action, "payload": payload}
        violations = []
        for rule in POLICIES:
            try:
                if not rule.check(context):
                    violations.append({"rule": rule.name, "description": rule.description})
            except Exception as e:
                violations.append({"rule": rule.name, "description": str(e)})
        return {"allowed": len(violations) == 0, "violations": violations}
