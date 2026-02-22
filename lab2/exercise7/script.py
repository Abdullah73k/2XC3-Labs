from lab2.graph import create_random_graph, MVC, MIS

def run_mis_experiment():
    print("Starting MIS vs MVC Experiment...\n")
    
    # We will test 5 different graph sizes (from 4 nodes up to 8 nodes)
    for nodes in range(4, 9):
        edges = int(nodes * 1.5) 
        
        G = create_random_graph(nodes, edges)
        
        mvc_result = MVC(G)
        mis_result = MIS(G)
        
        mvc_size = len(mvc_result)
        mis_size = len(mis_result)
        total_sum = mvc_size + mis_size
        
        print(f"--- Graph with {nodes} Nodes and {edges} Edges ---")
        print(f"All Graph Nodes: {list(range(nodes))}")
        print(f"MVC Nodes:       {mvc_result} (Size: {mvc_size})")
        print(f"MIS Nodes:       {mis_result} (Size: {mis_size})")
        print(f"Sum of Sizes:    {mvc_size} + {mis_size} = {total_sum}")
        print("------------------------------------------\n")

if __name__ == "__main__":
    run_mis_experiment()