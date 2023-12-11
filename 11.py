import numpy as np

def solve(part1: bool):
    filename = "input.txt"

    m = []
    for line in open(filename):
        m.append([c for c in line.strip()])
    m = np.array(m)
    rows, columns = len(m), len(m[0])

    # just take the expansion into account when calculating the distances
    if part1:
        expansion = 2
    else: 
        expansion = 1000000

    empty_rows = set(i for i in range(rows) 
                     if all(m[i][j] == '.' for j in range(columns)))
    
    empty_columns = set(j for j in range(columns) 
                        if all(m[i][j] == '.' for i in range(rows)))

    galaxy_positions = get_galaxy_positions(m)
    result = 0.
    for g1 in range(len(galaxy_positions)):
        y1, x1 = galaxy_positions[g1]
        for g2 in range(g1):
            y2, x2 = galaxy_positions[g2]
            result += np.abs(y2 - y1) + np.abs(x2 - x1)
            for row in range(min(y1, y2), max(y1, y2) + 1):
                if row in empty_rows:
                    result += expansion - 1
            for columnn in range(min(x1, x2), max(x1, x2) + 1):
                if columnn in empty_columns:
                    result += expansion - 1
    print(result)

def get_galaxy_positions(expanded):
    galaxy_positions = []
    for i in range(len(expanded)):
        for j in range(len(expanded[i])):
            if expanded[i][j] == "#":
                galaxy_positions.append((i, j))
    return galaxy_positions

if __name__ == '__main__':
    solve(part1=True)