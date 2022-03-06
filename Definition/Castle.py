from Card import ALL_MARK
from Location import Location


class Hands(Location):

    def __init__(self, suit: str, name="hands"):
        super().__init__(suit=suit, name=name, visible_to=[None, suit], content=[])


class Cabinet:
    suit: str
    cabinet: Location
    shadow_cabinet: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.cabinet.__init__(suit=self.suit, name="cabinet.light", visible_to=ALL_MARK, content=[])
        self.shadow_cabinet.__init__(suit=self.suit, name="cabinet.dark", visible_to=[None, self.suit], content=[])

    def visibility_initiation(self):
        self.cabinet.visible_to = ALL_MARK
        self.shadow_cabinet.visible_to = [None, self.suit]

    def hide_cabinet(self):
        self.cabinet.visible_to = [None, self.suit]
        self.shadow_cabinet.visible_to = [None, self.suit]

    def open_cabinet(self):
        self.cabinet.visible_to = ALL_MARK
        self.shadow_cabinet.visible_to = ALL_MARK


class Barracks(Location):

    def __init__(self, suit: str, name="barracks"):
        super().__init__(suit=suit, name=name, visible_to=ALL_MARK, content=[])


class Castle:
    suit: str
    king: Location
    hands: Hands
    cabinet: Cabinet
    barracks: Barracks

    def __init__(self, suit: str):
        self.suit = suit
        self.king = Location(suit=self.suit, name='king', visible_to=ALL_MARK, content=[])
        self.hands.__init__(suit=self.suit)
        self.cabinet.__init__(suit=self.suit)
        self.barracks.__init__(suit=self.suit)
