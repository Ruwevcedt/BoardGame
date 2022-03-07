import random

from Card import Card, ALL_SUIT
from Location import Location


class Deck(Location):
    def __init__(self, suit: str or None):
        super().__init__(suit=suit, name="deck", visible_to=[None], content=[])

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, quantity: int) -> list[Card]:
        _ = self.cards[:quantity]
        self.cards = self.cards[quantity:]
        return _


class Nature:
    suit: str or None = None
    deck: Deck
    excepted: Location

    def __init__(self):
        self.deck.__init__(suit=None)
        self.excepted.__init__(suit=None, name="excepted", visible_to=ALL_SUIT, content=[])
