def get_diffs(sequence):
    return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

def extrapolate(sequence, last: bool):
    sequences = [sequence]
    current_sequence = sequence
    while not all(v == 0 for v in current_sequence):
        current_sequence = get_diffs(current_sequence)
        sequences.append(current_sequence)

    for i in reversed(range(len(sequences))):
        if i == len(sequences) - 1:
            continue
        if last:
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
        else:
            sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
    if last:
        return sequences[0][-1]
    return sequences[0][0]
    
def solve(part1: bool):
    filename = "input.txt"

    sequences = []
    for line in open(filename):
        sequences.append([int(v) for v in line.split()])

    print(sum(extrapolate(seq, last=part1) for seq in sequences))

if __name__ == '__main__':
    solve(part1=False)