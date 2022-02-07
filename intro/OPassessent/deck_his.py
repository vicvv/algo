import random
import unittest

class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = []

        for i in range(n):
            if len(self.cards) == 0:
                break

            card = self.cards.pop()
            dealt_cards.append(card)

        return dealt_cards

    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )

    def contains(self, card):
        return card in self.cards

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)


valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
valid_suits = ['H', 'D', 'C', 'S']
valid_cards = [f'{value}{suit}' for suit in valid_suits for value in valid_values]



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        deck2.shuffle()
        self.assertNotEqual(deck1.get_cards(), deck2.get_cards())

    def test_case_2(self):
        deck1 = Deck()
        cards = deck1.get_cards()
        self.assertEqual(52, len(cards))
        self.assertEqual(52, len(deck1))
        for card in cards:
            self.assertIn(card, valid_cards)

    def test_case_3(self):
        deck1 = Deck()
        for card in valid_cards:
            self.assertTrue(deck1.contains(card))

    def test_case_4(self):
        deck1 = Deck()
        deck2 = deck1.copy()
        self.assertEqual(deck1.get_cards(), deck2.get_cards())
        deck1.shuffle()
        self.assertNotEqual(deck1.get_cards(), deck2.get_cards())

    def test_case_5(self):
        deck1 = Deck()
        deck1.shuffle()
        cards = deck1.deal(1)
        self.assertEqual(1, len(cards))
        card = cards[0]
        self.assertFalse(deck1.contains(card))

    def test_case_6(self):
        deck1 = Deck()
        deck1.shuffle()
        deck1.sort_by_suit()
        
        for (i, card) in enumerate(deck1.get_cards()):
            suit = card[len(card)-1]
            if i < 13:
                self.assertEqual('H', suit)
            elif i < 26:
                self.assertEqual('D', suit)
            elif i < 39:
                self.assertEqual('C', suit)
            else:
                self.assertEqual('S', suit)

    def test_case_7(self):
        deck1 = Deck()
        cards_seen = set([])
        for i in range(52):
            cards = deck1.deal(1)
            self.assertEqual(1, len(cards))
            card = cards[0]
            self.assertNotIn(card, cards_seen)
            cards_seen.add(cards[0])

    def test_case_8(self):
        deck1 = Deck()
        for i in range(10):
            cards = deck1.deal(5)
            self.assertEqual(5, len(cards))
        cards = deck1.deal(5)
        self.assertEqual(2, len(cards))

    def test_case_9(self):
        deck1 = Deck()
        deck1.shuffle()
        cards = deck1.get_cards()
        cards[0] = 'FAKE CARD'
        self.assertNotIn('FAKE CARD', deck1.get_cards())


if __name__ == '__main__':
    unittest.main()