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

    def __init__(self, suit: str or None, letter: str):
        self.suit = suit
        self.color = ALL_COLOR[ALL_MARK.index(suit)]
        self.letter = letter
        self.number = ALL_NUMBER[ALL_LETTER.index(letter)]

        self.location = 'deck'
        self.observable = []

    def __repr__(self):
        return f"{self.suit} {self.letter}"


class AllCard:
    all_card: list[Card]

    def __init__(self):
        print('\ncard: generating a pack of card')
        self.all_card = []
        self.all_card.extend([Card(None, 'Z')] * 2)
        for suit in VALID_MARK:
            for letter in REGULAR_LETTER:
                self.all_card.append(Card(suit, letter))
        print('card: all_card generated: ', self())

    def __call__(self) -> list[Card]:
        return self.all_card

    def __getitem__(self, index: int) -> Card:
        return self()[index]
