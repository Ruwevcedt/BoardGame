from Table.Card import ALL_SUIT
from Table.Location import Location


class Troop(Location):
    hostile: str

    def __init__(self, suit: str, hostile: str, name: str):
        super().__init__(suit=suit, name=name, visible_to=[None, suit], content=[])
        self.hostile = hostile

    def open_disposition(self):
        self.update_visibility(visible_to=ALL_SUIT)

    def force_power(self) -> int:
        _ = 0
        for card in self.cards:
            _ += card.number if card.suit == self.suit else card.number - 1
        return _


class Army:
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

    def __repr__(self):
        return f"army of {self.suit} against {self.hostile} : \n{self.left}\n{self.center}\n{self.right}"


class Battle:
    offensive: str
    defensive: str
    offensive_army: Army
    defensive_army: Army

    def __init__(self, offensive: str, defensive: str):
        self.offensive = offensive
        self.defensive = defensive
        self.offensive_army.__init__(suit=offensive, hostile=defensive)
        self.defensive_army.__init__(suit=defensive, hostile=offensive)

    def __repr__(self):
        return f"{self.offensive} attacks {self.defensive}\n" \
               f"offensive_army : {self.offensive_army}\n" \
               f"defensive_army : {self.defensive_army}"


class War:
    suit: str
    hostile: str
    is_offensive: bool
    battle: Battle

    def __init__(self, suit: str, hostile: str, is_offensive: bool, battle: Battle):
        self.suit = suit
        self.hostile: hostile
        self.is_offensive = is_offensive
        self.battle = battle

    def __repr__(self):
        return f"war of {self.suit} against {self.hostile} : " \
               f"{self.suit if self.is_offensive else self.hostile} is offensive\n" \
               f"{self.battle}"


class Field:
    suit: str
    wars: list[War]

    def __init__(self, suit: str):
        self.suit = suit
        self.wars = []

    def __repr__(self):
        return f"war list of {self.suit} : {self.wars}"

    def search_conflict_by_hostile_suit(self, hostile_suit: str):
        for conflict in self.wars:
            if conflict.hostile == hostile_suit:
                return conflict

    def add_war(self, hostile: str, is_offensive: bool):
        self.wars.append(War(suit=self.suit, hostile=hostile, is_offensive=is_offensive,
                             battle=Battle(offensive=self.suit, defensive=hostile)))

    def del_war(self, hostile: str):
        for index, war in enumerate(self.wars):
            if war.hostile == hostile:
                self.wars.pop(index)
