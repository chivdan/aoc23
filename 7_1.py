import enum
from functools import total_ordering

def get_type(hand: str):
    unique_cards = set(hand)
    if len(unique_cards) == 1:
        # five of a kind
        return 6
    if any(hand.count(card) == 4 for card in unique_cards):
        # four of a kind
        return 5
    if len(unique_cards) == 2:
        # full house
        first, second = list(unique_cards)
        if hand.count(first) == 3 and hand.count(second) == 2 or hand.count(first) == 2 and hand.count(second) == 3:
            return 4
    if any(hand.count(card) == 3 for card in unique_cards):
        # three of a kind
        return 3
    if any(hand.count(card1) == 2 and hand.count(card2) == 2
           for card1 in hand
           for card2 in hand if card2 != card1):
        # two pairs
        return 2
    if any(hand.count(card) == 2 for card in hand):
        # one pair
        return 1
    # high card
    return 0
    

card_order = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))

@total_ordering
class Hand:
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = bid
        self.hand_type = get_type(cards)
    
    def __str__(self) -> str:
        return f"{self.cards} [{self.hand_type}]: {self.bid}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return False
        return self.cards == __value.cards
    
    def __lt__(self, other: 'Hand') -> bool:
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for c1, c2 in zip(self.cards, other.cards):
            if card_order.index(c1) > card_order.index(c2):
                return False
            if card_order.index(c1) < card_order.index(c2):
                return True
        return False
    

def solve_part_1():
    filename = "input.txt"

    hands = []
    for line in open(filename):
        cards, bid = line.split()[0], int(line.split()[1])
        hands.append(Hand(cards, bid))

    hands = sorted(hands)
    result = sum(rank * hand.bid for rank, hand in enumerate(hands, start=1))
    print(result)

if __name__ == '__main__':
    solve_part_1()