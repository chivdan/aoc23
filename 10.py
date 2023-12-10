import itertools


def solve(part1: bool):
    def get_neighbors(c_i, c_j, prev_i, prev_j):
        result = []
        # N
        if c_i - 1 >= 0 and c_i - 1 != prev_i and m[c_i - 1][c_j] in possible_connections[m[c_i][c_j]]['N']:
            result.append([c_i - 1, c_j])
        # S
        if c_i + 1 < len(m) and c_i + 1 != prev_i and m[c_i + 1][c_j] in possible_connections[m[c_i][c_j]]['S']:
            result.append([c_i + 1, c_j])
        # W
        if c_j - 1 >= 0 and c_j - 1 != prev_j and m[c_i][c_j - 1] in possible_connections[m[c_i][c_j]]['W']:
            result.append([c_i, c_j - 1])
        # E
        if c_j + 1 < len(m[c_i]) and c_j + 1 != prev_j and m[c_i][c_j + 1] in possible_connections[m[c_i][c_j]]['E']:
            result.append([c_i, c_j + 1])
        return result

    filename = "input.txt"

    m = []
    for line in open(filename):
        m.append([c for c in line.strip()])

    possible_connections = {'|': {'N' : ['|', '7', 'F', 'S'],
                                'S': ['|', 'L', 'J', 'S'],
                                'W': [],
                                'E': []},
                            '-': {'W': ['-', 'L', 'F', 'S'],
                                'E': ['-', 'J', '7', 'S'],
                                'N': [],
                                'S': []},
                            'L': {'N': ['|', '7', 'F', 'S'],
                                'E': ['-', '7', 'J', 'S'],
                                'W': [],
                                'S': []},
                            '7': {'S': ['|', 'L', 'J', 'S'],
                                'W': ['-', 'L', 'F', 'S'],
                                'N': [],
                                'E': []},
                            'J': {'N': ['|', '7', 'F', 'S'],
                                'W': ['-', 'L', 'F', 'S'],
                                'S': [],
                                'E': []},
                            'F': {'E': ['-', '7', 'J', 'S'],
                                'S': ['|', 'L', 'J', 'S'],
                                'W': [],
                                'N': []},
                            'S': {'E': ['|', '-', 'L', 'J', '7', 'F'],
                                  'W': ['|', '-', 'L', 'J', '7', 'F'],
                                  'N': ['|', '-', 'L', 'J', '7', 'F'],
                                  'S': ['|', '-', 'L', 'J', '7', 'F']}}
    
    i_S, j_S = -1, -1
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'S':
                i_S, j_S = i, j
                break

    visited = [[False for j in range(len(m[i]))] for i in range(len(m))]

    loop_length = 0
    prev_i, prev_j = -1, -1
    c_i, c_j = i_S, j_S
    loop_coordinates = [(i_S, j_S)]
    while True:
        if loop_length > 0 and m[c_i][c_j] == 'S':
            break
        neighbors = get_neighbors(c_i, c_j, prev_i, prev_j)

        if not neighbors:
            prev_i, prev_j = -1, -1
            c_i, c_j = i_S, j_S
            loop_length = 0
            loop_coordinates = [(i_S, j_S)]
            continue

        for i, j in neighbors:
            if visited[i][j]:
                continue
            visited[i][j] = True
            loop_coordinates.append((i, j))

            loop_length += 1
            prev_i, prev_j = c_i, c_j
            c_i, c_j = i, j
            break

    def simple_neighbors(c_i, c_j):
        result = []
        # N
        if c_i - 1 >= 0 and (c_i - 1, c_j) not in loop_set:
            result.append((c_i - 1, c_j))
        # S
        if c_i + 1 < len(m) and (c_i + 1, c_j) not in loop_set:
            result.append((c_i + 1, c_j))
        # W
        if c_j - 1 >= 0 and (c_i, c_j - 1) not in loop_set:
            result.append((c_i, c_j - 1))
        # E
        if c_j + 1 < len(m[c_i]) and (c_i, c_j + 1) not in loop_set:
            result.append((c_i, c_j + 1))
        return result

    def expand(y, x):
        points = {(y, x)}
        s = {(y, x)}
        while s:
            i, j = s.pop()
            for point in simple_neighbors(i, j):
                if point not in points:
                    s.add(point)
                    points.add(point)
        return points
    
    loop_coordinates.append((i_S, j_S))

    loop_set = set(loop_coordinates)

    if part1:
        print(int((loop_length) / 2))
    else:
        potential_enclosed = []
        for (i1, j1), (i2, j2) in itertools.pairwise((loop_coordinates)):
            # going north
            if i2 < i1 and j1 == j2:
                if j2 + 1 < len(m[i2]) and (i2, j2 + 1) not in loop_coordinates:
                    potential_enclosed.append((i2, j2 + 1))
                if j1 + 1 < len(m[i1]) and (i1, j1 + 1) not in loop_coordinates:
                    potential_enclosed.append((i1, j1 + 1))
            # going east
            elif i2 == i1 and j2 > j1:
                if i2  + 1 < len(m) and (i2 + 1, j2) not in loop_coordinates:
                    potential_enclosed.append((i2 + 1, j2))
                if i1  + 1 < len(m) and (i1 + 1, j1) not in loop_coordinates:
                    potential_enclosed.append((i1 + 1, j1))
            # going south
            elif i2 > i1 and j2 == j1:
                if j2 > 0 and (i2, j2 - 1) not in loop_coordinates:
                    potential_enclosed.append((i2, j2 - 1))
                if j1 > 0 and (i1, j1 - 1) not in loop_coordinates:
                    potential_enclosed.append((i1, j1 - 1))
            # going west
            elif i2 == i1 and j2 < j1:
                if i2 > 0 and (i2 - 1, j2) not in loop_coordinates:
                    potential_enclosed.append((i2 - 1, j2))
                if i1 > 0 and (i1 - 1, j1) not in loop_coordinates:
                    potential_enclosed.append((i1 - 1, j1))

        potential_enclosed = list(set(potential_enclosed))
        enclosed = set()
        for i, j in potential_enclosed:
            enclosed |= expand(i, j)
        print(enclosed)
        print(len(enclosed))


if __name__ == '__main__':
    solve(part1=False)