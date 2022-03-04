from Card import ALL_MARK
from Location import Location


class Troop(Location):
    hostile: str

    def __init__(self, suit: str, hostile: str, name: str):
        self.hostile = hostile
        super().__init__(suit=suit, name=name, visible_to=[None, suit], content=[])

    def open_disposition(self):
        self.visible_to = ALL_MARK

    def force_power(self) -> int:
        _ = 0
        for card in self.content:
            _ += card.number if card.suit == self.suit else card.number - 1
        return _


class Battle:
    suit: str
    hostile: str
    left: Troop
    center: Troop
    right: Troop

    def __init__(self, suit: str, hostile: str):
        self.suit = suit
        self.hostile = hostile
        self.left.__init__(suit=self.suit, name="left troop against " + hostile)
        self.center.__init__(suit=self.suit, name="center troop against " + hostile)
        self.right.__init__(suit=self.suit, name="right troop against " + hostile)


class War:
    offensive: str
    defensive: str
    offensive_formation: Battle
    defensive_formation: Battle

    def __init__(self, offensive: str, defensive: str):
        self.offensive = offensive
        self.defensive = defensive
        self.offensive_formation.__init__(suit=offensive, hostile=defensive)
        self.defensive_formation.__init__(suit=defensive, hostile=offensive)


class Field:
    suit: str
    conflict: list[War]

    def __init__(self, suit: str):
        self.suit = suit
        self.conflict = []

