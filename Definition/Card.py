ALL_MARK = [
    None,
    'spade',
    'heart',
    'diamond',
    'club',
]
VALID_MARK = ALL_MARK[1:]

ALL_COLOR = [
    None,
    'black',
    'red',
    'red',
    'black',
]
VALID_COLOR = ALL_COLOR[1:]

ALL_LETTER = [
    'Z',  # Z is joker
    'A',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
]
REGULAR_LETTER = ALL_LETTER[1:]

ALL_NUMBER = [
    None,
    None,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    None,
    None,
    None,
]
REGULAR_NUMBER = ALL_NUMBER[1:]


class Card:
    suit: str
    color: str
    letter: str
    number: int or None

    def __init__(self, suit: str or None, letter: str):
        self.suit = suit
        self.color = ALL_COLOR[ALL_MARK.index(suit)]
        self.letter = letter
        self.number = ALL_NUMBER[ALL_LETTER.index(letter)]

    def __repr__(self):
        return f"{self.suit} {self.letter}"


class AllCard:
    all_card: list[Card]

    def __init__(self):
        self.all_card = []
        self.all_card.extend([Card(None, 'Z')] * 2)
        for suit in VALID_MARK:
            for letter in REGULAR_LETTER:
                self.all_card.append(Card(suit, letter))

    def __call__(self) -> list[Card]:
        return self.all_card

    def __getitem__(self, index: int) -> Card:
        return self()[index]

    def search_by_suit(self, suit: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self()):
            _.append(ind) if card.suit == suit else False
        return _

    def search_by_color(self, color: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self()):
            _.append(ind) if card.color == color else False
        return _

    def search_by_letter(self, letter: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self()):
            _.append(ind) if card.letter == letter else False
        return _

    def search_by_number(self, number: int or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self()):
            _.append(ind) if card.number == number else False
        return _
