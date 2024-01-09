def solve():
    filename = "input.txt"

    plan = []
    for line in open(filename):
        direction, length, color = line.replace("\n", "").split()
        length = int(length)
        color = color.replace("(", "").replace(")", "")
        plan.append((direction, length, color))

    loop = [[0, 0]]
    for direction, length, color in plan:
        y, x = loop[-1]
        for i in range(length):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y -= 1
            elif direction == "D":
                y += 1
            loop.append([y, x])

    min_y = min(v[0] for v in loop)
    min_x = min(v[1] for v in loop)

    if min_y < 0:
        for i in range(len(loop)):
            loop[i][0] += -min_y

    if min_x < 0:
        for i in range(len(loop)):
            loop[i][1] += -min_x

    max_y = max(v[0] for v in loop)
    max_x = max(v[1] for v in loop)

    m = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

    for y, x in loop:
        m[y][x] = 1

    for i in range(len(m)):
        if m[i][0] == 0:
            m[i][0] = 2
        elif m[i][-1] == 0:
            m[i][-1] = 2

    for j in range(len(m[0])):
        if m[0][j] == 0:
            m[0][j] = 2
        elif m[-1][j] == 0:
            m[-1][j] = 2

    while True:
        changed = False
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 2:
                    for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= y < len(m) and 0 <= x < len(m[0]):
                            if m[y][x] == 0:
                                m[y][x] = 2
                                changed = True
        if not changed:
            break

    for v in m:
        print("".join(["#" if vv == 1 else 
                       "." if vv == 2 else "#" for vv in v]))

    print(sum(m[i][j] != 2 
              for i in range(len(m))
              for j in range(len(m[0]))))




if __name__ == '__main__':
    solve()