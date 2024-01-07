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

    def bfs(node, edges):
        q = [node]
        visited = set()

        while q:
            node = q.pop()
            if node in visited:
                continue
            visited.add(node)
            for e in edges:
                if e[0] == node:
                    q.append(e[1])

        return len(visited)

    def floyd_warshall(nodes, edges):
        import math
        import numpy as np

        index = {node: nodes.index(node) for node in nodes}
        dist = np.array([[math.inf for u in nodes] for v in nodes])
        prev = np.array([[-1 for u in nodes] for v in nodes])

        for node_u, node_v in edges:
            u, v = index[node_u], index[node_v]
            dist[u][v] = 1
            prev[u][v] = u

        for node_v in nodes:
            v = index[node_v]
            dist[v][v] = 0
            prev[v][v] = v

        for k in range(len(nodes)):
            print(f"{k + 1} / {len(nodes)}")
            for i in range(len(nodes)):
                for j in range(len(nodes)):
                    dist_ikj = dist[i][k] + dist[k][j]
                    if dist[i][j] > dist_ikj:
                        dist[i][j] = dist_ikj
                        prev[i][j] = prev[k][j]

        def get_path(u, v):
            if prev[u][v] == -1:
                return []
            
            path = [nodes[v]]
            while u != v:
                v = prev[u][v]
                path.insert(0, nodes[v])
            return path

        paths = {}
        for u in nodes:
            for v in nodes:
                if u == v:
                    continue
                path = get_path(index[u], index[v])
                if path:
                    paths[(u, v)] = path
        return paths

    for i in range(3):
        paths = floyd_warshall(nodes, edges)

        def get_argmax_shortest_paths_count(paths):
            count = {}

            for (src, dst), path in paths.items():
                for u, v in itertools.pairwise(path):
                    if (u, v) not in count:
                        count[(u, v)] = 1
                    else:
                        count[(u, v)] += 1
            result = max(count.items(), key=lambda item: item[1])
            print(result[0], result[1])
            return result[0]

        u, v = get_argmax_shortest_paths_count(paths)
        print(u, v)
        edges.remove((u, v))
        edges.remove((v, u))

    left_size = bfs(u, edges)
    right_size = len(nodes) - left_size
    print("left, right =", left_size, right_size)
    print("result =", left_size * right_size)

    with open("graph.gv", "w") as f:
        f.write("graph g{\n")
        for src, dst in edges:
            f.write(f"{src} -- {dst}\n")
        f.write("}\n")


if __name__ == '__main__':
    solve("input.txt")
