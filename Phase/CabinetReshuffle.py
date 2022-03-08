import random

from Table.Card import ALL_LETTER
from Table.World import World


class CabinetReshuffle:
    world: World

    def __init__(self, world: World):
        self.world = world

    def cabinet_resign(self):
        self._hide_all_cabinets(world=self.world)
        self._cabinet_resign(world=self.world)

    def select_cabinet(self, suit: str, cabinet: int or None, shadow_cabinet: int or None):
        self._set_cabinet(world=self.world, suit=suit, cabinet=cabinet, shadow_cabinet=shadow_cabinet)

    def cabinet_reshuffle(self):
        self._reveal_cabinets(world=self.world)
        self._update_turn(world=self.world)

    def _hide_all_cabinets(self, world: World):
        for suit in world.turn:
            world.search_nation_by_suit(suit=suit).castle.cabinet.hide_cabinet()

    def _cabinet_resign(self, world: World):
        for suit in world.turn:
            world.search_nation_by_suit(suit=suit).castle.cabinet_resign()

    def _set_cabinet(self, world: World, suit: str, cabinet: int or None, shadow_cabinet: int or None):
        world.search_nation_by_suit(suit=suit).castle.cabinet_appointment(cabinet=cabinet,
                                                                          shadow_cabinet=shadow_cabinet)

    def _reveal_cabinets(self, world: World):
        for suit in world.turn:
            world.search_nation_by_suit(suit=suit).castle.cabinet.initiate_visibility()

    def _update_turn(self, world: World):
        _turn = []
        _power = {}.fromkeys(ALL_LETTER, [])
        _power[''] = []
        for suit in world.turn:
            nation = world.search_nation_by_suit(suit=suit)
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
        world.turn = _turn
