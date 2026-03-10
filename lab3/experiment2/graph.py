import matplotlib.pyplot as plt

def plot_graph(results):
    swaps = [r[0] for r in results]
    diffs = [r[1] for r in results]

    plt.figure()
    plt.plot(swaps, diffs, marker='o')
    plt.xlabel("Number of Swaps")
    plt.ylabel("Avg Height Difference (BST - RBT)")
    plt.title("Number of Swaps vs Avg Height Difference (BST - RBT)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
