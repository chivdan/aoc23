import itertools
from math import prod
from typing import Tuple, List


def solve():
    def invert_range(min_max):
        min_value, max_value = min_max
        if min_value == 1:
            return max_value + 1, 4000
        elif max_value == 4000:
            return 1, min_value - 1

    def intersect(domain1, domain2):
        domain1, domain2 = sorted([domain1, domain2])
        min1, max1 = domain1
        min2, max2 = domain2
        result = max(min1, min2), min(max1, max2)
        if result[0] > result[1]:
            return 0, 0
        else:
            return result

    def intersection(domains: List[Tuple[int, int]]) -> Tuple[int, int]:
        if len(domains) == 1:
            return domains[0]
        result = (1, 4000)
        for domain in domains:
            result = intersect(result, domain)
        return result


    filename = "input.txt"

    min_value = 1
    max_value = 4000
    g = {}
    for line in open(filename):
        line = line.replace("\n", "")
        if line.startswith("{"):
            pass
        elif not line.strip():
            pass
        else:
            name, rest = line.split("{")
            rest = rest.replace("}", "")
            instructions = rest.split(",")
            g[name] = []

            for instruction in instructions:
                if ">" in instruction or "<" in instruction:
                    condition, action = instruction.split(":")
                    if ">" in condition:
                        variable, value = condition.split(">")
                        value = int(value)
                        g[name].append((variable, (value + 1, max_value), action))
                    elif "<" in condition:
                        variable, value = condition.split("<")
                        value = int(value)
                        g[name].append((variable, (min_value, value - 1), action))
                else:
                    action = instruction
                    g[name].append((None, None, action))

    for name in g:
        print(name, g[name])

    t = {}
    for rule in g:
        t[rule] = []
        for variable, condition, action in g[rule]:
            t[rule].append(action)

    with open("graph.gv", "w") as f:
        f.write("digraph tree{")
        for node in t:
            for child in t[node]:
                f.write(f"{node} -> {child};\n")
        f.write("}")

    # find all paths from the root (in) to accept (A)
    paths = []
    def dfs(node: str, path):
        if node == "A":
            if not path in paths:
                paths.append(path)
            return
        if node == "R":
            return
        for i, (variable, min_max, action) in enumerate(g[node]):
            condition = {}
            if variable:
                condition[variable] = min_max
            for j in range(i):
                if g[node][j][0] not in condition: 
                    condition[g[node][j][0]] = invert_range(g[node][j][1])
                else:
                    condition[g[node][j][0]] = intersect(condition[g[node][j][0]], invert_range(g[node][j][1]))
            dfs(action, path + [(condition, action)])

    dfs("in", [(None, "in")])

    for path in paths:
        print(path)

    with open("paths.gv", "w") as f:
        f.write("digraph tree{")
        for path in paths:
            for src, dst in itertools.pairwise(path):
                f.write(f'{src[1]} -> {dst[1]} [label="{str(dst[0])[1:-1]}"];\n')
        f.write("}")

    result = 0
    for path in paths:
        domains = {'x': [(1, 4000)],
                   'm': [(1, 4000)],
                   'a': [(1, 4000)],
                   's': [(1, 4000)]}
        for condition, action in path:
            if not condition:
                continue
            for variable, min_max in condition.items():
                domains[variable].append(min_max)
        
        domains_list = []
        for variable in domains:
            domains_list.append(intersection(domains[variable]))
        
        result += prod(d[1] - d[0] + 1 for d in domains_list)
    print(result)    

if __name__ == '__main__':
    solve()