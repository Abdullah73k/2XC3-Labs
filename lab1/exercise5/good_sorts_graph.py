import numpy as np
import matplotlib.pyplot as plt

SWAPS = [100, 500, 1000, 5000, 9247]

quick_sort_times = [
    np.mean(
        [0.015081, 0.045367, 0.019494, 0.010391, 0.020788], dtype=np.float32
    ),  # 100 swaps
    np.mean(
        [0.004648, 0.004811, 0.004857, 0.009429, 0.004325], dtype=np.float32
    ),  # 500 swaps
    np.mean(
        [0.003164, 0.003347, 0.003780, 0.003420, 0.003215], dtype=np.float32
    ),  # 1000 swaps
    np.mean(
        [0.002357, 0.002924, 0.002632, 0.002462, 0.002546], dtype=np.float32
    ),  # 5000 swaps
    np.mean(
        [0.002349, 0.002308, 0.002747, 0.002241, 0.002515], dtype=np.float32
    ),  # 9247 swaps
]

merge_sort_times = [
    np.mean(
        [0.006343, 0.006264, 0.006287, 0.006324, 0.006073], dtype=np.float32
    ),  # 100 swaps
    np.mean(
        [0.006281, 0.006347, 0.006453, 0.006479, 0.006425], dtype=np.float32
    ),  # 500 swaps
    np.mean(
        [0.006584, 0.006678, 0.006377, 0.006653, 0.006418], dtype=np.float32
    ),  # 1000 swaps
    np.mean(
        [0.006756, 0.006831, 0.006828, 0.006676, 0.006577], dtype=np.float32
    ),  # 5000 swaps
    np.mean(
        [0.006729, 0.006741, 0.006771, 0.006626, 0.006737], dtype=np.float32
    ),  # 9247 swaps
]

heap_sort_times = [
    np.mean(
        [0.018877, 0.018544, 0.018624, 0.018998, 0.018828], dtype=np.float32
    ),  # 100 swaps
    np.mean(
        [0.018482, 0.018630, 0.018549, 0.018726, 0.018426], dtype=np.float32
    ),  # 500 swaps
    np.mean(
        [0.018761, 0.018734, 0.018642, 0.018207, 0.018756], dtype=np.float32
    ),  # 1000 swaps
    np.mean(
        [0.017881, 0.018436, 0.017910, 0.018035, 0.018096], dtype=np.float32
    ),  # 5000 swaps
    np.mean(
        [0.018239, 0.017812, 0.017811, 0.017892, 0.018115], dtype=np.float32
    ),  # 9247 swaps
]

plt.figure(figsize=(12, 7))

plt.plot(
    SWAPS,
    quick_sort_times,
    marker="o",
    color="#4C72B0",
    mfc="#4C72B0",
    label="Quick Sort",
    linewidth=2,
    markersize=8,
)

plt.plot(
    SWAPS,
    merge_sort_times,
    marker="o",
    color="#55A868",
    mfc="#55A868",
    label="Merge Sort",
    linewidth=2,
    markersize=8,
)

plt.plot(
    SWAPS,
    heap_sort_times,
    marker="o",
    color="#C44E52",
    mfc="#C44E52",
    label="Heap Sort",
    linewidth=2,
    markersize=8,
)

plt.xlabel("Number of Swaps", fontsize=12, fontweight="bold")
plt.ylabel("Time (seconds)", fontsize=12, fontweight="bold")
plt.title(
    "Experiment 5: Good Sorting Algorithms on Near-Sorted Lists\n(Number of Swaps vs Time - List Length: 5000)",
    fontsize=14,
    fontweight="bold",
)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
