from Definition.Card import AllCard, Card
from Definition.Game import Game


class Diplomacy:
    def __call__(self, game: Game):
        for suit in game.turn:
            __negotiation = self._negotiation(game=game, from_suit=suit, to_suit='')  # todo: user input
            if __negotiation[2]:
                nation1 = game.search_nation_by_suit(suit=__negotiation[0])
                nation2 = game.search_nation_by_suit(suit=__negotiation[1])
                nation2.castle.hands.put_cards(nation1.castle.hands.pop_by_indexes([]))  # todo: user input
                nation1.castle.hands.put_cards(nation2.castle.hands.pop_by_indexes([]))  # todo: user input

    def _negotiation(self, game: Game, from_suit: str, to_suit: str) -> (str, str, bool):
        __proposition = self._suggestion(game=game, from_suit=from_suit, to_suit=to_suit,
                                         mark=[], letter=[])  # todo: user input
        __response = self._response(game=game, from_suit=__proposition[1], to_suit=__proposition[0],
                                    mark=[], letter=[])  # todo: user input
        _count = 3
        _settlement: bool = __response == __proposition
        while _settlement or _count == 0:
            __proposition = self._suggestion(game=game, from_suit=from_suit, to_suit=to_suit,
                                             mark=[], letter=[])  # todo: user input
            __response = self._response(game=game, from_suit=__proposition[1], to_suit=__proposition[0],
                                        mark=[], letter=[])  # todo: user input
            _count -= 1
            _settlement: bool = __response == __proposition
        return from_suit, to_suit, _settlement

    def _suggestion(self, game: Game, from_suit: str, to_suit: str, mark: list[str], letter: list[str]) \
            -> (str, str, list[Card]) or None:
        from_nation = from_suit
        if to_suit in game.turn:
            to_nation = to_suit
        else:
            return None
        _ideal_cards = AllCard()
        _proposition = []
        for card in _ideal_cards.all_card:
            if card.suit in mark and card.letter in letter:
                _proposition.append(card)
        return from_nation, to_nation, _proposition  # todo: display on frontend

    def _response(self, game: Game, from_suit: str, to_suit: str, mark: list[str], letter: list[str]) \
            -> (str, str, list[Card]) or None:
        if from_suit in game.turn:
            from_nation = from_suit
        else:
            return None
        if to_suit in game.turn:
            to_nation = to_suit
        else:
            return None
        _ideal_cards = AllCard()
        _response = []
        for card in _ideal_cards.all_card:
            if card.suit in mark and card.letter in letter:
                _response.append(card)
        return from_nation, to_nation, _response  # todo: display on frontend
