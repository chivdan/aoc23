

def solve():
    def out_of_bounds(the_yy, the_xx) -> bool:
        return the_xx < 0 or the_xx >= len(m[0]) or the_yy < 0 or the_yy >= len(m)

    def bfs(yy, xx, initial_direction):
        explored = dict()
        explored[(yy, xx - 1, initial_direction)] = True
        q = [(yy, xx - 1, initial_direction)]
        # visited[yy][xx] = True

        while q:
            # print(q)
            y, x, direction = q.pop(0)

            if not (y == 0 and x == -1 and direction == 'r') and out_of_bounds(y, x):
                print(yy, xx, "out")
                continue
            
            # visited[y][x] = True
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

    filename = "input.txt"

    m = []
    for line in open(filename):
        line = line.replace("\n", "")
        m.append([c for c in line])

    visited = [[False for i in range(len(m[0]))] for v in m]

    bfs(0, 0, 'r')

    # for v in visited:
    #     print("".join(["#" if v[i] else "." for i in range(len(m))]))

    print(sum(visited[i][j] 
              for i in range(len(visited))
              for j in range(len(visited[i]))))

if __name__ == '__main__':
    solve()