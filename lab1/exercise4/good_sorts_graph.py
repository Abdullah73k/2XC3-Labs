import numpy as np
import matplotlib.pyplot as plt

LENGTHS = [1000, 2000, 10000]

heap_sort_times = [
    np.mean(
        [0.005559, 0.005346, 0.005312, 0.005812, 0.005325], dtype=np.float32
    ),  # 1000
    np.mean(
        [0.012495, 0.012496, 0.012195, 0.012375, 0.012341], dtype=np.float32
    ),  # 2000
    np.mean(
        [0.076727, 0.076727, 0.076582, 0.078123, 0.082828], dtype=np.float32
    ),  # 10000
]

merge_sort_times = [
    np.mean(
        [0.002193, 0.002161, 0.002231, 0.002190, 0.002183], dtype=np.float32
    ),  # 1000
    np.mean(
        [0.004635, 0.004685, 0.005027, 0.004772, 0.004754], dtype=np.float32
    ),  # 2000
    np.mean(
        [0.028090, 0.028690, 0.028285, 0.028515, 0.028217], dtype=np.float32
    ),  # 10000
]

quick_sort_times = [
    np.mean(
        [0.000826, 0.000866, 0.000825, 0.000799, 0.000824], dtype=np.float32
    ),  # 1000
    np.mean(
        [0.002007, 0.001799, 0.001755, 0.001645, 0.001724], dtype=np.float32
    ),  # 2000
    np.mean(
        [0.011393, 0.011036, 0.010638, 0.010632, 0.011394], dtype=np.float32
    ),  # 10000
]

plt.figure(figsize=(12, 7))

plt.plot(
    LENGTHS,
    heap_sort_times,
    marker="o",
    color="#C44E52",
    mfc="#C44E52",
    label="Heap Sort",
)

plt.plot(
    LENGTHS,
    merge_sort_times,
    marker="o",
    color="#55A868",
    mfc="#55A868",
    label="Merge Sort",
)

plt.plot(
    LENGTHS,
    quick_sort_times,
    marker="o",
    color="#4C72B0",
    mfc="#4C72B0",
    label="Quick Sort",
)

plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.title("Experiment 4: Good Sorting Algorithms Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
