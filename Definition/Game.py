from Definition.Card import VALID_SUIT, Card, AllCard
from Definition.Nation import Nation
from Definition.Nature import Nature


class Game:
    game_id: int
    ideal_cards: list[Card]
    nature: Nature
    spade: Nation
    heart: Nation
    diamond: Nation
    club: Nation
    turn: list[str] = VALID_SUIT

    def __init__(self, game_id: int):
        self.game_id = game_id
        self.ideal_cards = AllCard().all_card
        self.nature = Nature()
        self.spade = Nation(suit=VALID_SUIT[0])
        self.heart = Nation(suit=VALID_SUIT[1])
        self.diamond = Nation(suit=VALID_SUIT[2])
        self.club = Nation(suit=VALID_SUIT[3])

    def search_nation_by_suit(self, suit: str) -> Nation:
        return [self.spade, self.heart, self.diamond, self.club][VALID_SUIT.index(suit)]
