import random

from Definition.Card import ALL_LETTER, Card
from Definition.Game import Game


class CabinetReshuffle:
    def __init__(self, game: Game):
        self._hide_all_cabinets(game=game)
        self._cabinet_resign(game=game)
        for suit in game.turn:
            self._set_cabinet(game=game, suit=suit, cabinet=None, shadow_cabinet=None)  # todo: user input
        self._reveal_cabinets(game=game)
        self._update_turn(game=game)

    def _hide_all_cabinets(self, game: Game):
        for suit in game.turn:
            game.search_nation_by_suit(suit=suit).castle.cabinet.hide_cabinet()

    def _cabinet_resign(self, game: Game):
        for suit in game.turn:
            game.search_nation_by_suit(suit=suit).castle.cabinet_resign()

    def _set_cabinet(self, game: Game, suit: str, cabinet: Card or None, shadow_cabinet: Card or None):
        nation = game.search_nation_by_suit(suit=suit)
        nation.castle.cabinet.cabinet.cards = cabinet
        nation.castle.cabinet.shadow_cabinet.cards = shadow_cabinet

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
                _turn.extend(_power[letter]) # todo: use dice
            else:
                pass
        game.turn = _turn
