from typing import Self

class Coordinates:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def add(self, other: Self) -> Self:
        return Coordinates(self.x + other.x, self.y + other.y, self.z + other.z)

    def signs(self, other: Self) -> int:
        dx = 1 if other.x - self.x > 0 else -1
        dy = 1 if other.y - self.y > 0 else -1
        dz = 1 if other.z - self.z > 0 else -1
        return dx, dy, dz

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return str(self)

class Vector:
    def __init__(self, start: Coordinates, speed: Coordinates) -> None:
        self.start = start
        self.speed = speed

    def __str__(self) -> str:
        return f"{self.start}, {self.speed}"
    
    def __repr__(self) -> str:
        return str(self)


def solve(input_file: str):
    hailstones = []
    for line in open(input_file):
        left, speed = line.split("@")
        left = [int(v) for v in left.split(",")]
        speed = [int(v) for v in speed.split(",")]
        left = Coordinates(*left)
        speed = Coordinates(*speed)
        hailstones.append(Vector(left, speed))

    import sympy
    x, y, z, vx, vy, vz = sympy.symbols("x y z vx vy vz", real=True)
    t = sympy.symbols(" ".join([f"t_{i}" for i in range(5)]), real=True)

    eqs = []
    for i in range(5):
        eqs.append(sympy.Eq(x - t[i] * hailstones[i].speed.x + t[i] * vx,  hailstones[i].start.x))
        eqs.append(sympy.Eq(y - t[i] * hailstones[i].speed.y + t[i] * vy,  hailstones[i].start.y))
        eqs.append(sympy.Eq(z - t[i] * hailstones[i].speed.z + t[i] * vz,  hailstones[i].start.z))

    sol = sympy.solve(eqs)[0]
    answer = sol[x] + sol[y] + sol[z]
    print(answer)



if __name__ == '__main__':
    solve("input.txt")
