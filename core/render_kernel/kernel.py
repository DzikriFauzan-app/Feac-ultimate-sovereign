from typing import Dict, Any, List
from core.render_kernel.abi import RenderABI
class RenderKernel:
    def execute(self, pipeline_name: str, passes: List[str]) -> Dict[str, Any]:
        if not pipeline_name or not passes:
            raise ValueError("Invalid render graph")
        return RenderABI.manifest(pipeline=pipeline_name, passes=passes)
