def is_horizontally_symmetric(pattern, center):
    size = min(center, len(pattern) - center)
    return all(pattern[center + i][j] == pattern[center - 1 - i][j] 
               for j in range(len(pattern[0]))
               for i in range(size))

def is_vertically_symmetric(pattern, center):
    size = min(center, len(pattern[0]) - center)
    return all(pattern[i][center - 1 - j] == pattern[i][center + j]
               for i in range(len(pattern))
               for j in range(size))

# symmetry across horizontal line
def get_symmetry_line(pattern):
    n = len(pattern)
    for i in range(1, n):
        if is_horizontally_symmetric(pattern, i):
            return 100 * i
    return 0

# symmetry across vertical line
def get_symmetry_row(pattern):
    m = len(pattern[0])
    for i in range(1, m):
        if is_vertically_symmetric(pattern, i):
            return i
    return 0

def get_symmetry(pattern) -> int:
    line = get_symmetry_line(pattern)
    row = get_symmetry_row(pattern)
    return line + row

def solve():
    filename = "input.txt"

    result = 0
    pattern = []
    for line in open(filename):
        line = line.replace('\n', '')
        if pattern and not line.strip():
            result += get_symmetry(pattern)
            pattern = []
        else:
            pattern.append([0 if c == "." else 1 for c in line])

    if pattern:
        result += get_symmetry(pattern)
    print(result)

if __name__ == '__main__':
    solve()