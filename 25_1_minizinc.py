
import itertools

def solve(input_file: str):
    graph = {}
    edges = []
    nodes = []
    for line in open(input_file):
        src, dsts = line.split(": ")
        dsts = dsts.split()

        if src not in nodes:
            nodes.append(src)

        # create nodes
        if src not in graph:
            graph[src] = []

        for dst in dsts:
            if dst not in nodes:
                nodes.append(dst)
            graph[src].append(dst)
            if (src, dst) not in edges:
                edges.append((src, dst))
            if (dst, src) not in edges:
                edges.append((dst, src))

    index = {node: i for i, node in enumerate(nodes)}
    unique_edges = []
    for u, v in edges:
        if (u, v) not in unique_edges and (v, u) not in unique_edges:
            unique_edges.append((u, v))

    left = [index[u] + 1 for u, v in unique_edges]
    right = [index[v] + 1 for u, v in unique_edges]

    model = f"""
int: N = {len(nodes)};
int: M = {len(unique_edges)};
set of int: dom_V = 1..N;
set of int: dom_E = 1..M;
array[dom_E] of dom_V: left = {left};
array[dom_E] of dom_V: right = {right};
array[dom_V] of var bool: partition;
array[dom_E] of var bool: off;
array[1..3] of var dom_E: disabled;

% edges that are in disabled are off
constraint forall(k in 1..3) (
    off[disabled[k]]
);

% increasing order on disabled for symmetry breaking
constraint forall(k in 1..2) (
    disabled[k] < disabled[k + 1]
);

% definitino of off through disabled
constraint forall(i in dom_E) (
    off[i] <-> (i == disabled[1]) \/ (i == disabled[2]) \/ (i == disabled[3])
);

% definition of partition through off
constraint forall(i in dom_E) (
    not off[i] <-> not (partition[left[i]] xor partition[right[i]])
); 

% count the number of nodes in the first partition
var int: one;
constraint one = sum(i in dom_V) (partition[i]);

solve satisfy;

output [show(one)];
"""
    with open("generated.mzn", "w") as f:
        f.write(model)

    import subprocess
    result = subprocess.check_output(["minizinc", "--solver", "chuffed", "-O3", "generated.mzn"]).decode('ascii')
    result = int(result.split('\r\n')[0])
    print(result * (len(nodes) - result))


if __name__ == '__main__':
    solve("input.txt")
