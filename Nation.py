from Card import VALID_MARK, ALL_MARK
from Location import Location, Field


class Castle:
    suit: str
    king: Location
    visible_cabinet: Location
    invisible_cabinet: Location
    hands: Location
    drafted: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.king = Location(suit=self.suit, name='king' + f" of {self.suit}", visible_to=ALL_MARK, content=[])
        self.visible_cabinet = Location(suit=self.suit, name='visible_cabinet' + f" of {self.suit}",
                                        visible_to=ALL_MARK, content=[])
        self.invisible_cabinet = Location(suit=self.suit, name='invisible_cabinet' + f" of {self.suit}",
                                          visible_to=[None, self.suit], content=[])
        self.hands = Location(suit=self.suit, name='hands' + f" of {self.suit}", visible_to=[None, self.suit],
                              content=[])
        self.drafted = Location(suit=self.suit, name='draft' + f" of {self.suit}", visible_to=ALL_MARK, content=[])

    def open_invisible_cabinet(self):
        self.visible_cabinet.put_content(self.invisible_cabinet.pop_content(self.invisible_cabinet.content[0]))


class Nation:
    suit: str
    foreign_suit: list[str]
    castle: Castle
    war: dict[str, Field or None]

    def __init__(self, suit: str):
        self.suit = suit
        self.castle = Castle(suit=self.suit)

        self.foreign_suit = []
        for _suit in VALID_MARK:
            self.foreign_suit.append(_suit) if _suit != self.suit else False

        self.war = {}
        for _suit in self.foreign_suit:
            self.war[_suit] = None

    def __repr__(self):
        return f"nation of {self.suit}"

    def is_stable(self) -> bool:
        return True if len(self.castle.hands.search_index_of_content(suit=[self.suit])) >= 2 else False

    def open_war(self, field: Field):
        _hostile_suit = field.offensive_suit \
            if field.defensive_suit == self.suit \
            else field.defensive_suit
        self.war[_hostile_suit] = field

    def close_war(self, with_nation: str):
        self.war[with_nation] = None

    def number_of_war(self) -> int:
        _: int = 0
        for _suit in self.foreign_suit:
            _ = _ + 1 if self.war[_suit] is not None else _
        return _


class AllNation:
    all_nation: list[Nation]

    def __init__(self):
        print('\nlocation: generating all nation')
        self.all_nation = []
        for suit in VALID_MARK:
            self.all_nation.append(Nation(suit))
        print('location: all_nation generated: ', self())

    def __call__(self, suit: str = ''):
        return self.all_nation[VALID_MARK.index(suit)] if suit else self.all_nation

    def __getitem__(self, index):
        return self()[index]
