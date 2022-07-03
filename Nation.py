import Location


class Nation:
    suit: str

    king: Location
    hands: Location
    cabinet: Location
    shadow_cabinet: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.king = Location.Location(suit=self.suit, visibility=2, cards=[])
        self.hands = Location.Location(suit=self.suit, visibility=1, cards=[])
        self.cabinet = Location.Location(suit=self.suit, visibility=2, cards=[])
        self.shadow_cabinet = Location.Location(suit=self.suit, visibility=1, cards=[])

    def __repr__(self):
        return f"Nation: {self.suit}\n\thands: {self.hands}\n\tcabinet: {self.cabinet}\n\tshadow_cabinet: {self.shadow_cabinet}"

    def cabinet_resign(self) -> None:
        self.hands.append(self.cabinet.pop(0))

    def shadow_cabinet_resign(self) -> None:
        self.hands.append(self.shadow_cabinet.pop(0))
        self.cabinet.visibility = 1
