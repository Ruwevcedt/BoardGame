import random

from Definition.Card import ALL_LETTER, Card
from Definition.Game import Game


class CabinetReshuffle:
    def __call__(self, game: Game):
        self._cabinet_resign(game=game)
        for suit in game.turn:
            self._set_cabinet(game=game, suit=suit, cabinet=None, shadow_cabinet=None)  # todo: user input
        self._update_turn(game=game)

    def _cabinet_resign(self, game: Game):
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            nation.castle.cabinet.hide_cabinet()
            _former_cabinet = []
            _former_cabinet.extend(nation.castle.cabinet.cabinet.pop_by_indexes(indexes=[0]))
            _former_cabinet.extend(nation.castle.cabinet.shadow_cabinet.pop_by_indexes(indexes=[0]))
            nation.castle.hands.put_cards(cards=_former_cabinet)

    def _set_cabinet(self, game: Game, suit: str, cabinet: Card or None, shadow_cabinet: Card or None):
        nation = game.search_nation_by_suit(suit=suit)
        nation.castle.cabinet.cabinet.put_cards([cabinet])
        nation.castle.cabinet.shadow_cabinet.put_cards([shadow_cabinet])
        nation.castle.cabinet.visibility_initiation()

    def _update_turn(self, game: Game):
        _turn = []
        _power = {}.fromkeys(ALL_LETTER, [])
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            _power[nation.castle.cabinet.cabinet.cards[0].letter].append(nation.suit)
        for letter in ALL_LETTER:
            for suits in _power[letter]:
                _turn.extend(random.shuffle(suits))  # todo: use dice
        _turn.reverse()
        game.turn = _turn
