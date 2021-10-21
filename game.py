import operator

from card import VALID_MARK, ALL_CARD
from location import NATURE, ALL_NATION


class Turn:
    turn: list[str]
    now_str: str
    now_index: int

    def __init__(self):
        self.turn = VALID_MARK

    def initiate_turn(self, turn: list[str]):
        self.turn = turn
        self.now_index = 0
        self.now_str = self.turn[self.now_index]

    def turn_over(self):
        self.now_index = 0 if self.now_index == 3 else self.now_index + 1
        self.now_str = self.turn[self.now_index]
        return self


class Game:
    id: int
    turn: Turn

    def __init__(self, id: int):
        self.id = id
        self.turn = Turn()

        print('\nGame: generating deck')
        NATURE.deck.content.extend(ALL_CARD)
        NATURE.initiate_observability()
        print(f'Game: deck generated: {NATURE.deck.content}')

        print('\nGame: distributing king')
        _kings = NATURE.deck.search_card(letter=['K'], show_card=True)['cards']
        [NATURE.deck.content.remove(_card) for _card in _kings]

        for index, nation in enumerate(ALL_NATION):
            nation.castle.king.content.append(_kings[index])
            nation.castle.initiate_observability()
        print(f'Game: king distributed: {[nation.castle.king for nation in ALL_NATION]}')

        print('\nGame: shuffling deck')
        NATURE.deck_shuffle()
        print(f'Game: deck shuffled: {NATURE.deck.content}')

        print('\nGame: distribute hands')
        for _turn in range(5):
            for nation in ALL_NATION:
                nation.castle.hands.content.extend(NATURE.deck_draw(1))

        _can_start = {True: [], False: []}
        for index, nation in enumerate(ALL_NATION):
            _can_start[nation.is_stable()].append(index)
        while len(_can_start[False]):
            for index in _can_start[False]:
                _foreigner: list = ALL_NATION[index].castle.hands.show_foreigner()
                ALL_NATION[index].castle.hands.content = \
                    ALL_NATION[index].castle.hands.show_citizen()
                NATURE.deck.content.extend(_foreigner)

                ALL_NATION[index].castle.hands.content.extend(NATURE.deck_draw(len(_foreigner)))

            _can_start = {True: [], False: []}
            for index, nation in enumerate(ALL_NATION):
                _can_start[nation.is_stable()].append(index)
        for nation in ALL_NATION:
            nation.castle.initiate_observability()
        print(f'Game: hands distributed: {[nation.castle.hands for nation in ALL_NATION]}')

        print('\nGame: check location and observability of all cards')
        for card in ALL_CARD:
            print(f"'{card}'    is in '{card.location}' and     visible to {card.observable}")
        print('Game: all cards checked')

        print('\nGame: determining turn')
        _ = {}
        for nation in ALL_NATION:
            _[nation.suit] = nation.castle.hands.minimum_number()
        _ = sorted(_, key=operator.itemgetter(1))  # ?: I expected _ = [(suit, number)] but output is [suit]
        self.turn.initiate_turn(_)
        print(f'Game: turn determined: {self.turn.turn}')
