from Definition.Card import ALL_SUIT
from Definition.Location import Location, move_card


class Hands(Location):

    def __init__(self, suit: str, name="hands"):
        super().__init__(suit=suit, name=name, visible_to=[None, suit], content=[])


class Cabinet:
    suit: str
    cabinet: Location
    shadow_cabinet: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.cabinet = Location(suit=self.suit, name="cabinet.light", visible_to=ALL_SUIT, content=[])
        self.shadow_cabinet = Location(suit=self.suit, name="cabinet.dark", visible_to=[None, self.suit], content=[])

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
    hands: Hands
    cabinet: Cabinet
    barracks: Barracks

    def __init__(self, suit: str):
        self.suit = suit
        self.king = Location(suit=self.suit, name='king', visible_to=ALL_SUIT, content=[])
        self.hands = Hands(suit=self.suit)
        self.cabinet = Cabinet(suit=self.suit)
        self.barracks = Barracks(suit=self.suit)

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
                  )
        move_card(from_location=self.cabinet.shadow_cabinet, to_location=self.hands,
                  from_location_index=0
                  )

    def conscription(self, index_of_warrior: int):
        move_card(from_location=self.hands, to_location=self.barracks,
                  from_location_index=index_of_warrior)
