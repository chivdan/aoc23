from typing import List, Tuple, Self
import itertools

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
        return dx, dy

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return str(self)

class Vector:
    def __init__(self, start: Coordinates, speed: Coordinates) -> None:
        self.start = start
        self.end = start.add(speed)
        dy = self.end.y - self.start.y
        dx = self.end.x - self.start.x
        self.a = dy
        self.b = -dx
        self.c = self.start.y * dx - self.start.x * dy

    def intersection(self, other: Self) -> Coordinates:
        if (self.a * other.b - other.a * self.b) == 0 or self.a == 0:
            return None
        y = (other.a * self.c - self.a * other.c) / (self.a * other.b - other.a * self.b)
        x = (- self.b * y - self.c) / self.a
        result = Coordinates(x, y, 0)

        if self.in_the_future(result) and other.in_the_future(result):
            return result
        return None
    
    def in_the_future(self, other: Coordinates) -> bool:
        return self.start.signs(self.end) == self.start.signs(other)

    def __str__(self) -> str:
        return f"{self.start}, {self.end}"
    
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

    min_x, max_x = 200000000000000, 400000000000000
    min_y, max_y = 200000000000000, 400000000000000

    answer = 0
    for first, second in itertools.combinations(hailstones, 2):
        intersection = first.intersection(second)
        if intersection is None:
            continue
        if min_x <= intersection.x <= max_x and min_y <= intersection.y <= max_y:
            # print(f"{first}, {second}: {intersection}")
            answer += 1
    print(answer)

if __name__ == '__main__':
    solve("input.txt")
