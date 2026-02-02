import sys
import os

lab1_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if lab1_dir not in sys.path:
    sys.path.insert(0, lab1_dir)

import numpy as np
import matplotlib.pyplot as plt
from graphs.plotting import create_graph

LENGTHS = [1000, 2000, 10000]

LABELS = ["Insertion Sort", "Bubble Sort", "Selection Sort"]

insertion_times = [
    np.mean([0.0222, 0.0204, 0.0210, 0.0195, 0.0215], dtype=np.float32),  # 1000
    np.mean([0.0734, 0.0682, 0.0749, 0.0748, 0.0736], dtype=np.float32),  # 2000
    np.mean([1.6738, 1.6754, 1.6500, 1.6712, 1.7030], dtype=np.float32),  # 10000
]

bubble_times = [
    np.mean([0.0356, 0.0315, 0.0388, 0.0421, 0.0388], dtype=np.float32),  # 1000
    np.mean([0.1276, 0.1342, 0.1260, 0.1281, 0.1340], dtype=np.float32),  # 2000
    np.mean([3.2044, 3.3141, 3.2322, 3.3433, 3.3385], dtype=np.float32),  # 10000
]

selection_times = [
    np.mean([0.0104, 0.0129, 0.0094, 0.0130, 0.0105], dtype=np.float32),  # 1000
    np.mean([0.0342, 0.0426, 0.0418, 0.0410, 0.0406], dtype=np.float32),  # 2000
    np.mean([0.8183, 0.8190, 0.8497, 0.8090, 0.8198], dtype=np.float32),  # 10000
]

# plt.plot(
#     LENGTHS,
#     insertion_times,
#     marker="o",
#     color="#4c72b0",
#     mfc="#4c72b0",
#     label="Insertion Sort",
# )

# plt.plot(
#     LENGTHS,
#     bubble_times,
#     marker="o",
#     color="#c44e52",
#     mfc="#c44e52",
#     label="Bubble Sort",
# )

# plt.plot(
#     LENGTHS,
#     selection_times,
#     marker="o",
#     color="#55a868",
#     mfc="#55a868",
#     label="Selection Sort",
# )
# plt.xlabel("List Size")
# plt.ylabel("Time (seconds)")
# plt.legend()
# plt.grid(True)
# plt.title("Bad Sorting Algorithms Comparison")
# plt.tight_layout()

# plt.show()


create_graph(
    mean_times=[insertion_times, selection_times, bubble_times],
    plot_x=LENGTHS, 
    plot_labels=LABELS,
    x_label="List Size",
    y_label="Time (seconds)",
    title="Bad Sorting Algorithms Comparison",
)
