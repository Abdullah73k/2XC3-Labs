from final_project_part1 import (
    create_random_complete_graph,
    dijkstra_approx,
    bellman_ford_approx,
    dijkstra,
    bellman_ford,
    total_dist,
)
import matplotlib.pyplot as plt
from collections import defaultdict

N = [20, 40, 60, 80, 100, 120]
UPPER = 30
K = [1, 3, 10]

data = {"dij": defaultdict(dict), "bell": defaultdict(dict)}

print("hello")

for n in N:
    G = create_random_complete_graph(n, UPPER)
    source = list(G.adj.keys())[0]

    dij_total_dist = total_dist(dijkstra(G, source))
    bell_total_dist = total_dist(bellman_ford(G, source))

    for k in K:
        dij_approx_dist = total_dist(dijkstra_approx(G, source, k))
        dij_err = (dij_approx_dist - dij_total_dist) / dij_total_dist
        data["dij"][n][k] = dij_err

        bell_approx_dist = total_dist(bellman_ford_approx(G, source, k))
        bell_err = (bell_approx_dist - bell_total_dist) / bell_total_dist
        data["bell"][n][k] = bell_err

    print(f"n={n} done")

plt.figure()

for k in K:
    dij_errs = [data["dij"][n][k] for n in N]
    bell_errs = [data["bell"][n][k] for n in N]
    plt.plot(N, dij_errs, label=f"Dijkstra k={k}")
    plt.plot(N, bell_errs, label=f"Bellman-Ford k={k}")

plt.xlabel("Graph Size (n)")
plt.ylabel("Relative Error (Total Distance)")
plt.title("Approximation Error vs Graph Size For Different K")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
