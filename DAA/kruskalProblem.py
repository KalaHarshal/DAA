class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def join(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal(edges, total_nodes):
    edges.sort(key=lambda e: e.weight)
    parent = [i for i in range(total_nodes)]
    rank = [0] * total_nodes
    tree = []

    for edge in edges:
        if find(parent, edge.a) != find(parent, edge.b):
            tree.append(edge)
            join(parent, rank, edge.a, edge.b)

    return tree

edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]

nodes = 4
result = kruskal(edges, nodes)

for edge in result:
    print(edge.a, "-", edge.b, ":", edge.weight)
