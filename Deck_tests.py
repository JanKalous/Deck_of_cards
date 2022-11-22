from deck_of_cards import *
import unittest


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertEqual(isinstance(self.deck.deck_list, list), True)
        self.assertEqual(len(self.deck.deck_list), 52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), f"Deck of 52 cards")

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.deck_list.pop()
        self.assertEqual(self.deck.count(), 51)


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "5")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "5")

    def test_repr(self):
        """repr should return 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "5 of Hearts")


if __name__ == '__main__':
    unittest.main()
