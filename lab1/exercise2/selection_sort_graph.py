import numpy as np
import matplotlib.pyplot as plt

LENGTHS = [1000, 2000, 10000]

selection_times = [
    np.mean([0.01035013, 0.01289687, 0.00941704, 0.01297400, 0.01053329], dtype=np.float32),  # 1000
    np.mean([0.03422688, 0.04262558, 0.04181088, 0.04101325, 0.04059329], dtype=np.float32),  # 2000
    np.mean([0.81827712, 0.81903021, 0.84972808, 0.80900621, 0.81981904], dtype=np.float32),  # 10000
]

selection2_times = [
    np.mean([0.01211900, 0.01449263, 0.01175725, 0.01224421, 0.01429833], dtype=np.float32),  # 1000
    np.mean([0.05284750, 0.04828379, 0.05879754, 0.04952975, 0.04889163], dtype=np.float32),  # 2000
    np.mean([1.28550887, 1.27130842, 1.22022971, 1.30069279, 1.21474004], dtype=np.float32),  # 10000
]

plt.plot(
    LENGTHS,
    selection_times,
    marker="o",
    color="#4c72b0",
    mfc="#4c72b0",
    label="Selection Sort",
)

plt.plot(
    LENGTHS,
    selection2_times,
    marker="o",
    color="#c44e52",
    mfc="#c44e52",
    label="Optimized Selection Sort",
)

plt.xlabel("List Length")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.title("Selection Sort VS Optimized Selection Sort")

plt.show()

