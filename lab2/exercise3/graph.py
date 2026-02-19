import matplotlib.pylab as plt
import numpy as np


def gen_graph(x, y, nodes, M, exp_two):
    title = (
        f"Probability of Connected Graph vs Number of Edges (n = {nodes}, {M} trials per edge count)"
        if exp_two
        else f"Probability of Cycle vs Number of Edges (n = {nodes}, {M} trials per edge count)"
    )
    x_label = "Num of Edges"
    y_label = f"Percentage of {'Connected' if exp_two else 'Cyclic'} Graphs"

    plt.plot(
        np.array(list(x), dtype=float),
        np.array(list(y), dtype=float),
        color="skyblue",
        marker="o",
    )
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
