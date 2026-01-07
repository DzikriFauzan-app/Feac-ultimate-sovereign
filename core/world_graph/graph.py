class WorldGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)
        return node.id

    def add_edge(self, edge):
        self.edges.append(edge.serialize())
        return edge.id

    def snapshot(self):
        return {
            "nodes": [
                n.serialize() if hasattr(n, "serialize") else n
                for n in self.nodes
            ],
            "edges": list(self.edges)
        }
def get_node(self, node_id: str):
    for n in self.nodes:
        if isinstance(n, dict):
            if n.get("id") == node_id: return n
        else:
            if getattr(n, "id", None) == node_id: return n.serialize()
    return None
