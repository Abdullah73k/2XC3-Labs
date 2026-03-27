from final_project_part1 import (
    DirectedWeightedGraph,
    dijkstra_approx,
    bellman_ford_approx,
    dijkstra,
    bellman_ford,
    total_dist,
)
import matplotlib.pyplot as plt
from collections import defaultdict
import random


def create_random_graph(n, upper, p):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)

    for i in range(n - 1):
        G.add_edge(i, i + 1, random.randint(1, upper))

    for i in range(n):
        for j in range(n):
            if i != j and not G.are_connected(i, j):
                if random.random() < p:
                    G.add_edge(i, j, random.randint(1, upper))
    return G


N = 60
UPPER = 30
K = [1, 3, 10]
P = [0.2, 0.4, 0.6, 0.8, 1.0]

data = {"dij": defaultdict(dict), "bell": defaultdict(dict)}

print("hello")

for p in P:
    G = create_random_graph(N, UPPER, p)
    source = list(G.adj.keys())[0]

    dij_total_dist = total_dist(dijkstra(G, source))
    bell_total_dist = total_dist(bellman_ford(G, source))

    for k in K:
        dij_approx_dist = total_dist(dijkstra_approx(G, source, k))
        dij_err = (dij_approx_dist - dij_total_dist) / dij_total_dist
        data["dij"][p][k] = dij_err

        bell_approx_dist = total_dist(bellman_ford_approx(G, source, k))
        bell_err = (bell_approx_dist - bell_total_dist) / bell_total_dist
        data["bell"][p][k] = bell_err

    print(f"p={p} done")

plt.figure()

for k in K:
    dij_errs = [data["dij"][p][k] for p in P]
    bell_errs = [data["bell"][p][k] for p in P]
    plt.plot(P, dij_errs, label=f"Dijkstra k={k}")
    plt.plot(P, bell_errs, label=f"Bellman-Ford k={k}")

plt.xlabel("Graph Density (p)")
plt.ylabel("Relative Error (Total Distance)")
plt.title("Approximation Error vs Graph Density For Different K")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()