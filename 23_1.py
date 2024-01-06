import heapq

def solve():
    def dijkstra(source):
        dist = {}
        q = []
        heapq.heappush(q, (0, source, -1, [source]))

        while q:
            dist_u, u, direction_u, prev = heapq.heappop(q)
            prev_tuple = tuple(prev)
            if (u, direction_u, prev_tuple) in dist:
                continue
            dist[(u, direction_u, prev_tuple)] = abs(dist_u)
            i, j = u
            
            potential_neighbors = enumerate([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

            if m[i][j] == ">":
                potential_neighbors = [(1, (i, j + 1))]
            elif m[i][j] == "<":
                potential_neighbors = [(0, (i, j - 1))]
            elif m[i][j] == "v":
                potential_neighbors = [(3, (i + 1, j))]
            elif m[i][j] == "^":
                potential_neighbors = [(2, (i - 1, j))]

            # check potential neighbors
            for direction_v, v in potential_neighbors:
                if v in prev:
                    continue

                y, x = v
                
                # don't go out of bounds
                if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
                    continue

                if m[y][x] == "#":
                    continue

                alt = abs(dist_u) + 1
                if (v, direction_v, prev_tuple) in dist:
                    continue
                heapq.heappush(q, (-alt, v, direction_v, prev + [v]))
                
        return dist

    filename = "simple.txt"

    m = []
    for line in open(filename):
        line = line.replace("\n", "")
        m.append([c for c in line])

    dist = dijkstra(source=(0, 1))

    ans = 0
    for (u, direction, prev), cost in dist.items():
        if u[0] == len(m) - 1 and u[1] == len(m[0]) - 2:
            ans = max(ans, cost)
    print(ans)

if __name__ == '__main__':
    solve()