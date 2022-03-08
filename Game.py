from Action import RandomAction, Action
from Definition.Card import VALID_SUIT
from Definition.World import World
from Phase import Setup, NewYear, CabinetReshuffle, Diplomacy


class Game:
    year: int
    game: World
    spade_user: Action or RandomAction
    heart_user: Action or RandomAction
    diamond_user: Action or RandomAction
    club_user: Action or RandomAction

    def __init__(self, game: World):
        self.year = 0
        self.game = game
        Setup.Setup(game=self.game).setup()
        self.spade_user = RandomAction(
            nation=self.game.search_nation_by_suit(suit=VALID_SUIT[0]))  # todo: Action if user else RandomAction
        self.heart_user = RandomAction(
            nation=self.game.search_nation_by_suit(suit=VALID_SUIT[1]))  # todo: Action if user else RandomAction
        self.diamond_user = RandomAction(
            nation=self.game.search_nation_by_suit(suit=VALID_SUIT[2]))  # todo: Action if user else RandomAction
        self.club_user = RandomAction(
            nation=self.game.search_nation_by_suit(suit=VALID_SUIT[3]))  # todo: Action if user else RandomAction

    def round(self):
        self.year += 1
        self._new_year()
        self._cabinet_reshuffle()
        self._diplomacy()

    def search_user_by_suit(self, suit: str) -> Action or RandomAction:
        return [self.spade_user, self.heart_user, self.diamond_user, self.club_user][VALID_SUIT.index(suit)]

    def _new_year(self):
        NewYear.NewYear(game=self.game).new_year()

    def _cabinet_reshuffle(self):
        for suit in VALID_SUIT:
            _user = self.search_user_by_suit(suit=suit)
            CabinetReshuffle.CabinetReshuffle(game=self.game).select_cabinet(
                suit=suit,
                cabinet=_user.select_from_hands(),
                shadow_cabinet=_user.select_from_hands() - 1
            )
        CabinetReshuffle.CabinetReshuffle(game=self.game).cabinet_reshuffle()

    def _diplomacy(self):
        Diplomacy.Diplomacy(game=self.game)
