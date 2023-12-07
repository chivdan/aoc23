def simulate_race(charging_time, race_time):
    assert charging_time <= race_time
    speed = charging_time
    remaining_time = race_time - charging_time
    return remaining_time * speed

def get_winning_races_count(race_time, record):
    result = 0
    for charging_time in range(race_time):
        if simulate_race(charging_time, race_time) > record:
            result += 1
    return result

def prod(values):
    result = 1
    for v in values:
        result *= v
    return result

def solve_part_1():
    filename = "input.txt"

    times = []
    distances = []
    for line in open(filename):
        if "Time" in line:
            times = [int(v.strip()) for v in line.split(":")[-1].strip().split()]
        elif "Distance" in line:
            distances = [int(v.strip()) for v in line.split(":")[-1].strip().split()]

    winning_counts = []
    for race_time, record in zip(times, distances):
        count = get_winning_races_count(race_time, record)
        winning_counts.append(count)

    print(prod(winning_counts))

def solve_part_2():
    filename = "input.txt"

    race_time = []
    distance = []
    for line in open(filename):
        if "Time" in line:
            race_time = int("".join([v.strip() for v in line.split(":")[-1].strip().split()]))
        elif "Distance" in line:
            distance = int("".join([v.strip() for v in line.split(":")[-1].strip().split()]))

    count = get_winning_races_count(race_time, distance)
    print(count)
    

if __name__ == '__main__':
    solve_part_1()
    solve_part_2()