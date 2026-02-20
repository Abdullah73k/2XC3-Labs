import matplotlib.pylab as plt
import numpy as np

COLORS = ["red", "skyblue", "orange", "green"]


def gen_graph(x, y, nodes, M, exp_two):
    title = (
        f"Probability of Connected Graph vs Number of Edges (n = {nodes}, {M} trials per edge count)"
        if exp_two
        else f"Probability of Cycle vs Number of Edges (n = {nodes}, {M} trials per edge count)"
    )
    x_label = "Num of Edges"
    y_label = f"Percentage of {'Connected' if exp_two else 'Cyclic'} Graphs"

    count = 0
    for run in y:
        x = run.keys()
        y = run.values()
        plt.plot(
            np.array(list(x), dtype=float),
            np.array(list(y), dtype=float),
            color=COLORS[count],
            marker="o",
        )
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        count += 1
    plt.show()
