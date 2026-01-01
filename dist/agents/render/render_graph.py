#!/usr/bin/env python3
"""
RenderGraph - FULL IMPLEMENTATION (NeoEngine)

Tujuan:
  - Menyediakan sistem node-based (DAG) untuk rendering modern.
  - Setiap node adalah Unit Render: ShaderCompile, MaterialBuild, ToneMap, RenderPipeline, PostProcess, dll.
  - Masing-masing node memiliki ID unik, type, dan config.

Fitur Utama:
  - Registrasi node dinamis
  - Dependency-based execution
  - Cycle detection
  - Graph serialization/deserialization
  - Resource merging antar node
  - Eksekusi full atau partial
  - Kompatibel dengan seluruh modul render NeoEngine

Struktur Node:
  node = {
      "id": "unique-id",
      "type": "PipelineNode",
      "config": {...},
      "inputs": [],
      "outputs": []
  }

Eksekusi:
  - Graph membangun urutan eksekusi dari node-node yang tidak memiliki parent.
  - Setiap node dieksekusi, hasilnya digabung ke resources.
  - Node berikutnya menerima resources yang sudah diperbarui.

"""

import uuid
import json
import time
import traceback
from typing import Dict, List, Any, Callable

# Registry node type -> class
_NODE_REGISTRY: Dict[str, Any] = {}

def register_render_node(node_type: str, cls: Any):
    """Register class node untuk type tertentu."""
    _NODE_REGISTRY[node_type] = cls

def create_node_instance(node_type: str, node_id: str, config: Dict[str, Any]):
    """Buat instance dari type terdaftar."""
    if node_type not in _NODE_REGISTRY:
        raise ValueError(f"RenderGraph: node type not registered: {node_type}")
    return _NODE_REGISTRY[node_type](node_id=node_id, config=config)


# ============================
# Base Render Node
# ============================
class RenderNode:
    """
    Base class untuk semua node di dalam RenderGraph.
    """
    def __init__(self, node_id: str, config: Dict[str, Any]):
        self.id = node_id
        self.config = config or {}
        self.type = self.__class__.__name__

    def run(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        """
        Override di semua implementasi node.
        Wajib return dict (boleh kosong).
        """
        raise NotImplementedError(f"{self.type}.run() not implemented")

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "config": self.config
        }


# ============================
# Built-in Node Implementations
# ============================

# 1) PipelineNode → menjalankan RenderPipeline
from render.render_pipeline import RenderPipeline

class PipelineNode(RenderNode):
    def run(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        name = self.config.get("name", f"pipeline_{self.id}")
        pipeline = RenderPipeline(name=name, config=self.config.get("pipeline", {}))

        # camera dapat berasal dari resources
        camera = resources.get("camera", None)

        out = pipeline.render(camera)
        return {"pipeline_output_" + self.id: out}


# 2) ShaderCompileNode → memanggil shader compiler agent-style
from render.shader import ShaderCompiler

class ShaderCompileNode(RenderNode):
    def run(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        name = self.config.get("name", f"shader_{self.id}")
        src = self.config.get("source", "")
        stage = self.config.get("stage", "fragment")

        compiler = ShaderCompiler()
        compiled = compiler.compile(name=name, source=src, stage=stage)

        return {
            f"shader_{self.id}": compiled,
            f"shader_{self.id}_meta": {
                "source_len": len(src),
                "stage": stage,
                "compiled": True,
                "time": time.time()
            }
        }


# 3) ToneMapNode → menggunakan ToneMappingPass
from render.render_pass.tonemap_pass import ToneMappingPass

class ToneMapNode(RenderNode):
    def run(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        tonemap = ToneMappingPass()
        return tonemap.run(None, resources)


# 4) FinalCompositeNode → membuat frame final
class FinalCompositeNode(RenderNode):
    def run(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        # Ambil hasil tone-map jika ada
        tm = resources.get("tone_mapped_255")
        if tm:
            final = {"final_frame": tm}
        else:
            # fallback: ambil pipeline terakhir
            final = {"final_frame": resources.get("pipeline_output", {})}

        return final


# ============================
# Register built-in nodes
# ============================
register_render_node("PipelineNode", PipelineNode)
register_render_node("ShaderCompileNode", ShaderCompileNode)
register_render_node("ToneMapNode", ToneMapNode)
register_render_node("FinalCompositeNode", FinalCompositeNode)


# ============================
# RenderGraph Core
# ============================

class RenderGraph:
    def __init__(self):
        self.nodes: Dict[str, RenderNode] = {}
        self.edges: Dict[str, List[str]] = {}      # parent -> list(child)
        self.reverse_edges: Dict[str, List[str]] = {}  # child -> parent
        self.metadata = {"created_at": time.time()}

    # --------------------------
    # Node & Edge Management
    # --------------------------
    def add_node(self, node_type: str, config: Dict[str, Any]):
        node_id = self._new_id()
        inst = create_node_instance(node_type, node_id, config)
        self.nodes[node_id] = inst
        self.edges[node_id] = []
        self.reverse_edges[node_id] = []
        return node_id

    def connect(self, parent_id: str, child_id: str):
        """
        parent → child
        """
        if parent_id not in self.nodes or child_id not in self.nodes:
            raise ValueError("Invalid node id in connect()")

        self.edges[parent_id].append(child_id)
        self.reverse_edges[child_id].append(parent_id)

    def _new_id(self):
        return "node-" + uuid.uuid4().hex[:12]

    # --------------------------
    # Cycle Detection
    # --------------------------
    def validate(self):
        visited = {}
        stack = {}

        def dfs(nid):
            visited[nid] = True
            stack[nid] = True
            for nxt in self.edges.get(nid, []):
                if nxt not in visited:
                    if dfs(nxt):
                        return True
                elif stack.get(nxt):
                    return True
            stack[nid] = False
            return False

        for nid in self.nodes:
            if nid not in visited:
                if dfs(nid):
                    raise ValueError("RenderGraph cycle detected")

    # --------------------------
    # Execution Order
    # --------------------------
    def _topological_order(self) -> List[str]:
        indeg = {n: len(self.reverse_edges[n]) for n in self.nodes}
        q = [n for n in self.nodes if indeg[n] == 0]
        out = []

        while q:
            x = q.pop(0)
            out.append(x)
            for nxt in self.edges.get(x, []):
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return out

    # --------------------------
    # Execute Whole Graph
    # --------------------------
    def execute(self, initial_resources: Dict[str, Any] = None) -> Dict[str, Any]:
        self.validate()
        order = self._topological_order()

        resources = initial_resources.copy() if initial_resources else {}
        logs = []
        start_ts = time.time()

        for nid in order:
            node = self.nodes[nid]
            t0 = time.time()
            try:
                out = node.run(resources)
                if out:
                    resources.update(out)
                status = "success"
            except Exception:
                status = "error"
                out = {}
                traceback.print_exc()

            dt = round((time.time() - t0) * 1000, 3)
            logs.append({
                "node": nid,
                "type": node.type,
                "status": status,
                "duration_ms": dt,
                "keys_out": list(out.keys()) if out else []
            })

        return {
            "executed_nodes": order,
            "resources": resources,
            "logs": logs,
            "total_time_ms": round((time.time() - start_ts) * 1000, 3)
        }

    # --------------------------
    # Serialization
    # --------------------------
    def serialize(self) -> Dict[str, Any]:
        return {
            "nodes": [self.nodes[nid].serialize() for nid in self.nodes],
            "edges": {pid: self.edges[pid] for pid in self.edges},
            "metadata": self.metadata
        }

    @classmethod
    def deserialize(cls, data: Dict[str, Any]):
        g = cls()
        g.metadata = data.get("metadata", {})
        node_list = data.get("nodes", [])
        edge_map = data.get("edges", {})

        # rebuild nodes
        for nd in node_list:
            nid = nd["id"]
            ntype = nd["type"]
            cfg = nd.get("config", {})
            inst = create_node_instance(ntype, nid, cfg)
            g.nodes[nid] = inst

        # rebuild edges
        for pid, ch in edge_map.items():
            g.edges[pid] = list(ch)
            for c in ch:
                g.reverse_edges.setdefault(c, []).append(pid)
            g.reverse_edges.setdefault(pid, [])
            g.edges.setdefault(pid, [])

        return g

# END FILE
