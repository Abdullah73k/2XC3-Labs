import numpy as np 
import matplotlib.pyplot as plt
from graphs.plotting import create_graph

LENGTHS = [1000, 2000, 10000]

LABELS = ["Bubble Sort", "Optimized Bubble Sort"]

bubble_times = [
    np.mean([0.03564579, 0.03145479, 0.03876196, 0.04211758, 0.03883829], dtype=np.float32),  # 1000
    np.mean([0.12757250, 0.13424771, 0.12595446, 0.12812325, 0.13402404], dtype=np.float32),  # 2000
    np.mean([3.20444658, 3.31410646, 3.23215658, 3.34334679, 3.33849775], dtype=np.float32),  # 10000
]

bubble2_times = [
    np.mean([0.03566833, 0.03415513, 0.03352146, 0.03563250, 0.03609908], dtype=np.float32),  # 1000
    np.mean([0.12098296, 0.12414008, 0.12143967, 0.11961250, 0.11791621], dtype=np.float32),  # 2000
    np.mean([2.82005596, 2.85008508, 2.82068758, 2.85432804, 2.89490808], dtype=np.float32),  # 10000
]

means = [bubble_times, bubble2_times]

# plt.plot(
#     LENGTHS,
#     bubble_times,
#     marker="o",
#     color="#4c72b0",
#     mfc="#4c72b0",
#     label="Bubble Sort",
# )

# plt.plot(
#     LENGTHS,
#     bubble2_times,
#     marker="o",
#     color="#c44e52",
#     mfc="#c44e52",
#     label="Optimized Bubble Sort",
# )

# plt.xlabel("List Lengths")
# plt.ylabel("Time (seconds)")
# plt.legend()
# plt.grid(True)
# plt.title("Bubble Sort VS Optimized Bubble Sort")

# plt.show()


create_graph(
    mean_times=means,
    plot_x=LENGTHS,
    plot_labels=LABELS,
    x_label="List Lengths",
    y_label="Time (seconds)",
    title="Bubble Sort VS Optimized Bubble Sort"
)