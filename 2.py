colors = ["red", "green", "blue"]

max_cubes = {"red": 12,
             "green": 13,
             "blue": 14}

def solve_part_1():
    result = 0
    for line in open("input.txt"):
        game_str, rest = line.split(":")
        game_id = int(game_str.strip().split()[-1])
        shows = rest.strip().split(";")
        invalid_game = False
        for show in shows:
            if invalid_game:
                break
            cubes_in_show = {color: 0 for color in colors}
            cubes = show.split(",")        
            for cube in cubes:
                for color in colors:
                    if cube.endswith(color):
                        cubes_in_show[color] = int(cube.split()[0].strip())
                        break
            for color in colors:
                if cubes_in_show[color] > max_cubes[color]:
                    invalid_game = True
                    break

        if not invalid_game:
            result += game_id
    print(result)

def solve_part_2():
    def prod(values):
        result = 1
        for v in values:
            result *= v
        return result

    result = 0
    for line in open("input.txt"):
        game_str, rest = line.split(":")
        game_id = int(game_str.strip().split()[-1])
        shows = rest.strip().split(";")
        max_values = {color: 0 for color in colors}
        for show in shows:
            cubes_in_show = {color: 0 for color in colors}
            cubes = show.split(",")        
            for cube in cubes:
                for color in colors:
                    if cube.endswith(color):
                        cubes_in_show[color] = int(cube.split()[0].strip())
                        break
            for color in colors:
                if cubes_in_show[color] > max_values[color]:
                    max_values[color] = cubes_in_show[color]

        result += prod([max_values[color] for color in colors])
    print(result)


if __name__ == '__main__':
    solve_part_2()