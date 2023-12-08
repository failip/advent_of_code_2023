from __future__ import annotations
from dataclasses import dataclass

def card_to_card_value(card):
    if card == "2":
        return 2
    elif card == "3":
        return 3
    elif card == "4":
        return 4
    elif card == "5":
        return 5
    elif card == "6":
        return 6
    elif card == "7":
        return 7
    elif card == "8":
        return 8
    elif card == "9":
        return 9
    elif card == "T":
        return 10
    elif card == "J":
        return 1
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14


class CamelHand:
    cards: list
    card_string: str
    bid: int
    value: int

    def __init__(self, cards, bid):
        self.bid = bid
        self.card_string = cards
        max_card_count = 0
        unique_cards = set([*cards])
        number_of_jokers = cards.count("J")
        for card in unique_cards:
            card_count = cards.count(card)
            if card_count > max_card_count:
                max_card_count = card_count
        
        number_of_unique_cards = len(unique_cards)
        # High card
        if max_card_count == 1:
            if number_of_jokers == 1:
                self.value = 2
            else:
                self.value = 1
        # Pair
        elif max_card_count == 2 and number_of_unique_cards == 4:
            if number_of_jokers == 1 or number_of_jokers == 2:
                self.value = 4
            else:
                self.value = 2
        # Two pair
        elif max_card_count == 2 and number_of_unique_cards == 3:
            if number_of_jokers == 2:
                self.value = 6
            elif number_of_jokers == 1:
                self.value = 5
            else:
                self.value = 3
        # Three of a kind
        elif max_card_count == 3 and number_of_unique_cards == 3:
            if number_of_jokers == 1 or number_of_jokers == 3:
                self.value = 6
            else:
                self.value = 4 
        # Full house
        elif max_card_count == 3 and number_of_unique_cards == 2:
            if number_of_jokers == 2 or number_of_jokers == 3:
                self.value = 7
            else:
                self.value = 5
        # Four of a kind
        elif max_card_count == 4:
            if number_of_jokers == 1 or number_of_jokers == 4:
                self.value = 7
            else:
                self.value = 6
        # Five of a kind
        elif max_card_count == 5:
            self.value = 7
        else:
            raise Exception("Invalid card count")
        
        self.cards = [card_to_card_value(card) for card in cards]
    
    def __eq__(self, other: CamelHand) -> bool:
        if self.value == other.value:
            if self.cards == other.cards:
                return True
        return False
    
    def __lt__(self, other: CamelHand) -> bool:
        if self.value < other.value:
            return True
        elif self.value == other.value:
            for cards in zip(self.cards, other.cards):
                if cards[0] < cards[1]:
                    return True
                if cards[0] > cards[1]:
                    return False
        return False
    
    def __gt__(self, other: CamelHand) -> bool:
        if self.value > other.value:
            return True
        elif self.value == other.value:
            for cards in zip(self.cards, other.cards):
                if cards[0] > cards[1]:
                    return True
                if cards[0] < cards[1]:
                    return False
        return False
    
    def __str__(self) -> str:
        return f"{self.card_string}"

with open("input.txt", "r") as camel_cards:
    hands = []
    for line in camel_cards:
        hand, bid = line.split()
        hands.append(CamelHand(hand, int(bid)))
    
    hands.sort()

    winnings = 0
    for rank, hand in enumerate(hands):
        winnings += (rank + 1) * hand.bid
    
    print(winnings)