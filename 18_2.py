class Point:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"({self.y}, {self.x})"

    def __repr__(self) -> str:
        return str(self)

def solve():
    filename = "input.txt"

    plan = []
    for line in open(filename):
        _, _, hex = line.replace("\n", "").split()
        hex = hex.replace("(", "").replace(")", "").replace("#", "")
        length = int(hex[:5], 16)
        direction = int(hex[-1])
        if direction == 0:
            direction = "R"
        elif direction == 1:
            direction = "D"
        elif direction == 2:
            direction = "L"
        elif direction == 3:
            direction = "U"
        plan.append((direction, length))

    loop = []
    point = Point(0, 0)
    for direction, length in plan:
        if direction == "R":
            next_point = Point(point.y, point.x + length)
        elif direction == "L":
            next_point = Point(point.y, point.x - length)
        elif direction == "U":
            next_point = Point(point.y - length, point.x)
        elif direction == "D":
            next_point = Point(point.y + length, point.x)
        loop.append(next_point)
        point = next_point

    boundary_length = sum(p[1] for p in plan)

    result = 0
    for i in range(len(loop)):
        result += loop[i].x * loop[(i + 1) % (len(loop))].y - loop[(i + 1) % (len(loop))].x * loop[i].y

    result //= 2
    
    print(result + boundary_length // 2 + 1)


if __name__ == '__main__':
    solve()