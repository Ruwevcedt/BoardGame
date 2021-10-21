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
    1,
    1,
    2,
    2,
    3,
    3,
    4,
    4,
    5,
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

    location: str = ''
    observable: list[str or None] = []

    def __init__(self, suit: str or None, letter: str):
        self.suit = suit
        self.color = ALL_COLOR[ALL_MARK.index(suit)]
        self.letter = letter
        self.number = ALL_NUMBER[ALL_LETTER.index(letter)]

        self.location = 'deck'
        self.observable = []

    def __repr__(self):
        return f"{self.suit} {self.letter}"

    def update_observability(self, owner: bool = False, all: bool = False):
        if all:
            self.observable = ALL_MARK
        elif owner:
            self.observable = [None, self.suit] if self.suit else [None]
        else:
            self.observable = [None]


print('\ncard: generating a pack of card')
ALL_CARD = []  # init variable
ALL_CARD.extend([Card(None, 'Z')] * 2)  # input two joker
for suit in VALID_MARK:
    for letter in REGULAR_LETTER:
        ALL_CARD.append(Card(suit, letter))  # input all regular cards
print('card: ALL_CARD generated: ', ALL_CARD)
