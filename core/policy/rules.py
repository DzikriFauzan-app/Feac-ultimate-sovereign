from typing import Dict, Callable
from core.decision.recursive_reasoning import RecursiveReasoning
from agents.BaseAgent import BaseAgent

class PolicyRule:
    def __init__(self, name: str, description: str, check: Callable[[Dict], bool]):
        self.name = name
        self.description = description
        self.check = check

def check_chain_risk(ctx):
    # Gunakan RecursiveReasoning untuk melihat masa depan
    # (Dalam implementasi ini, kita mengevaluasi potensi resiko berdasarkan state saat ini)
    wg = BaseAgent._world_graph
    if not wg: return True # Jika belum ada graph, izinkan
    
    # Mencari apakah aksi serupa pernah berakhir buruk di masa lalu (Multi-Hop)
    # Kita ambil sampel event terakhir yang mirip
    similar = [n for n in wg.nodes if n["data"].get("action") == ctx["action"]]
    for s in similar:
        trace = RecursiveReasoning.trace_effects(wg, s["id"])
        if trace["negative_detected"]:
            return False # BLOKIR: Pernah memicu krisis secara berantai
    return True

POLICIES = [
    PolicyRule(
        name="NO_NEGATIVE_PRODUCTION",
        description="Produksi tidak boleh bernilai negatif",
        check=lambda ctx: not (ctx["action"] == "produce" and ctx["payload"].get("qty", 0) < 0)
    ),
    PolicyRule(
        name="PREVENT_CHAIN_COLLAPSE",
        description="Aksi diblokir karena secara historis memicu krisis berantai",
        check=check_chain_risk
    )
]
