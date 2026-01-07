import time
from typing import Dict, Any, List
class RenderABI:
    @staticmethod
    def manifest(pipeline: str, passes: List[str]) -> Dict[str, Any]:
        return {
            "abi_version": "1.0.0",
            "engine": "NeoEngine",
            "mode": "HEADLESS_KERNEL",
            "timestamp": time.time(),
            "pipeline": pipeline,
            "passes": passes,
            "graph_valid": True,
            "visual_output": False
        }
