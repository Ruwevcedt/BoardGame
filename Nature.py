import Location


class Nature:
    deck: Location
    excepted_cards: Location

    def __init__(self):
        self.deck = Location.Location(suit=None, visibility=0, cards=[])
        self.excepted_cards = Location.Location(suit=None, visibility=0, cards=[])

    def __repr__(self):
        return f"Nature:\n\tdeck: {self.deck}\n\texcepted_cards: {self.excepted_cards}"
