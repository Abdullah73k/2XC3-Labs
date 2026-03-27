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

N = 20
UPPER = 20
K = 0

data = defaultdict(dict)

for i in range(N):
    K = i
    print(f"K = {K}/{N-2}") 
    G = create_random_complete_graph(N, UPPER)
    dij_total = dijkstra(G, list(G.adj.keys())[0])
    dij_total_dist = total_dist(dij_total)

    dij_approx = dijkstra_approx(G, list(G.adj.keys())[0], K)
    dij_approx_dist = total_dist(dij_approx)

    dij_err = (dij_approx_dist - dij_total_dist) / dij_total_dist

    data["dij"][K] = dij_err

    bell_total = bellman_ford(G, list(G.adj.keys())[0])
    bell_total_dist = total_dist(bell_total)

    bell_approx = bellman_ford_approx(G, list(G.adj.keys())[0], K)
    bell_approx_dist = total_dist(bell_approx)

    bell_err = (bell_approx_dist - bell_total_dist) / bell_approx_dist
    
    data["bell"][K] = bell_err


dij_x = list(data["dij"].keys())
dij_y = list(data["dij"].values())

bell_x = list(data["bell"].keys())
bell_y = list(data["bell"].values())

plt.figure()
plt.plot(dij_x, dij_y)
plt.plot(bell_x, bell_y)
plt.xlabel("Relative Error (Total Distance)")
plt.ylabel("K")
plt.title("Approximation Error vs Relaxation Limit (k)")
plt.grid(True)
plt.tight_layout()
plt.show()
