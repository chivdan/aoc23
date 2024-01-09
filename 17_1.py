import heapq

def solve():
    def dijkstra(source):
        dist = {}
        q = []
        heapq.heappush(q, (0, source, -1, 0))

        while q:
            dist_u, u, direction_u, nd_u = heapq.heappop(q)
            
            if (u, direction_u, nd_u) in dist:
                continue
            dist[(u, direction_u, nd_u)] = dist_u
            i, j = u

            # check potential neighbors
            for direction_v, v in enumerate([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]):
                y, x = v
                
                # don't go out of bounds
                if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
                    continue

                if direction_u == 0 and direction_v == 1 or direction_u == 1 and direction_v == 0:
                    continue

                if direction_u == 2 and direction_v == 3 or direction_u == 3 and direction_v == 2:
                    continue

                # line of four in the same direction not allowed
                if direction_v == direction_u:
                    nd = nd_u + 1
                else:
                    nd = 1

                if nd > 3:
                    continue

                alt = dist_u + m[y][x]
                if (v, direction_v, nd) in dist:
                    continue
                heapq.heappush(q, (alt, v, direction_v, nd))
                
        return dist

    filename = "input.txt"

    m = []
    for line in open(filename):
        line = line.replace("\n", "")
        m.append([int(c) for c in line])

    dist = dijkstra(source=(0, 0))

    ans = 1e9
    for (u, direction, nd), cost in dist.items():
        if u[0] == len(m) - 1 and u[1] == len(m[0]) - 1 and nd <= 3:
            ans = min(ans, cost)
    print(ans)

if __name__ == '__main__':
    solve()