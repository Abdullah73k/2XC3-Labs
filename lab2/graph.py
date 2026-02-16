from collections import deque


# Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    # def number_of_nodes():
    #     return len()


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


def BFS2(G, node1, node2):
    Q = deque([node1])
    seen = set([node1])
    parents = {}

    while len(Q) != 0:
        curr = Q.popleft()
        if curr == node2:
            path = []
            while curr is not None:
                path.append(curr)
                curr = parents.get(curr)
            path.reverse()
            return path

        for neighbor in G.adj[curr]:
            if neighbor not in seen:
                Q.append(neighbor)
                seen.add(neighbor)
                parents[neighbor] = curr
    return []


def BFS3(G, node1):
    Q = deque([node1])
    seen = set([node1])
    parents = {}

    while len(Q) != 0:
        curr = Q.popleft()
        for neighbor in G.adj[curr]:
            if neighbor not in seen:
                Q.append(neighbor)
                seen.add(neighbor)
                parents[neighbor] = curr
    return parents


# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


def DFS2(G, node1, node2):
    STACK = [node1]
    seen = set([])
    parents = {}

    while len(STACK) != 0:
        curr_node = STACK.pop()
        if curr_node not in seen:
            seen.add(curr_node)

            if curr_node == node2:
                path = []
                while curr_node is not None:
                    path.append(curr_node)
                    curr_node = parents.get(curr_node)
                path.reverse()
                return path

            for neighbor in G.adj[curr_node]:
                if neighbor not in seen and neighbor not in parents:
                    parents[neighbor] = curr_node
                    STACK.append(neighbor)
    return []


# Test DFS2

g = Graph(6)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(2, 4)
g.add_edge(4, 5)

print(DFS2(g, 0, 4))
print(DFS2(g, 0, 5))


def DFS3(G, node1):
    STACK = [node1]
    seen = set([])
    parents = {}

    while len(STACK) != 0:
        curr_node = STACK.pop()
        if curr_node not in seen:
            seen.add(curr_node)
            for neighbor in G.adj[curr_node]:
                if neighbor not in seen and neighbor not in parents:
                    parents[neighbor] = curr_node
                    STACK.append(neighbor)
    return parents


# print(DFS3(g, 0))

# Use the methods below to determine minimum vertex covers


def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy


def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])


def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not (start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover
