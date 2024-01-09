def solve_part_1(m):
    # roll the O's
    for i in range(1, len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'O':
                if m[i - 1][j] == '.':
                    # roll the stone to the north while there is space
                    min_i = i
                    while m[min_i - 1][j] == '.' and min_i > 0:
                        min_i -= 1
                    print(f"{min_i}")
                    m[i][j] = '.'
                    m[min_i][j] = 'O'

    # count the objective
    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'O':
                result += len(m) - i
    
    print(result)

import copy
from functools import lru_cache

def solve_part_2(m):
    @lru_cache
    def north(m_current):
        m = [list(v) for v in m_current]
        for i in range(1, len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 'O' and m[i - 1][j] == '.':
                    # roll the stone to the north while there is space
                    min_i = i
                    while min_i > 0 and m[min_i - 1][j] == '.':
                        min_i -= 1
                    m[i][j] = '.'
                    m[min_i][j] = 'O'
        return tuple(tuple(v) for v in m)

    @lru_cache
    def west(m_current):
        m = [list(v) for v in m_current]
        for j in range(1, len(m[0])):
            for i in range(len(m)):            
                if m[i][j] == 'O' and m[i][j - 1] == '.':
                    min_j = j
                    while min_j > 0 and m[i][min_j - 1] == '.':
                        min_j -= 1
                    m[i][j] = '.'
                    m[i][min_j] = 'O'
        return tuple(tuple(v) for v in m)
    
    @lru_cache
    def south(m_current):
        m = [list(v) for v in m_current]
        for i in range(len(m) - 2, -1, -1):
            for j in range(len(m[i])):
                if m[i][j] == 'O' and m[i + 1][j] == '.':
                    max_i = i
                    while max_i < len(m) - 1 and m[max_i + 1][j] == '.':
                        max_i += 1
                    m[i][j] = '.'
                    m[max_i][j] = 'O'
        return tuple(tuple(v) for v in m)
    
    @lru_cache
    def east(m_current):
        m = [list(v) for v in m_current]
        for j in range(len(m[0]) - 2, -1, -1):
            for i in range(len(m)):            
                if m[i][j] == 'O' and m[i][j + 1] == '.':
                    max_j = j
                    while max_j < len(m[0]) - 1 and m[i][max_j + 1] == '.':
                        max_j += 1
                    m[i][j] = '.'
                    m[i][max_j] = 'O'
        return tuple(tuple(v) for v in m)
    
    def count(m):
         # count the objective
        result = 0
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 'O':
                    result += len(m) - i
        return result

    def is_peridodic_from(start, period, counts):
        for i in range(start, start + period):       
            j = i + period    
            if i not in counts or j not in counts:
                return False
            if counts[i] != counts[j]:
                return False
        return True


    # the state is the position of the O's
    # the actions are tilting north, west, south, and east
    m = tuple(tuple(v) for v in m)

    counts = {}
    period = -1
    start_period = None
    target = 1000000000
    for k in range(1, 1000000001):
        m = north(m)
        m = west(m)
        m = south(m)
        m = east(m)
        cnt = count(m)
        counts[k] = cnt
        print(k, cnt)

        for i in range(k - 1, k - 100, -1):
            if i not in counts:
                break
            if counts[k] == counts[i]:
                period = k - i
            if is_peridodic_from(i - 2*period, period, counts):
                print("period", period)
                start_period = k
                break
        if period > 0 and start_period is not None:
            break
    print("found period = ", period, "start = ", start_period)
    print(counts[start_period + (target - start_period) % period])


if __name__ == '__main__':
    filename = "input.txt"
    m = []
    for line in open(filename):
        line = line.replace('\n', '')
        m.append([c for c in line])
    # solve_part_1(m)
    solve_part_2(m)