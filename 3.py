def is_digit(c):
        return '0' <= c <= '9'

class NumberEntry:
    def __init__(self, x_start, x_end, y, number):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.number = number

    def is_adjacent(self, x, y):
        return self.points_are_adjacent(self.x_start, self.y, x, y) or self.points_are_adjacent(self.x_end, self.y, x, y)

    def points_are_adjacent(self, x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def solve_part_1():
    symbol_positions = []
    filename = "input.txt"

    y = 0
    for line in open(filename):
        for x, c in enumerate(line[:-1]):
            if not is_digit(c) and c != ".":
                symbol_positions.append((x, y))
        y += 1

    y = 0
    number_positions = []
    for line in open(filename):
        start_number = -1
        number = ""
        for x, c in enumerate(line[:-1]):
            if is_digit(c):
                if not number:
                    start_number = x
                number += c
            elif number:
                number_positions.append(NumberEntry(start_number, x - 1, y, int(number)))
                number = ""
                start_number = -1

        if number:
            number_positions.append(NumberEntry(start_number, len(line) - 1, y, int(number)))
        y += 1

    result = 0
    for number_pos in number_positions:
        if any(number_pos.is_adjacent(x, y) for x, y in symbol_positions):
            result += number_pos.number
            # print(number_pos.number, number_pos.x_start, number_pos.x_end, number_pos.y)
    print(result)

def solve_part_2():
    symbol_positions = []
    filename = "input.txt"

    y = 0
    for line in open(filename):
        for x, c in enumerate(line[:-1]):
            if c == "*":
                symbol_positions.append((x, y))
        y += 1

    y = 0
    number_positions = []
    for line in open(filename):
        start_number = -1
        number = ""
        for x, c in enumerate(line[:-1]):
            if is_digit(c):
                if not number:
                    start_number = x
                number += c
            elif number:
                number_positions.append(NumberEntry(start_number, x - 1, y, int(number)))
                number = ""
                start_number = -1

        if number:
            number_positions.append(NumberEntry(start_number, len(line) - 1, y, int(number)))
        y += 1

    result = 0

    for x, y in symbol_positions:
        adjacent_numbers = [number_pos for number_pos in number_positions 
                            if number_pos.is_adjacent(x, y)]
        if len(adjacent_numbers) == 2:
            result += adjacent_numbers[0].number * adjacent_numbers[1].number

    print(result)

if __name__ == '__main__':
    solve_part_2()