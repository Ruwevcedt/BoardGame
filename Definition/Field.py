from Definition.Card import ALL_SUIT
from Definition.Location import Location


class Troop(Location):
    hostile: str

    def __init__(self, suit: str, hostile: str, name: str):
        self.hostile = hostile
        super().__init__(suit=suit, name=name, visible_to=[None, suit], content=[])

    def open_disposition(self):
        self.update_visibility(visible_to=ALL_SUIT)

    def force_power(self) -> int:
        _ = 0
        for card in self.cards:
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


class Conflict:
    suit: str
    hostile: str
    is_offensive: bool
    war: War

    def __init__(self, suit: str, hostile: str, is_offensive: bool, war: War):
        self.suit = suit
        self.hostile: hostile
        self.is_offensive = is_offensive
        self.war = war


class Field:
    suit: str
    conflicts: list[Conflict]

    def __init__(self, suit: str):
        self.suit = suit
        self.conflicts = []

    def search_conflict_by_hostile_suit(self, hostile_suit: str):
        for conflict in self.conflicts:
            if conflict.hostile == hostile_suit:
                return conflict

    def add_conflict(self, conflict: Conflict):
        self.conflicts.append(conflict)

    def del_conflict(self, hostile: str):
        for index, conflict in enumerate(self.conflicts):
            if conflict.hostile == hostile:
                self.conflicts.pop(index)
