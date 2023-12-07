
def solve_part_1():
    filename = "input.txt"

    result = 0
    for line in open(filename):
        card_id, rest = line[:-1].split(":")
        winning, ours = rest.strip().split("|")
        winning_nums = set(int(v) for v in winning.strip().split())
        our_nums = [int(v) for v in ours.strip().split()]

        matches = [num for num in our_nums if num in winning_nums]
        if not matches:
            continue
        result += 2**(len(matches) - 1)

    print(result)


def solve_part_2():
    filename = "input.txt"

    result = 0
    cards = {}
    for line in open(filename):
        card_id, rest = line[:-1].split(":")
        card_number = int(card_id.strip().split()[-1])
        winning, ours = rest.strip().split("|")
        winning_nums = set(int(v) for v in winning.strip().split())
        our_nums = [int(v) for v in ours.strip().split()]
        matches = len([num for num in our_nums if num in winning_nums])
        cards[card_number] = [matches]

    max_id = len(cards) + 1

    for card_id in cards:
        # how many matches does the current card(s) have?
        matches = cards[card_id][0]

        # add cards with higher ids
        for i in range(card_id + 1, min(max_id, card_id + matches + 1)):
            for j in range(len(cards[card_id])):
                cards[i].append(cards[i][0])

    result = sum(len(cards[i]) for i in cards)
    print(result)



if __name__ == '__main__':
    solve_part_2()