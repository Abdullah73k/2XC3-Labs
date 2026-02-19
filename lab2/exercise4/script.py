from lab2.exercise3.script import run_exp_script

nodes = 200
edges = [50, 100, 200, 300, 400, 450, 500, 550, 600, 650, 700]

if __name__ == "__main__":
    run_exp_script(nodes, edges, exp_two=True)
