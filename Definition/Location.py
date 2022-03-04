import random

from Card import Card, ALL_LETTER


class Location:
    suit: str
    name: str
    visible_to: list[str or None]
    content: list[Card]

    def __init__(self, suit: str or None, name: str, visible_to: list[str or None], content: list[Card]):
        self.suit = suit
        self.name = name + " of " + suit
        self.visible_to = visible_to
        self.content: list[Card] = content

    def __repr__(self):
        return f"\n{self.name} containing {self.content}"

    def update_visibility(self, visible_to: list[str]):
        self.visible_to = visible_to

    def search_by_suit(self, suit: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.content):
            _.append(ind) if card.suit == suit else False
        return _

    def search_by_color(self, color: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.content):
            _.append(ind) if card.color == color else False
        return _

    def search_by_letter(self, letter: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.content):
            _.append(ind) if card.letter == letter else False
        return _

    def search_by_number(self, number: int or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.content):
            _.append(ind) if card.number == number else False
        return _

    def search_by_random(self, quantity: int) -> list[int]:
        _ = []
        for i in range(quantity):
            _.append(random.randrange(0, len(self.content)))
        return _

    def pop_by_indexes(self, indexes: list[int]) -> list[Card]:
        _ = []
        for i, indexes in enumerate(sorted(indexes)):
            _.append(self.content.pop(indexes - i))
        return _

    def put_cards(self, cards: list[Card]):
        self.content.extend(cards)
        self.content.sort(key=ALL_LETTER)
