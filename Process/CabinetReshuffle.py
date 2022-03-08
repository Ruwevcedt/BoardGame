import random

from Definition.Card import ALL_LETTER
from Definition.Nation import Nation
from Definition.Game import Game


class CabinetReshuffle:
    game: Game

    def __init__(self, game: Game):
        self.game = game

    def cabinet_resign(self):
        self._hide_all_cabinets(game=self.game)
        self._cabinet_resign(game=self.game)

    def select_cabinet(self, suit: str, cabinet: int or None, shadow_cabinet: int or None):
        self._set_cabinet(game=self.game, suit=suit, cabinet=cabinet, shadow_cabinet=shadow_cabinet)

    def cabinet_reshuffle(self):
        self._reveal_cabinets(game=self.game)
        self._update_turn(game=self.game)

    def _hide_all_cabinets(self, game: Game):
        for suit in game.turn:
            game.search_nation_by_suit(suit=suit).castle.cabinet.hide_cabinet()

    def _cabinet_resign(self, game: Game):
        for suit in game.turn:
            game.search_nation_by_suit(suit=suit).castle.cabinet_resign()

    def _set_cabinet(self, game: Game, suit: str, cabinet: int or None, shadow_cabinet: int or None):
        game.search_nation_by_suit(suit=suit).castle.cabinet_appointment(cabinet=cabinet, shadow_cabinet=shadow_cabinet)

    def _reveal_cabinets(self, game: Game):
        for suit in game.turn:
            game.search_nation_by_suit(suit=suit).castle.cabinet.initiate_visibility()

    def _update_turn(self, game: Game):
        _turn = []
        _power = {}.fromkeys(ALL_LETTER, [])
        _power[''] = []
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            if nation.castle.cabinet.cabinet.cards:
                _power[nation.castle.cabinet.cabinet.cards[0].letter].append(nation.suit)
            else:
                _power[''].append(nation.suit)
        for letter in _power.keys():
            if _power[letter]:
                random.shuffle(_power[letter])
                _turn.extend(_power[letter])  # todo: use dice
            else:
                pass
        game.turn = _turn
