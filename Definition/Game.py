from Card import VALID_MARK, AllCard
from Nation import Nation
from Nature import Nature


class Game:
    game_id: int
    nature: Nature
    spade: Nation
    heart: Nation
    diamond: Nation
    club: Nation
    turn: list[str] = VALID_MARK

    def __init__(self, game_id: int):
        self.game_id = game_id
        self.nature = Nature()
        self.spade = Nation(suit=VALID_MARK[0])
        self.heart = Nation(suit=VALID_MARK[1])
        self.diamond = Nation(suit=VALID_MARK[2])
        self.club = Nation(suit=VALID_MARK[3])

    def search_nation_by_suit(self, suit: str) -> Nation:
        return [self.spade, self.heart, self.diamond, self.club][VALID_MARK.index(suit)]

    def safe_check(self):
        _ideal_cards = AllCard().all_card
        _current_cards = []
        _current_cards.extend(self.nature.deck.cards)
        _current_cards.extend(self.nature.excepted.cards)
        for suit in VALID_MARK:
            nation = self.search_nation_by_suit(suit=suit)
            _current_cards.extend(nation.castle.hands.cards)
            _current_cards.extend(nation.castle.cabinet.cabinet.cards)
            _current_cards.extend(nation.castle.cabinet.shadow_cabinet.cards)
            _current_cards.append(nation.castle.king)
            _current_cards.extend(nation.castle.barracks.cards)
            for war in nation.field.conflict:
                if nation.suit == war.offensive:
                    _current_cards.extend(war.offensive_formation.left.cards)
                    _current_cards.extend(war.offensive_formation.center.cards)
                    _current_cards.extend(war.offensive_formation.right.cards)
        return True if _ideal_cards == _current_cards else False
