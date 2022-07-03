import Letter
import Suit


class Card:
    suit: str
    letter: str

    def __init__(self, suit: str or None, letter: str):
        self.suit = suit
        self.letter = letter

    def __repr__(self):
        return f"Card: {self.suit} {self.letter}"


POWERORDER = [Card(suit=None, letter='Z')]
for _letter in Letter.REGULARLETTER:
    for _suit in Suit.REGULARSUIT:
        POWERORDER.append(Card(suit=_suit, letter=_letter))
