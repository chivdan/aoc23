import heapq

def solve(input: str):
    m = []
    s_i, s_j = None, None
    for line in open(input):
        line = line.replace("\n", "")
        m.append([c for c in line])
        if "S" in line:
            s_i = len(m) - 1
            s_j = m[-1].index("S")

    visited = set()
    Q = [(0, s_i, s_j)]
    heapq.heapify(Q)

    while Q:
        num, i, j = heapq.heappop(Q)
        if num == 64:
            visited.add((i, j))
            continue
        for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
                continue
            if m[y][x] == "#":
                continue
            if (num + 1, y, x) in Q:
                continue
            heapq.heappush(Q, (num + 1, y, x))
        
    print(len(visited))

if __name__ == '__main__':
    solve("input.txt")