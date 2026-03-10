import sys
import os
import random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bst import BST
from rbt import RBTree
from graph import plot_graph

LIST_LENGTH = 1000
NUM_TRIALS = 20
SWAP_COUNTS = [0, 1, 2, 3, 4, 5, 10, 25, 50, 100, 250, 500]

def do_swaps(lst, num_swaps):
    arr = lst[:]
    for _ in range(num_swaps):
        i, j = random.randint(0, len(arr) - 1), random.randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

results = []

for swaps in SWAP_COUNTS:
    total_diff = 0
    for _ in range(NUM_TRIALS):
        base = list(range(1, LIST_LENGTH + 1))
        data = do_swaps(base, swaps)

        bst = BST()
        rbt = RBTree()
        for val in data:
            bst.insert(val)
            rbt.insert(val)

        total_diff += bst.height() - rbt.get_height()

    avg_diff = total_diff / NUM_TRIALS
    results.append((swaps, avg_diff))
    print(f"Swaps: {swaps:4d} | Avg height diff (BST - RBT): {avg_diff:.2f}")

plot_graph(results)


