class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight

def prim(edges, total_nodes):
    connected = set()
    connected.add(0)
    tree = []

    while len(connected) < total_nodes:
        possible_edges = [e for e in edges if (e.a in connected and e.b not in connected) or (e.b in connected and e.a not in connected)]
        if not possible_edges:
            break
        min_edge = min(possible_edges, key=lambda e: e.weight)
        tree.append(min_edge)
        connected.add(min_edge.a)
        connected.add(min_edge.b)

    return tree

edges = [
    Edge(0, 1, 4),
    Edge(0, 2, 3),
    Edge(1, 2, 1),
    Edge(1, 3, 2),
    Edge(2, 3, 4)
]

nodes = 4
result = prim(edges, nodes)

for edge in result:
    print(edge.a, "-", edge.b, ":", edge.weight)
