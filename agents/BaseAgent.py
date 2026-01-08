from core.world_graph.graph import WorldGraph

class BaseAgent:
    _world_graph = WorldGraph() # Aktifkan Graph
    
    @staticmethod
    def emit_kernel_event(agent_name, action, payload):
        from core.world_graph.node import WorldNode # Pastikan import lokal
        node = WorldNode(agent_name, action, payload)
        return BaseAgent._world_graph.add_node(node)
