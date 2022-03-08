from Table.Card import Card
from Table.Location import move_card
from Table.World import World


class Diplomacy:
    world: World

    def __init__(self, world: World):
        self.world = world

        for suit in world.turn:
            __negotiation = self._negotiation(world=world, from_suit=suit, to_suit='')  # todo: user input
            if __negotiation[2]:
                nation1 = world.search_nation_by_suit(suit=__negotiation[0])
                nation2 = world.search_nation_by_suit(suit=__negotiation[1])
                _index_of_card_to_assign_to_nation1 = 0  # todo: user input
                _index_of_card_to_assign_to_nation2 = 0  # todo: user input
                move_card(from_location=nation1.castle.hands, to_location=nation2.castle.hands,
                          from_location_index=_index_of_card_to_assign_to_nation2)
                move_card(from_location=nation2.castle.hands, to_location=nation1.castle.hands,
                          from_location_index=_index_of_card_to_assign_to_nation1)

    def _negotiation(self, world: World, from_suit: str, to_suit: str) -> (str, str, bool):
        __proposition = self._suggestion(world=world, from_suit=from_suit, to_suit=to_suit,
                                         marks=[], letters=[])  # todo: user input
        __response = self._response(world=world, from_suit=__proposition[1], to_suit=__proposition[0],
                                    marks=[], letters=[])  # todo: user input
        _count = 2
        _settlement: bool = __response == __proposition
        while _settlement or _count == 0:
            __proposition = self._suggestion(world=world, from_suit=from_suit, to_suit=to_suit,
                                             marks=[], letters=[])  # todo: user input
            __response = self._response(world=world, from_suit=__proposition[1], to_suit=__proposition[0],
                                        marks=[], letters=[])  # todo: user input
            _count -= 1
            _settlement = __response == __proposition if __response else False
        return from_suit, to_suit, _settlement

    def _suggestion(self, world: World, from_suit: str, to_suit: str, marks: list[str], letters: list[str]) \
            -> (str, str, list[Card]) or None:
        _ideal_cards = world.ideal_cards
        _proposition = []
        for card in _ideal_cards:
            if card.suit in marks and card.letter in letters:
                _proposition.append(card)
        return from_suit, to_suit, _proposition  # todo: display on frontend

    def _response(self, world: World, from_suit: str, to_suit: str, marks: list[str], letters: list[str]) \
            -> (str, str, list[Card]) or None:
        _ideal_cards = world.ideal_cards
        _response = []
        for card in _ideal_cards:
            if card.suit in marks and card.letter in letters:
                _response.append(card)
        return from_suit, to_suit, _response  # todo: display on frontend
