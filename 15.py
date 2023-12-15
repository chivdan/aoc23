import enum


def my_hash(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def solve_part_1():
    filename = "input.txt"

    line = open(filename).read().replace('\n', '')
    words = line.split(",")
    result = 0
    for word in words:
        result += my_hash(word)
    print(result)

def find_label(entries, label):
    for i in range(len(entries)):
        if entries[i][0] == label:
            return i
    return -1

def solve_part_2():
    filename = "input.txt"

    boxes = [[] for i in range(256)]

    line = open(filename).read().replace('\n', '')
    words = line.split(",")
    for word in words:
        if "=" in word:
            label, focal = word.split("=")
            focal = int(focal)
            box_id = my_hash(label)
            label_id = find_label(boxes[box_id], label)
            if label_id == -1:
                boxes[box_id].append((label, focal))
            else:
                boxes[box_id][label_id] = label, focal
        elif "-" in word:
            label = word.replace("-", "")
            box_id = my_hash(label)
            label_id = find_label(boxes[box_id], label)
            if label_id >= 0:
                boxes[box_id] = boxes[box_id][:label_id] + boxes[box_id][label_id + 1:]

    result = 0
    for box_id in range(len(boxes)):
        for i, (label, focal) in enumerate(boxes[box_id], start=1):
            result += (box_id + 1) * i * focal

    print(result)

if __name__ == '__main__':
    solve_part_1()
    solve_part_2()