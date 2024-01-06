import copy
from typing import List, Tuple
import numpy as np

CNT = 1

class Coordinates:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return str(self)

class Brick:
    def __init__(self, left: Coordinates, right: Coordinates) -> None:
        global CNT
        self.left = left
        self.right = right
        self.id = CNT
        CNT += 1
        self.vertical = self.left.x == self.right.x and self.left.y == self.right.y

    def min_z(self) -> int:
        return min(self.left.z, self.right.z)

    def max_z(self) -> int:
        return max(self.left.z, self.right.z)

    def min_x(self) -> int:
        return min(self.left.x, self.right.x)

    def max_x(self) -> int:
        return max(self.left.x, self.right.x)

    def min_y(self) -> int:
        return min(self.left.y, self.right.y)

    def max_y(self) -> int:
        return max(self.left.y, self.right.y)

    def can_fall(self, m) -> int:
        i = 1
        min_z = self.min_z()
        coordinates = self.coordinates()
        while True: 
            if min_z - i == 0:
                i -= 1
                break
            if (not self.vertical and all(m[x][y][z - i] == 0 for x, y, z in coordinates)) or self.vertical and m[self.min_x()][self.min_y()][self.min_z() - i] == 0:
                i += 1
            else:
                i = i - 1
                break
        if i <= 0:
            return 0
        return i

    def fall(self, m) -> bool:
        i = self.can_fall(m)
        if i == 0:
            return False
        
        for x, y, z in self.coordinates():
            m[x][y][z] = 0
            m[x][y][z - i] = self.id
        
        self.left.z -= i
        self.right.z -= i

        return True
        
    def coordinates(self) -> List[Tuple[int, int, int]]:
        result = []
        for x in range(self.min_x(), self.max_x() + 1):
            for y in range(self.min_y(), self.max_y() + 1):
                for z in range(self.min_z(), self.max_z() + 1):
                    result.append((x, y, z))

        return result

    def __str__(self) -> str:
        return f"{self.id}: {self.left}, {self.right}"
    
    def __repr__(self) -> str:
        return str(self)


def solve(input_file: str):
    bricks = []
    for line in open(input_file):
        left, right = line.split("~")
        left = [int(v) for v in left.split(",")]
        right = [int(v) for v in right.split(",")]
        left = Coordinates(*left)
        right = Coordinates(*right)
        bricks.append(Brick(left, right))

    max_x = max(b.max_x() for b in bricks)
    max_y = max(b.max_y() for b in bricks)
    max_z = max(b.max_z() for b in bricks)

    m = np.zeros((max_x + 1, max_y + 1, max_z + 1), dtype=np.int64)

    for b in bricks:
        for x, y, z in b.coordinates():
            m[x][y][z] = b.id

    def let_fall_and_count(bricks, matrix):
        fallen = set()
        while True:
            some_fell = False
            bricks = sorted(bricks, key=lambda brick: brick.min_z())
            for brick in bricks:
                if brick.fall(matrix):
                    fallen.add(brick.id)
                    some_fell = True
            if not some_fell:
                break
        return len(fallen)

    let_fall_and_count(bricks, m)

    answer = 0
    for brick in bricks:
        # disintegrate brick
        for x, y, z in brick.coordinates():
            m[x][y][z] = 0
        answer += let_fall_and_count(copy.deepcopy(bricks), copy.deepcopy(m))
        # restore brick
        for x, y, z in brick.coordinates():
            m[x][y][z] = brick.id

    print(answer)
        


if __name__ == '__main__':
    solve("input.txt")
