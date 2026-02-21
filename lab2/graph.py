from collections import deque
import random


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



def is_cycle(G):
    seen = set()

    for node in G.adj.keys():
        S = []
        if node not in seen:
            S.append((node, None))
        while S:
            curr, parent = S.pop()
            if curr in seen:
                continue
            seen.add(curr)

            for neighbor in G.adj[curr]:
                if neighbor not in seen:
                    S.append((neighbor, curr))
                elif parent != neighbor:
                    return True
    return False


def is_cycle_recur(G):
    seen = set()

    def helper(curr, parent):
        seen.add(curr)

        for neighbor in G.adj[curr]:
            if neighbor not in seen:
                if helper(neighbor, curr):
                    return True
            elif neighbor != parent:
                return True

    for node in G.adj.keys():
        if node not in seen:
            if helper(node, None):
                return True
    return False


def is_connected(G):
    l = list(G.adj.keys())
    queue = deque([l[0]])
    seen = set([l[0]])

    while queue:
        curr = queue.popleft()

        for neighbor in G.adj[curr]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    for node in G.adj.keys():
        if node not in seen:
            return False
    return True



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


## randomly generate graphs

def create_random_graph(i, j):
    if j > i * (i - 1) // 2:
        raise ValueError("Too many edges for a simple graph without duplicates.")

    G = Graph(i)
    edges = set()

    while len(edges) < j:
        u = random.randint(0, i - 1)
        v = random.randint(0, i - 1)

        if u != v:
            edge = tuple(sorted((u, v)))

            if edge not in edges:
                edges.add(edge)
                G.add_edge(u, v)

    return G

# Approximation algorithms for vertex cover

def approx1(G):
    C = []
    
    local_adj = {}
    for node in G.adj:
        local_adj[node] = list(G.adj[node]) 
        
    while not is_vertex_cover(G, C):
        max_degree = -1
        v = None
        for node in local_adj:
            degree = len(local_adj[node])
            if degree > max_degree:
                max_degree = degree
                v = node
                
        if v not in C:
            C.append(v)
            
        for neighbor in local_adj[v]:
            if v in local_adj[neighbor]:
                local_adj[neighbor].remove(v)
        local_adj[v] = []
        
    return C

def approx2(G):
    adj = {u: set(vs) for u, vs in G.adj.items()}
    
    C = set()
    vertices = list(adj.keys())

    while True:
        edges_left = any(len(adj[u]) > 0 for u in adj)
        if not edges_left:
            return C

        remaining = [v for v in vertices if v not in C]
        v = random.choice(remaining)

        C.add(v)
        
        
def approx3(G):
    adj = {u: set(vs) for u, vs in G.adj.items()}
    
    C = set()

    while True:
        edges = []
        for u in adj:
            for v in adj[u]:
                if u < v:   
                    edges.append((u, v))

        if not edges:
            return C

        u, v = random.choice(edges)

        C.add(u)
        C.add(v)

        for neighbor in list(adj[u]):
            adj[neighbor].remove(u)
        adj[u].clear()

        for neighbor in list(adj[v]):
            adj[neighbor].remove(v)
        adj[v].clear()


if __name__ == "__main__":

    g = Graph(6)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 4)
    g.add_edge(4, 5)

    print(DFS2(g, 0, 4))
    print(DFS2(g, 0, 5))
    
    print(is_connected(g))
    
    print(is_cycle(g))
    print(is_cycle_recur(g))
