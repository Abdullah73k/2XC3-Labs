from typing import Protocol
import matplotlib.pyplot as plt


class CreateGraphObject(Protocol): ...


def create_graph(
    mean_times: list,
    plot_x: list,
    plot_labels: list[str],
    x_label: str,
    y_label: str,
    title: str,
):
    COLORS = [
        "#4C72B0",  # blue
        "#DD8452",  # orange
        "#55A868",  # green
        "#C44E52",  # red
        "#8172B3",  # purple
        "#937860",  # brown
        "#DA8BC3",  # pink
        "#8C8C8C",  # gray
        "#64B5CD",  # cyan
        "#E24A33",  # dark orange
    ]

    for i in range(len(mean_times)):
        plt.plot(
            plot_x,
            mean_times[i],
            marker="o",
            color=COLORS[i],
            mfc=COLORS[i],
            label=plot_labels[i],
        )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.title(title)
    plt.tight_layout()

    plt.show()
