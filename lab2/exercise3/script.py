from lab2.graph import create_random_graph, is_cycle, is_connected
from lab2.exercise3.graph import gen_graph

nodes = 200
edges = [50, 75, 85, 100, 110, 130, 150, 200]


def run_exp_script(nodes: int, edges: list[int], exp_two=False):
    M = 1000
    graphs = {}
    percentage = {}
    exp_func = is_connected if exp_two else is_cycle
    
    for edge in edges:
        graphs[edge] = [create_random_graph(nodes, edge) for _ in range(M)]
    for key, val in graphs.items():
        num_of_cycles = 0
        for v in val:
            if exp_func(v):
                num_of_cycles += 1
        percentage[key] = num_of_cycles / M
    print(percentage)
    gen_graph(percentage.keys(), percentage.values(), nodes, M, exp_two)


if __name__ == "__main__":
    run_exp_script(nodes, edges)
