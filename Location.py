import Card


class Location(list[Card]):
    suit: str or None
    visibility: int

    def __init__(self, suit: str or None, visibility: int, cards: list[Card]) -> None:
        list.__init__([])  # ?
        self.extend(cards)
        self.suit = suit
        self.visibility = visibility

    def search_cards(self, suits: list[str or None], letters: list[str]) -> list[Card]:
        _output = []
        for _card in self:
            _output.append(_card) if _card.suit in suits and _card.letter in letters else False
        return _output

    def multiple_pop(self, indexes: list[int]) -> list[Card]:
        _indexes = sorted(indexes, reverse=True)
        _output = []
        for _index in indexes:
            _output.append(self.pop(_index))
        return _output
