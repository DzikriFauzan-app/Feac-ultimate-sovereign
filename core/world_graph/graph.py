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
