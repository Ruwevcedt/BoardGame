from Card import Card, ALL_MARK
from Location import Location


class Hands(Location):

    def __init__(self, suit: str, name="hands"):
        super().__init__(suit=suit, name=name, visible_to=[None, suit], content=[])


class Cabinet:
    suit: str
    light: Location
    dark: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.light.__init__(suit=self.suit, name="cabinet.light", visible_to=ALL_MARK, content=[])
        self.dark.__init__(suit=self.suit, name="cabinet.dark", visible_to=[None, self.suit], content=[])

    def visibility_initiation(self):
        self.light.visible_to = ALL_MARK
        self.dark.visible_to = [None, self.suit]

    def hide_cabinet(self):
        self.light.visible_to = [None, self.suit]
        self.dark.visible_to = [None, self.suit]

    def open_cabinet(self):
        self.light.visible_to = ALL_MARK
        self.dark.visible_to = ALL_MARK


class Barracks(Location):

    def __init__(self, suit: str, name="barracks"):
        super().__init__(suit=suit, name=name, visible_to=ALL_MARK, content=[])


class Castle:
    suit: str
    king: Card or None
    hands: Hands
    cabinet: Cabinet
    barracks: Barracks

    def __init__(self, suit: str):
        self.suit = suit
        self.king = None
        self.hands.__init__(suit=self.suit)
        self.cabinet.__init__(suit=self.suit)
        self.barracks.__init__(suit=self.suit)


