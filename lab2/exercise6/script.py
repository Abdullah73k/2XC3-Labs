import matplotlib.pyplot as plt
from lab2.graph import create_random_graph, approx1, approx2, approx3, MVC


def experiment_fixed_nodes():

    n = 8
    trials = 500
    edge_values = [1, 5, 10, 15, 20, 25, 28]

    a1_ratios, a2_ratios, a3_ratios = [], [], []

    for m in edge_values:

        mvc_sum = a1_sum = a2_sum = a3_sum = 0

        for _ in range(trials):
            G = create_random_graph(n, m)

            mvc_size = len(MVC(G))
            mvc_sum += mvc_size

            a1_sum += len(approx1(G))
            a2_sum += len(approx2(G))
            a3_sum += len(approx3(G))

        a1_ratios.append(a1_sum / mvc_sum)
        a2_ratios.append(a2_sum / mvc_sum)
        a3_ratios.append(a3_sum / mvc_sum)

    plt.figure()
    plt.plot(edge_values, a1_ratios, label="Approx1 (Greedy Degree)")
    plt.plot(edge_values, a2_ratios, label="Approx2 (Random Vertex)")
    plt.plot(edge_values, a3_ratios, label="Approx3 (Random Edge)")
    plt.xlabel("Number of Edges (n = 8)")
    plt.ylabel("Average Approximation Ratio")
    plt.title("Average Approximation Performance vs Number of Edges")
    plt.legend()
    plt.grid()
    plt.show()


def experiment_fixed_edges():

    m = 10
    trials = 500
    node_values = [5, 6, 7, 8, 9]

    a1_ratios, a2_ratios, a3_ratios = [], [], []

    for n in node_values:

        mvc_sum = a1_sum = a2_sum = a3_sum = 0

        for _ in range(trials):
            G = create_random_graph(n, m)

            mvc_size = len(MVC(G))
            mvc_sum += mvc_size

            a1_sum += len(approx1(G))
            a2_sum += len(approx2(G))
            a3_sum += len(approx3(G))

        a1_ratios.append(a1_sum / mvc_sum)
        a2_ratios.append(a2_sum / mvc_sum)
        a3_ratios.append(a3_sum / mvc_sum)

    plt.figure()
    plt.plot(node_values, a1_ratios, label="Approx1 (Greedy Degree)")
    plt.plot(node_values, a2_ratios, label="Approx2 (Random Vertex)")
    plt.plot(node_values, a3_ratios, label="Approx3 (Random Edge)")
    plt.xlabel("Number of Nodes (m = 10)")
    plt.ylabel("Average Approximation Ratio")
    plt.title("Average Approximation Performance vs Number of Nodes")
    plt.legend()
    plt.grid()
    plt.show()


def experiment_worst_case():

    n = 5
    trials = 500
    edge_values = [1, 3, 5, 7, 10]

    worst_a1 = []
    worst_a2 = []
    worst_a3 = []

    for m in edge_values:

        max_a1 = max_a2 = max_a3 = 0

        for _ in range(trials):
            G = create_random_graph(n, m)

            mvc_size = len(MVC(G))

            r1 = len(approx1(G)) / mvc_size
            r2 = len(approx2(G)) / mvc_size
            r3 = len(approx3(G)) / mvc_size

            max_a1 = max(max_a1, r1)
            max_a2 = max(max_a2, r2)
            max_a3 = max(max_a3, r3)

        worst_a1.append(max_a1)
        worst_a2.append(max_a2)
        worst_a3.append(max_a3)

    plt.figure()
    plt.plot(edge_values, worst_a1, label="Approx1 (Worst Case)")
    plt.plot(edge_values, worst_a2, label="Approx2 (Worst Case)")
    plt.plot(edge_values, worst_a3, label="Approx3 (Worst Case)")
    plt.xlabel("Number of Edges (n = 5)")
    plt.ylabel("Worst Observed Approximation Ratio")
    plt.title("Worst Case Approximation Performance")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    experiment_fixed_nodes()
    experiment_fixed_edges()
    experiment_worst_case()