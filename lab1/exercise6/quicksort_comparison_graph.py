import numpy as np
import matplotlib.pyplot as plt

LENGTHS = [1000, 2000, 10000]

quick_sort_times = [
    np.mean([0.000470, 0.000428, 0.000415, 0.000403, 0.000416], dtype=np.float32),  # 1000
    np.mean([0.000837, 0.000848, 0.001418, 0.000812, 0.000776], dtype=np.float32),  # 2000
    np.mean([0.005888, 0.005469, 0.005357, 0.005269, 0.005484], dtype=np.float32),  # 10000
]

dual_pivot_times = [
    np.mean([0.000524, 0.000523, 0.000513, 0.000509, 0.000506], dtype=np.float32),  # 1000
    np.mean([0.000936, 0.000997, 0.000913, 0.000884, 0.000975], dtype=np.float32),  # 2000
    np.mean([0.004336, 0.004502, 0.003893, 0.003897, 0.004219], dtype=np.float32),  # 10000
]

plt.figure(figsize=(12, 7))

plt.plot(
    LENGTHS,
    quick_sort_times,
    marker="o",
    color="#4C72B0",
    mfc="#4C72B0",
    label="Quick Sort",
    linewidth=2,
    markersize=8
)

plt.plot(
    LENGTHS,
    dual_pivot_times,
    marker="o",
    color="#DD8452",
    mfc="#DD8452",
    label="Dual Pivot Quick Sort",
    linewidth=2,
    markersize=8
)

plt.xlabel("List Size", fontsize=12, fontweight='bold')
plt.ylabel("Time (seconds)", fontsize=12, fontweight='bold')
plt.title("Experiment 6: Quick Sort vs Dual Pivot Quick Sort Comparison", fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
