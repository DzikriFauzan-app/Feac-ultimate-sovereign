from typing import List, Set
from core.world_graph.query import WorldGraphQuery

NEGATIVE_ACTIONS = {"fail", "error", "crisis", "collapse"}

class RecursiveReasoning:
    @staticmethod
    def trace_effects(graph, start_event_id: str, max_depth: int = 5) -> dict:
        visited: Set[str] = set()
        negative_paths: List[List[str]] = []

        def dfs(current_id: str, path: List[str], depth: int):
            if depth > max_depth or current_id in visited: return
            visited.add(current_id)
            
            effects = WorldGraphQuery.get_effects(graph, current_id)
            for eff_id in effects:
                new_path = path + [eff_id]
                node = graph.get_node(eff_id)
                if not node: continue
                
                action = node["data"].get("action", "").lower()
                if action in NEGATIVE_ACTIONS:
                    negative_paths.append(new_path)
                else:
                    dfs(eff_id, new_path, depth + 1)

        dfs(start_event_id, [start_event_id], 0)
        return {
            "root_event": start_event_id,
            "negative_detected": len(negative_paths) > 0,
            "paths": negative_paths
        }
