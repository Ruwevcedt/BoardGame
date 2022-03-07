from Card import VALID_SUIT, AllCard
from Nation import Nation
from Nature import Nature


class Game:
    game_id: int
    nature: Nature
    spade: Nation
    heart: Nation
    diamond: Nation
    club: Nation
    turn: list[str] = VALID_SUIT

    def __init__(self, game_id: int):
        self.game_id = game_id
        self.nature = Nature()
        self.spade = Nation(suit=VALID_SUIT[0])
        self.heart = Nation(suit=VALID_SUIT[1])
        self.diamond = Nation(suit=VALID_SUIT[2])
        self.club = Nation(suit=VALID_SUIT[3])

    def search_nation_by_suit(self, suit: str) -> Nation:
        return [self.spade, self.heart, self.diamond, self.club][VALID_SUIT.index(suit)]

