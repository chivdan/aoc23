import heapq
import copy

def solve():
    def find_neighbors(node, distance, prev):
        y_prev, x_prev = prev
        if y_prev < 0 or y_prev >= len(m) or x_prev < 0 or x_prev >= len(m[0]):
            return []
        if m[y_prev][x_prev] == "#":
            return []

        i, j = node
        if m[i][j] == "#":
            return []
        potential_neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if node in potential_neighbors:
            potential_neighbors.remove(node)
        if prev in potential_neighbors:
            potential_neighbors.remove(prev)
        while True:
            to_remove = None
            for y, x in potential_neighbors:
                if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
                    to_remove = y, x
                    break
                if m[y][x] == "#":
                    to_remove = y, x
                    break
            if to_remove:
                potential_neighbors.remove(to_remove)
            else: 
                break
        if len(potential_neighbors) == 1:
            # still only one way to go, continue
            return find_neighbors(potential_neighbors[0], distance + 1, node)
        elif len(potential_neighbors) > 1 and distance == 0:
            result = []
            for v in potential_neighbors:
                result.extend(find_neighbors(v, distance + 1, node))
            return list(set(result))
        else:
            return [(node, distance)]
        

    def build_graph(m):
        graph = {}
        for i in range(len(m)):
            for j in range(len(m[i])):
                if (i, j) not in graph:
                    graph[(i, j)] = []
                if m[i][j] == "#":
                    continue
                for neighbor in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    yy, xx = neighbor
                    if yy < 0 or yy >= len(m) or xx < 0 or xx >= len(m[0]):
                        neighbor = i, j
                    graph[(i, j)] = list(set(graph[(i, j)] + find_neighbors((i, j), 0, neighbor)))
                    for node, distance in graph[(i, j)][:]:
                        if node == (i, j) and (node, distance) in graph[(i, j)]:
                            graph[(i, j)].remove((node, distance))
        return graph
        

    def dijkstra(source):
        dist = {}
        previous = {}
        q = []
        heapq.heappush(q, (0, source))
        previous[(0, source)] = [source], hash(tuple([source]))

        max_result = 0
        while q:
            dist_u, u = heapq.heappop(q)
            prev, prev_hash = previous[(dist_u, u)]
            if (u, prev_hash) in dist:
                continue
            dist[(u, prev_hash)] = abs(dist_u)
            i, j = u

            if i == len(m) - 1 and j == len(m[0]) - 2:
                if abs(dist_u) > max_result:
                    max_result = abs(dist_u)
                    print(f"reached goal, skip: {abs(dist_u)}, prev={prev}")
                # continue

            # check potential neighbors
            for v, delta_d in graph[u]:
                if v == u:
                    continue
                if v in prev:
                    continue

                alt = abs(dist_u) + delta_d
                if (v, prev_hash) in dist:
                    continue

                heapq.heappush(q, (-alt, v))
                new_prev = copy.copy(prev)
                new_prev.append(v)
                previous[(-alt, v)] = new_prev, hash(tuple(new_prev))

                
        return dist, previous

    filename = "input.txt"

    m = []
    for line in open(filename):
        line = line.replace("\n", "")
        m.append([c for c in line])

    graph = build_graph(m)
    for v in graph:
        if graph[v]:
            print(v, graph[v])

    dist, previous = dijkstra(source=(0, 1))
    prev = []

    ans = 0
    for (u, _), cost in dist.items():
        if u[0] == len(m) - 1 and u[1] == len(m[0]) - 2:
            ans = max(ans, cost)
            prev = previous[(-cost, u)][0]
            
    print(ans)
    print(prev)

    for i in range(len(m)):
        s = ""
        for j in range(len(m[i])):
            if (i, j) in prev:
                s += "O"
            else:
                s += m[i][j]
        print(s)

if __name__ == '__main__':
    solve()