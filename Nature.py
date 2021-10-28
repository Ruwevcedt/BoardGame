import random

from Card import ALL_MARK
from Location import Location


class Nature:
    deck: Location
    exception: Location

    def __init__(self):
        print('\nlocation: generating nature')
        self.deck = Location(suit=None, name='deck', visible_to=[None], content=[])
        self.exception = Location(suit=None, name='excepted', visible_to=ALL_MARK, content=[])
        print('location: nature generated: ', self)

    def __repr__(self):
        return f"MOTHER NATURE\ndeck: {self.deck.content}\nexcepted: {self.exception.content}"

    def deck_shuffle(self):
        random.shuffle(self.deck.content)

    def deck_draw(self, number: int = 1):
        _ = self.deck.content[:number]
        self.deck.content = self.deck.content[number:]
        return _
