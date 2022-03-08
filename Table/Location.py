import random

from Table.Card import Card


class Location:
    suit: str
    name: str
    default_visibility: list[str or None]
    current_visibility: list[str or None]
    cards: list[Card]

    def __init__(self, suit: str or None, name: str, visible_to: list[str or None], content: list[Card]):
        self.suit = suit
        self.name = name + " of " + str(suit)
        self.default_visibility = visible_to
        self.current_visibility = visible_to
        self.cards: list[Card] = content

    def __repr__(self):
        return f"\n{self.name} : {self.cards}"

    def update_visibility(self, visible_to: list[str]):
        self.current_visibility = visible_to

    def initiate_visibility(self):
        self.current_visibility = self.default_visibility

    def search_by_suit(self, suit: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.cards):
            _.append(ind) if card.suit == suit else False
        return _

    def search_by_suits(self, suits: list[str] or None) -> list[int]:
        _ = []
        for suit in suits:
            _.extend(self.search_by_suit(suit=suit))
        return _

    def search_by_color(self, color: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.cards):
            _.append(ind) if card.color == color else False
        return _

    def search_by_colors(self, colors: list[str] or None) -> list[int]:
        _ = []
        for color in colors:
            _.extend(self.search_by_color(color=color))
        return _

    def search_by_letter(self, letter: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.cards):
            _.append(ind) if card.letter == letter else False
        return _

    def search_by_letters(self, letters: list[str] or None) -> list[int]:
        _ = []
        for letter in letters:
            _.extend(self.search_by_letter(letter=letter))
        return _

    def search_by_number(self, number: int or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.cards):
            _.append(ind) if card.number == number else False
        return _

    def search_by_numbers(self, numbers: list[int] or None) -> list[int]:
        _ = []
        for number in numbers:
            _.extend(self.search_by_number(number=number))
        return _

    def search_by_random(self, quantity: int) -> list[int]:
        _ = []
        for i in range(quantity):
            _.append(random.randrange(0, len(self.cards)))
        return _

    def pop_by_attribute(self, suit: str, letter: str) -> Card or None:
        _indexes = list(set(self.search_by_suit(suit=suit)) & set(self.search_by_letter(letter=letter)))
        return self.cards.pop(_indexes[0]) if len(_indexes) == 1 else None

    def pop_by_index(self, index: int) -> Card:
        return self.cards.pop(index)

    def pop_by_indexes(self, indexes: list[int]) -> list[Card]:
        _ = []
        for i, index in enumerate(sorted(indexes)):
            _.append(self.cards.pop(index - i))
        return _

    def put_card(self, card: Card):
        self.cards.append(card)

    def put_cards(self, cards: list[Card]):
        self.cards.extend(cards)


def move_card(from_location: Location, to_location: Location, from_location_index: int):
    to_location.put_card(
        card=from_location.pop_by_index(index=from_location_index)
    )


def move_cards(from_location: Location, to_location: Location, from_location_indexes: list[int]):
    to_location.put_cards(
        cards=from_location.pop_by_indexes(indexes=from_location_indexes)
    )
