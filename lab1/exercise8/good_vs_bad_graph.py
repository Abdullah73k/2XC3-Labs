import matplotlib.pyplot as plt
import numpy as np

list_lengths = np.array([500, 1000, 2000])

insertion_sorted = np.array([0.00003521, 0.00006503, 0.00016841])
merge_sorted = np.array([0.00065379, 0.00134562, 0.00291468])
quick_sorted = np.array([0.00366028, 0.00928516, 0.02457761])

insertion_moderate = np.array([0.00665685, 0.02741678, 0.10881478])
merge_moderate = np.array([0.00070538, 0.00153588, 0.00392101])
quick_moderate = np.array([0.00036116, 0.00082993, 0.00140062])

insertion_random = np.array([0.00626952, 0.02757090, 0.10983034])
merge_random = np.array([0.00071835, 0.00153833, 0.00339837])
quick_random = np.array([0.00039493, 0.00074608, 0.00173766])

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle(
    'Experiment 8: When "Bad" Sorts Beat "Good" Sorts\n(List Lengths: 500, 1000, 2000)',
    fontsize=14,
    fontweight="bold",
)

ax1.plot(
    list_lengths,
    insertion_sorted,
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=8,
    color="#2E86AB",
    label="Insertion Sort",
)
ax1.plot(
    list_lengths,
    merge_sorted,
    marker="s",
    linestyle="--",
    linewidth=2,
    markersize=8,
    color="#A23B72",
    label="Merge Sort",
)
ax1.plot(
    list_lengths,
    quick_sorted,
    marker="^",
    linestyle="-.",
    linewidth=2,
    markersize=8,
    color="#F18F01",
    label="Quick Sort (Dual-Pivot)",
)
ax1.set_xlabel("List Length", fontweight="bold", fontsize=11)
ax1.set_ylabel("Time (seconds)", fontweight="bold", fontsize=11)
ax1.set_title(
    "Sorted Lists (0 swaps)\nInsertion Sort: O(n) Best Case!",
    fontsize=11,
    fontweight="bold",
)
ax1.legend(loc="upper left", fontsize=9)
ax1.grid(True, alpha=0.3)

ax2.plot(
    list_lengths,
    insertion_moderate,
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=8,
    color="#2E86AB",
    label="Insertion Sort",
)
ax2.plot(
    list_lengths,
    merge_moderate,
    marker="s",
    linestyle="--",
    linewidth=2,
    markersize=8,
    color="#A23B72",
    label="Merge Sort",
)
ax2.plot(
    list_lengths,
    quick_moderate,
    marker="^",
    linestyle="-.",
    linewidth=2,
    markersize=8,
    color="#F18F01",
    label="Quick Sort (Dual-Pivot)",
)
ax2.set_xlabel("List Length", fontweight="bold", fontsize=11)
ax2.set_ylabel("Time (seconds)", fontweight="bold", fontsize=11)
ax2.set_title(
    "Moderately Unsorted\n(~half random swaps)", fontsize=11, fontweight="bold"
)
ax2.legend(loc="upper left", fontsize=9)
ax2.grid(True, alpha=0.3)

ax3.plot(
    list_lengths,
    insertion_random,
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=8,
    color="#2E86AB",
    label="Insertion Sort",
)
ax3.plot(
    list_lengths,
    merge_random,
    marker="s",
    linestyle="--",
    linewidth=2,
    markersize=8,
    color="#A23B72",
    label="Merge Sort",
)
ax3.plot(
    list_lengths,
    quick_random,
    marker="^",
    linestyle="-.",
    linewidth=2,
    markersize=8,
    color="#F18F01",
    label="Quick Sort (Dual-Pivot)",
)
ax3.set_xlabel("List Length", fontweight="bold", fontsize=11)
ax3.set_ylabel("Time (seconds)", fontweight="bold", fontsize=11)
ax3.set_title(
    "Random Lists\n(length*log(length)/2 swaps)", fontsize=11, fontweight="bold"
)
ax3.legend(loc="upper left", fontsize=9)
ax3.grid(True, alpha=0.3)

plt.tight_layout(rect=(0, 0, 1, 0.96))

plt.show()
