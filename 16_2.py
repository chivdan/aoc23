

def solve(part1: bool):
    def out_of_bounds(the_yy, the_xx) -> bool:
        return the_xx < 0 or the_xx >= len(m[0]) or the_yy < 0 or the_yy >= len(m)

    def bfs(yy, xx, initial_direction):
        visited = [[False for i in range(len(m[0]))] for v in m]
        explored = dict()
        explored[(yy, xx, initial_direction)] = True
        q = [(yy, xx, initial_direction)]

        while q:
            y, x, direction = q.pop(0)

            if not (y == yy and x == xx and direction == initial_direction) and out_of_bounds(y, x):
                print(yy, xx, "out")
                continue
            
            if direction == 'r':
                y_next = y
                x_next = x + 1

                if out_of_bounds(y_next, x_next):
                    continue
                elif m[y_next][x_next] in '.-':
                    if (y_next, x_next, direction) not in explored:
                        q.append((y_next, x_next, direction))
                        explored[(y_next, x_next, direction)] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '|':
                    if (y_next, x_next, 'u') not in explored:
                        q.append((y_next, x_next, 'u'))
                        explored[(y_next, x_next, 'u')] = True
                        visited[y_next][x_next] = True
                    if (y_next, x_next, 'd') not in explored:
                        q.append((y_next, x_next, 'd'))
                        explored[(y_next, x_next, 'd')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '/':
                    if (y_next, x_next, 'u') not in explored:
                        q.append((y_next, x_next, 'u'))
                        explored[(y_next, x_next, 'u')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '\\':
                    if (y_next, x_next, 'd') not in explored:
                        q.append((y_next, x_next, 'd'))
                        explored[(y_next, x_next, 'd')] = True
                        visited[y_next][x_next] = True
            elif direction == 'l':
                y_next = y
                x_next = x - 1

                if out_of_bounds(y_next, x_next):
                    continue
                elif m[y_next][x_next] in '.-':
                    if (y_next, x_next, direction) not in explored:
                        q.append((y_next, x_next, direction))
                        explored[(y_next, x_next, direction)] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '|':
                    if (y_next, x_next, 'u') not in explored:
                        q.append((y_next, x_next, 'u'))
                        explored[(y_next, x_next, 'u')] = True
                        visited[y_next][x_next] = True
                    if (y_next, x_next, 'd') not in explored:
                        q.append((y_next, x_next, 'd'))
                        explored[(y_next, x_next, 'd')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '/':
                    if (y_next, x_next, 'd') not in explored:
                        q.append((y_next, x_next, 'd'))
                        explored[(y_next, x_next, 'd')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '\\':
                    if (y_next, x_next, 'u') not in explored:
                        q.append((y_next, x_next, 'u'))
                        explored[(y_next, x_next, 'u')] = True
                        visited[y_next][x_next] = True

            elif direction == 'u':
                y_next = y - 1
                x_next = x

                if out_of_bounds(y_next, x_next):
                    continue
                elif m[y_next][x_next] in '.|':
                    if (y_next, x_next, direction) not in explored:
                        q.append((y_next, x_next, direction))
                        explored[(y_next, x_next, direction)] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '-':
                    if (y_next, x_next, 'l') not in explored:
                        q.append((y_next, x_next, 'l'))
                        explored[(y_next, x_next, 'l')] = True
                        visited[y_next][x_next] = True
                    if (y_next, x_next, 'r') not in explored:
                        q.append((y_next, x_next, 'r'))
                        explored[(y_next, x_next, 'r')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '/':
                    if (y_next, x_next, 'r') not in explored:
                        q.append((y_next, x_next, 'r'))
                        explored[(y_next, x_next, 'r')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '\\':
                    if (y_next, x_next, 'l') not in explored:
                        q.append((y_next, x_next, 'l'))
                        explored[(y_next, x_next, 'l')] = True
                        visited[y_next][x_next] = True
            
            elif direction == 'd':
                y_next = y + 1
                x_next = x

                if out_of_bounds(y_next, x_next):
                    continue
                elif m[y_next][x_next] in '.|':
                    if (y_next, x_next, direction) not in explored:
                        q.append((y_next, x_next, direction))
                        explored[(y_next, x_next, direction)] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '-':
                    if (y_next, x_next, 'l') not in explored:
                        q.append((y_next, x_next, 'l'))
                        explored[(y_next, x_next, 'l')] = True
                        visited[y_next][x_next] = True
                    if (y_next, x_next, 'r') not in explored:
                        q.append((y_next, x_next, 'r'))
                        explored[(y_next, x_next, 'r')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '/':
                    if (y_next, x_next, 'l') not in explored:
                        q.append((y_next, x_next, 'l'))
                        explored[(y_next, x_next, 'l')] = True
                        visited[y_next][x_next] = True
                elif m[y_next][x_next] == '\\':
                    if (y_next, x_next, 'r') not in explored:                    
                        q.append((y_next, x_next, 'r'))
                        explored[(y_next, x_next, 'r')] = True
                        visited[y_next][x_next] = True

        return sum(visited[i][j] 
                for i in range(len(visited))
                for j in range(len(visited[i])))


    filename = "input.txt"

    m = []
    for line in open(filename):
        line = line.replace("\n", "")
        m.append([c for c in line])

    if part1:
        print(bfs(0, -1, 'r'))
    else:
        max_result = 0
        for y in range(len(m)):
            max_result = max(max_result, bfs(y, -1, 'r'))
            max_result = max(max_result, bfs(y, len(m[0]), 'l'))
        for x in range(len(m)):
            max_result = max(max_result, bfs(-1, x, 'd'))
            max_result = max(max_result, bfs(len(m), x, 'u'))
        print(max_result)

if __name__ == '__main__':
    solve(part1=False)