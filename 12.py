from code import interact
from concurrent.futures import BrokenExecutor
from functools import lru_cache
import itertools
import re
import numpy as np

def count_arrangements_part_1(mask, broken_intervals):
    total_broken = sum(broken_intervals)
    current_broken = sum(c == '#' for c in mask)
    unique_arrangments = set()
    wildcard_positions = [i for i, c in enumerate(mask) if c == "?"]
    for arr in itertools.product(['.', '#'], repeat=len(wildcard_positions)):
        if current_broken + sum(c == "#" for c in arr) != total_broken:
            continue
        
        # substitute
        candidate = list(mask)
        for i in range(len(wildcard_positions)):
            candidate[wildcard_positions[i]] = arr[i]

        candidate = "".join(candidate)
        matches = re.findall("#+", candidate)
        lengths = [len(m) for m in matches]
        if len(lengths) != len(broken_intervals):
            continue
        if all(i == j for i, j in zip(lengths, broken_intervals)):
            unique_arrangments.add(candidate)
    return len(unique_arrangments)


def count_arrangements_part_2(mask, intervals):
    @lru_cache(maxsize=None)
    def count(pos: int, interval: int, length: int):
        # reached end of string, result is either 1 or 0
        if pos >= len(mask):
            if interval >= len(intervals):
                return 1
            if interval == len(intervals) - 1 and length == intervals[-1]:
                return 1
            return 0

        result = 0
        if mask[pos] in '.?':
            # ending the interval or continuing outside an interval     
            if length > 0 and intervals[interval] == length:
                # we're in the interval and have to end it, otherwise constraint violated
                result += count(pos + 1, interval + 1, 0)
            elif length == 0:
                # still waiting for next interval, just go to next symbol                
                result += count(pos + 1, interval, 0)

        if mask[pos] in '#?':
            # continue the current interval
            if interval < len(intervals) and length < intervals[interval]:
                result += count(pos + 1, interval, length + 1)

        return result
    return count(0, 0, 0)
        
                
def solve(part1: bool):
    filename = "input.txt"
    result = 0
    for line in open(filename):
        mask, broken_intervals = line.split()
        if not part1:
            mask = "?".join([mask for i in range(5)])
            broken_intervals = ",".join([broken_intervals for i in range(5)])
        broken_intervals = [int(v) for v in broken_intervals.split(",")]
        if part1:
            result += count_arrangements_part_1(mask, broken_intervals)
        else:
            result += count_arrangements_part_2(mask, broken_intervals)
    print(result)


if __name__ == '__main__':
    solve(part1=False)