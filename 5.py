
class Interval:
    def __init__(self, start, length) -> None:
        self.start = start
        self.end = start + length - 1
        self.length = length
        assert 0 <= self.start <= self.end, f"start = {start}, end = {self.end}, length = {length}"

    def contains(self, number):
        return self.start <= number <= self.end

    def contains_interval(self, interval):
        return self.start <= interval.start <= interval.end <= self.end

    def intersects(self, interval):
        return self.end >= interval.start or self.end <= interval.end

    def get_mapping(self, destination_interval: 'Interval', number: int):
        offset = number - self.start
        return destination_interval.start + offset
    
    def get_interval_mapping(self, destination_interval: 'Interval', interval):
        if self.contains_interval(interval) or interval.contains_interval(self):
            intersection_length = min(self.length, interval.length)
        else:
            intersection_length = max(self.end - interval.start + 1, interval.end - self.start + 1)

        if self.contains_interval(interval):
            offset = interval.start - self.start
            return [Interval(destination_interval.start + offset, intersection_length)]
        if self.start <= interval.start <= self.end:
            offset = interval.start - self.start
            start = destination_interval.start + offset
            length = self.end - interval.start + 1
            return [Interval(start, length), Interval(self.end + 1, interval.end - self.end)]
        if interval.start <= self.start <= interval.end:
            start = destination_interval.start
            length = interval.end - self.start + 1
            return [Interval(start, length), Interval(interval.start, self.start - interval.start)]


    def __hash__(self) -> int:
        return hash((self.start, self.end))
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Interval):
            return False
        return self.start == __value.start and self.end == __value.end

    def __str__(self) -> str:
        return f"[{self.start}..{self.end}]"

    def __repr__(self) -> str:
        return str(self)

def get_destination_values(mapping, values):
    result = []

    for value in values:
        found_value = False
        for interval in mapping:
            if interval.contains(value):
                result.append(interval.get_mapping(mapping[interval], value))
                found_value = True
                break
        if not found_value:
            result.append(value)

    return result

def solve_part_1():
    filename = "input.txt"

    seeds = []
    map_type = None
    maps = []
    current_map = {}
    for line in open(filename):
        if "seeds:" in line:
            seeds = [int(v) for v in line[:-1].split(":")[-1].strip().split()]
        elif "map" in line:
            map_type = line.split()[0]
            continue
        elif len(line) == 1:
            if map_type is not None:
                maps.append(current_map)
            current_map = {}
            map_type = None
        else:
            destination_range_start, source_range_start, length = [int(v) for v in line.split()]
            source_range = Interval(source_range_start, length)
            destination_range = Interval(destination_range_start, length)
            current_map[source_range] = destination_range

    values = seeds
    for mapping in maps:
        values = get_destination_values(mapping, values)
    print(min(values))     


def get_destination_intervals(mapping, intervals):
    result = set()

    for source_interval in intervals:
        found_value = False
        for interval in mapping:
            if interval.intersects(source_interval):
                mapped_intervals = interval.get_interval_mapping(mapping[interval], source_interval)
                if not mapped_intervals:
                    continue
                if len(mapped_intervals) == 1:
                    result.add(mapped_intervals[0])
                elif len(mapped_intervals) == 2:
                    result.add(mapped_intervals[0])
                    if not mapped_intervals[1] in result:
                        for i in get_destination_intervals(mapping, [mapped_intervals[1]]):
                            if not i in result:
                                result.add(i)
                found_value = True
                break
        if not found_value:
            result.add(source_interval)
    return result


def solve_part_2():
    filename = "input.txt"

    seeds = []
    map_type = None
    maps = []
    current_map = {}
    for line in open(filename):
        if "seeds:" in line:
            seeds_raw = [int(v) for v in line[:-1].split(":")[-1].strip().split()]
            for i in range(0, len(seeds_raw), 2):
                seeds.append(Interval(seeds_raw[i], seeds_raw[i + 1]))
        elif "map" in line:
            map_type = line.split()[0]
            continue
        elif len(line) == 1:
            if map_type is not None:
                maps.append(current_map)
            current_map = {}
            map_type = None
        else:
            destination_range_start, source_range_start, length = [int(v) for v in line.split()]
            source_range = Interval(source_range_start, length)
            destination_range = Interval(destination_range_start, length)
            current_map[source_range] = destination_range

    intervals = seeds
    for mapping in maps:
        intervals = get_destination_intervals(mapping, intervals)
    print(min(interval.start for interval in intervals))     



if __name__ == '__main__':
    solve_part_1()
    solve_part_2()