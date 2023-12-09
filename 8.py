def solve(part1 : bool):
    filename = "input.txt"

    graph = {}
    instructions = ""
    for line in open(filename):
        if not instructions:
            instructions = line[:-1]
            continue
        if len(line) <= 1:
            continue
        src, lr = line[:-1].split(" = ")
        lr = lr.replace("(", "").replace(")", "")
        l, r = lr.split(", ")
        if part1:
            graph[src] = {"L": l, "R": r}
        else:
            graph[src] = [l, r]

    if part1:
        result = 0
        node = "AAA"
        while True:
            for turn in instructions:
                node = graph[node][turn]
                result += 1
                if node == "ZZZ":
                    break
            if node == "ZZZ":
                break
        print(result)
    else:
        result = 0
        nodes = [node for node in graph if node.endswith("A")]
        end_nodes = set(node for node in graph if node.endswith("Z"))
        binary_instructions = instructions.replace("L", "0").replace("R", "1")
        binary_instructions = [int(v) for v in binary_instructions]

        loops = [[] for node in nodes]
        while not all(len(loop) == 2 for loop in loops):
            for turn in binary_instructions:
                nodes = [graph[node][turn] for node in nodes]
                for index, node in enumerate(nodes):
                    if node.endswith("Z") and len(loops[index]) < 2:
                        loops[index].append(result)
                result += 1

        import math
        lengths = [end - start for start, end in loops]
        print(math.lcm(*lengths))

if __name__ == '__main__':
    solve(part1=False)