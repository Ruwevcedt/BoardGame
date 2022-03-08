from Table.Card import ALL_SUIT
from Table.Location import Location, move_card


class Cabinet:
    suit: str
    cabinet: Location
    shadow_cabinet: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.cabinet = Location(suit=self.suit, name="cabinet", visible_to=ALL_SUIT, content=[])
        self.shadow_cabinet = Location(suit=self.suit, name="shadow_cabinet", visible_to=[None, self.suit], content=[])

    def __repr__(self):
        return f"cabinet of {self.suit} : \n{self.cabinet}\n{self.shadow_cabinet}"

    def initiate_visibility(self):
        self.cabinet.initiate_visibility()
        self.shadow_cabinet.initiate_visibility()

    def hide_cabinet(self):
        self.cabinet.update_visibility(visible_to=[None, self.suit])
        self.shadow_cabinet.update_visibility(visible_to=[None, self.suit])

    def open_cabinet(self):
        self.cabinet.update_visibility(visible_to=ALL_SUIT)
        self.shadow_cabinet.update_visibility(visible_to=ALL_SUIT)


class Barracks(Location):

    def __init__(self, suit: str, name="barracks"):
        super().__init__(suit=suit, name=name, visible_to=ALL_SUIT, content=[])

    def hide_barracks(self):
        self.update_visibility(visible_to=[None, self.suit])


class Castle:
    suit: str
    king: Location
    hands: Location
    cabinet: Cabinet
    barracks: Barracks

    def __init__(self, suit: str):
        self.suit = suit
        self.king = Location(suit=self.suit, name='king', visible_to=ALL_SUIT, content=[])
        self.hands = Location(suit=suit, name='hands', visible_to=[None, suit], content=[])
        self.cabinet = Cabinet(suit=self.suit)
        self.barracks = Barracks(suit=self.suit)

    def __repr__(self):
        return f"castle of {self.suit} : {self.king}\n{self.hands}\n{self.cabinet}\n{self.barracks}"

    def cabinet_appointment(self, cabinet: int or None, shadow_cabinet: int or None):
        move_card(from_location=self.hands, to_location=self.cabinet.cabinet,
                  from_location_index=cabinet
                  )
        move_card(from_location=self.hands, to_location=self.cabinet.shadow_cabinet,
                  from_location_index=shadow_cabinet
                  )

    def cabinet_resign(self):
        move_card(from_location=self.cabinet.cabinet, to_location=self.hands,
                  from_location_index=0
                  ) if self.cabinet.cabinet.cards else False
        move_card(from_location=self.cabinet.shadow_cabinet, to_location=self.hands,
                  from_location_index=0
                  ) if self.cabinet.shadow_cabinet.cards else False

    def conscription(self, index_of_warrior: int):
        move_card(from_location=self.hands, to_location=self.barracks,
                  from_location_index=index_of_warrior)
