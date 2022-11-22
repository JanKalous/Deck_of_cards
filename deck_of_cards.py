import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    suit_tuple = ("Hearts", "Diamonds", "Clubs", "Spades")

    value_tuple = ("A", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.deck_list = [Card(value=v, suit=s)
                          for v in Deck.value_tuple for s in Deck.suit_tuple]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.deck_list)

    def count(self):
        return len(self.deck_list)

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.deck_list)
        else:
            raise ValueError("Only full decks can be shuffled")

        return self

    def _deal(self, deal_num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        dealt = []

        while deal_num >= 1 and self.count() >= 1:
            deal_num -= 1
            dealt.append(self.deck_list.pop())
        return dealt

    def deal_card(self):
        self._deal(1)

    def deal_hand(self, dnum):
        self._deal(dnum)

deck = Deck()

