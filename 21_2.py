import numpy as np 

def solve(input: str):
    m = []
    s_i, s_j = None, None
    for line in open(input):
        line = line.replace("\n", "")
        m.append([c for c in line])
        if "S" in line:
            s_i = len(m) - 1
            s_j = m[-1].index("S")
    m[s_i][s_j] = "."

    def bfs(start_i, start_j, remaining_steps):
        q = set()
        q.add((start_i, start_j))

        for t in range(remaining_steps):
            next = set()
            for i, j in q:
                for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if m[y % len(m)][x % len(m[0])] == ".":
                        next.add((y, x))
            q = next
        return len(q)
    
    n = len(m)
    s, d = divmod(26501365, n)

    ans = []
    for i in range(3):
        steps = d + n * i
        ans.append(bfs(s_i, s_j, steps))
        print(steps, ans[-1])

    quadratic_coef = np.polyfit(np.arange(3), ans, 2)
    print(quadratic_coef)
    print(int(round(s**2 * quadratic_coef[0])) + s * quadratic_coef[1] + quadratic_coef[2])

if __name__ == '__main__':
    solve("input.txt")