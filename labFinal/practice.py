import min_heap


class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def dijkstras(G: DirectedWeightedGraph, source):
    nodes = list(G.adj.keys())
    dist = {}
    pred = {}
    Q = min_heap.MinHeap([])

    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    while not Q.is_empty():
        curr_element = Q.extract_min()
        curr_node = curr_element.value
        dist[curr_node] = curr_element.key

        for neighbor in G.adj[curr_node]:
            weight = G.w(curr_node, neighbor)
            updated_dist = weight + dist[curr_node]
            if dist[neighbor] > updated_dist:
                Q.decrease_key(neighbor, updated_dist)
                dist[neighbor] = updated_dist
                pred[neighbor] = curr_node

    return dist


def bellman_ford(G: DirectedWeightedGraph, source):
    nodes = list(G.adj.keys())
    dist = {} # node: (node, distance, predecessor), e.g: A: (A, 0, None)
    updated = False

    for node in nodes:
        dist[node] = (node, float("inf"), None)
    dist[source] = (source, 0, None)

    for _ in range(G.number_of_nodes() - 1):
        updated = False
        for node in nodes:
            for neighbor in G.adj[node]:
                weight = G.w(node, neighbor)
                if (new := dist[node][1] + weight) < dist[neighbor][1]:
                    dist[neighbor] = (neighbor, new, node)
                    updated = True
        if not updated:
            break
    return dist