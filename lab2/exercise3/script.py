from lab2.graph import create_random_graph, is_cycle
from lab2.exercise3.graph import gen_graph

nodes = 200
edges = [50, 75, 85, 100, 110, 130, 150, 200]


def run_exp_one_script(nodes: int, edges: list[int]):
    M = 1000
    graphs = {}
    percentage_of_cycle = {}
    for edge in edges:
        graphs[edge] = [create_random_graph(nodes, edge) for _ in range(M)]
    for key, val in graphs.items():
        num_of_cycles = 0
        for v in val:
            if is_cycle(v):
                num_of_cycles += 1
        percentage_of_cycle[key] = num_of_cycles / M
    gen_graph(percentage_of_cycle.keys(), percentage_of_cycle.values(), nodes, M)


run_exp_one_script(nodes, edges)
