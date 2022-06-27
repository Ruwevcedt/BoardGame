import random

from Action import RandomAction, Action
from Phase import Setup, NewYear, CabinetReshuffle
from Table.Card import VALID_SUIT, AllCard
from Table.World import World


class Game:
    year: int
    world: World
    spade_user: Action or RandomAction
    heart_user: Action or RandomAction
    diamond_user: Action or RandomAction
    club_user: Action or RandomAction

    def __init__(self, world: World):
        self.world = world

        Setup.Setup(world=self.world).setup()

        self.spade_user = RandomAction(
            nation=self.world.search_nation_by_suit(suit=VALID_SUIT[0]))  # todo: Action if user else RandomAction
        self.heart_user = RandomAction(
            nation=self.world.search_nation_by_suit(suit=VALID_SUIT[1]))  # todo: Action if user else RandomAction
        self.diamond_user = RandomAction(
            nation=self.world.search_nation_by_suit(suit=VALID_SUIT[2]))  # todo: Action if user else RandomAction
        self.club_user = RandomAction(
            nation=self.world.search_nation_by_suit(suit=VALID_SUIT[3]))  # todo: Action if user else RandomAction

        self.year = 0

    def round(self):
        self.year += 1
        self._new_year()
        self._cabinet_reshuffle()
        self._reset_turn()

    def search_user_by_suit(self, suit: str) -> Action or RandomAction:
        return [self.spade_user, self.heart_user, self.diamond_user, self.club_user][VALID_SUIT.index(suit)]

    def _new_year(self):
        NewYear.NewYear(world=self.world).new_year()

    def _cabinet_reshuffle(self):
        for suit in self.world.turn:
            _user = self.search_user_by_suit(suit=suit)
            CabinetReshuffle.CabinetReshuffle(world=self.world).select_cabinet(
                suit=suit,
                cabinet=_user.select_from_hands(),
                shadow_cabinet=_user.select_from_hands() - 1
            )
        CabinetReshuffle.CabinetReshuffle(world=self.world).cabinet_reshuffle()

    def _reset_turn(self):
        _all_card = AllCard()
        self.world.turn = []
        _ = {}
        for card in _all_card.all_card_by_letter_suit:
            _[f"{card.suit} {card.letter}"] = []
        for name_of_nation in VALID_SUIT:
            _card = self.world.search_nation_by_suit(name_of_nation).castle.cabinet.cabinet.cards[0]
            _[f"{_card.suit} {_card.letter}"] = [name_of_nation]
        for card in _all_card.all_card_by_letter_suit:
            if _[f"{card.suit} {card.letter}"]:
                random.shuffle(_[f"{card.suit} {card.letter}"]) if card.letter == "Z" else False
                self.world.turn.extend(_[f"{card.suit} {card.letter}"])
