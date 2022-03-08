from Table.Card import VALID_SUIT, Card, AllCard
from Table.Nation import Nation
from Table.Nature import Nature


class World:
    world_id: int
    ideal_cards: list[Card]
    nature: Nature
    spade: Nation
    heart: Nation
    diamond: Nation
    club: Nation
    turn: list[str] = VALID_SUIT

    def __init__(self, world_id: int):
        self.world_id = world_id
        self.ideal_cards = AllCard().all_card
        self.nature = Nature()
        self.spade = Nation(suit=VALID_SUIT[0])
        self.heart = Nation(suit=VALID_SUIT[1])
        self.diamond = Nation(suit=VALID_SUIT[2])
        self.club = Nation(suit=VALID_SUIT[3])

    def __repr__(self):
        return f"table : {self.world_id}\n" \
               f"{self.ideal_cards}\n" \
               f"{self.nature}\n" \
               f"{self.spade}\n{self.heart}\n{self.diamond}\n{self.club}\n" \
               f"{self.turn}"

    def search_nation_by_suit(self, suit: str) -> Nation:
        return [self.spade, self.heart, self.diamond, self.club][VALID_SUIT.index(suit)]
