import random

from Definition.Card import ALL_LETTER
from Definition.Game import Game


class CabinetReshuffle:
    def __call__(self, game: Game):
        self._cabinet_resign(game=game)

    def _cabinet_resign(self, game: Game):
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            _former_cabinet = []
            _former_cabinet.extend(nation.castle.cabinet.light.pop_by_indexes(indexes=[0]))
            _former_cabinet.extend(nation.castle.cabinet.dark.pop_by_indexes(indexes=[0]))
            nation.castle.hands.put_cards(cards=_former_cabinet)

    def _set_cabinet(self, game: Game):
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            nation.castle.cabinet.light.put_cards(cards=[])  # todo: need user input
            nation.castle.cabinet.dark.put_cards(cards=[])  # todo: need user input

    def _update_turn(self, game: Game):
        _turn = []
        _power = {}.fromkeys(ALL_LETTER, [])
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            _power[nation.castle.cabinet.light.content[0].letter].append(nation.suit)
        for letter, suits in _power:
            _turn.extend(random.shuffle(suits))
        _turn.reverse()
        game.turn = _turn
