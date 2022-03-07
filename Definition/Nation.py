from Castle import Castle
from Field import Field, Troop
from Location import move_card


class Nation:
    suit: str
    castle: Castle
    field: Field

    def __init__(self, suit: str):
        self.suit = suit
        self.castle.__init__(suit=self.suit)
        self.field.__init__(suit=self.suit)

    def can_start_game(self) -> bool:
        return True if len(self.castle.hands.search_by_suit(suit=self.suit)) >= 2 and \
                       len(self.castle.hands.cards) == 5 else False

    def is_it_alive(self) -> bool:
        return False if not self.castle.king else True

    def allocate_warrior_on_troop(self, index_of_warrior_in_barracks: int, troop: Troop):
        move_card(from_location=self.castle.barracks, to_location=troop,
                  from_location_index=index_of_warrior_in_barracks
                  )
