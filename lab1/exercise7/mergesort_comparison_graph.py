import numpy as np
import matplotlib.pyplot as plt

LENGTHS = [1000, 2000, 10000]

merge_sort_times = [
    np.mean(
        [0.001136, 0.001101, 0.001210, 0.001036, 0.001176], dtype=np.float32
    ),  # 1000
    np.mean(
        [0.002427, 0.002263, 0.002608, 0.002719, 0.002363], dtype=np.float32
    ),  # 2000
    np.mean(
        [0.014325, 0.014230, 0.014322, 0.014556, 0.013810], dtype=np.float32
    ),  # 10000
]

bottom_up_times = [
    np.mean(
        [0.000692, 0.000680, 0.000647, 0.000661, 0.000655], dtype=np.float32
    ),  # 1000
    np.mean(
        [0.001459, 0.001436, 0.001510, 0.001433, 0.001565], dtype=np.float32
    ),  # 2000
    np.mean(
        [0.009380, 0.009420, 0.009497, 0.009132, 0.009430], dtype=np.float32
    ),  # 10000
]

plt.figure(figsize=(12, 7))

plt.plot(
    LENGTHS,
    merge_sort_times,
    marker="o",
    color="#55A868",
    mfc="#55A868",
    label="Merge Sort",
    linewidth=2,
    markersize=8,
)

plt.plot(
    LENGTHS,
    bottom_up_times,
    marker="o",
    color="#8172B3",
    mfc="#8172B3",
    label="Bottom-Up Merge Sort",
    linewidth=2,
    markersize=8,
)

plt.xlabel("List Size", fontsize=12, fontweight="bold")
plt.ylabel("Time (seconds)", fontsize=12, fontweight="bold")
plt.title(
    "Experiment 7: Merge Sort vs Bottom-Up Merge Sort Comparison",
    fontsize=14,
    fontweight="bold",
)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
