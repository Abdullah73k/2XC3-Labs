import matplotlib.pylab as plt
import numpy as np


def gen_graph(x, y, nodes, M):
    plt.plot(np.array(list(x), dtype=float), np.array(list(y), dtype=float), color="skyblue", marker="o")
    plt.title(
        f"Probability of Cycle vs Number of Edges (n = {nodes}, {M} trials per edge count)"
    )
    plt.xlabel("Num of Edges")
    plt.ylabel("Percentage of Cyclic Graphs")
    plt.show()
