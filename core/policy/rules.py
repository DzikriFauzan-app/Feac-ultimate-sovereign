from typing import Dict, Callable
class PolicyRule:
    def __init__(self, name: str, description: str, check: Callable[[Dict], bool]):
        self.name = name
        self.description = description
        self.check = check

POLICIES = [
    PolicyRule(
        name="NO_NEGATIVE_PRODUCTION",
        description="Produksi tidak boleh bernilai negatif",
        check=lambda ctx: not (ctx["action"] == "produce" and ctx["payload"].get("qty", 0) < 0)
    ),
    PolicyRule(
        name="MAX_TAX_LIMIT",
        description="Pajak tidak boleh melebihi 90%",
        check=lambda ctx: not (ctx["action"] == "tax" and ctx["payload"].get("rate", 0) > 90)
    ),
]
