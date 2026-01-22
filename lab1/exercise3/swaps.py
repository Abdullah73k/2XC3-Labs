import matplotlib.pyplot as plt
import numpy as np

SWAPS = [100, 1000, 5000]

insertion_times = [
    np.mean(
        [0.023794, 0.022996, 0.022746, 0.023774, 0.023709], dtype=np.float32
    ),  # 100 swaps
    np.mean(
        [0.180505, 0.175589, 0.179727, 0.177383, 0.181712], dtype=np.float32
    ),  # 1000 swaps
    np.mean(
        [0.419498, 0.406930, 0.392201, 0.402154, 0.393964], dtype=np.float32
    ),  # 5000 swaps
]

bubble_times = [
    np.mean(
        [0.603471, 0.582882, 0.577537, 0.577342, 0.587917], dtype=np.float32
    ),  # 100 swaps
    np.mean(
        [0.662767, 0.670733, 0.689759, 0.687630, 0.677450], dtype=np.float32
    ),  # 1000 swaps
    np.mean(
        [0.824656, 0.809577, 0.836648, 0.826860, 0.808699], dtype=np.float32
    ),  # 5000 swaps
]

selection_times = [
    np.mean(
        [0.195600, 0.195881, 0.210763, 0.197751, 0.196845], dtype=np.float32
    ),  # 100 swaps
    np.mean(
        [0.198497, 0.197857, 0.198484, 0.200988, 0.201536], dtype=np.float32
    ),  # 1000 swaps
    np.mean(
        [0.210610, 0.204544, 0.211504, 0.226579, 0.207978], dtype=np.float32
    ),  # 5000 swaps
]


plt.plot(
    SWAPS,
    insertion_times,
    marker="o",
    color="#4c72b0",
    mfc="#4c72b0",
    label="Insertion Sort",
)

plt.plot(
    SWAPS,
    bubble_times,
    marker="o",
    color="#c44e52",
    mfc="#c44e52",
    label="Bubble Sort",
)

plt.plot(
    SWAPS,
    selection_times,
    marker="o",
    color="#55a868",
    mfc="#55a868",
    label="Selection Sort",
)

plt.xlabel("Number Of Swaps")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.title("Bad Sorting Algorithms Swap Comparison")
plt.tight_layout()

plt.show()