import random

from Definition.Card import Card, ALL_SUIT
from Definition.Location import Location


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
        self.deck = Deck(suit=None)
        self.excepted = Location(suit=None, name="excepted", visible_to=ALL_SUIT, content=[])
