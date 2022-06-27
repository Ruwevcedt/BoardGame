ALL_SUIT = [
    None,
    'spade',
    'heart',
    'club',
    'diamond',
]
VALID_SUIT = ALL_SUIT[1:]

ALL_COLOR = [
    None,
    'black',
    'red',
    'black',
    'red',
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
        self.color = ALL_COLOR[ALL_SUIT.index(suit)]
        self.letter = letter
        self.number = ALL_NUMBER[ALL_LETTER.index(letter)]

    def __repr__(self):
        return f"{self.suit} {self.letter}"


class AllCard:
    all_card_by_suit_letter: list[Card]
    all_card_by_letter_suit: list[Card]

    def __init__(self):
        self.all_card_by_suit_letter = []
        self.all_card_by_suit_letter.extend([Card(None, 'Z')] * 2)
        for suit in VALID_SUIT:
            for letter in REGULAR_LETTER:
                self.all_card_by_suit_letter.append(Card(suit, letter))

        self.all_card_by_letter_suit = []
        self.all_card_by_letter_suit.append(Card(None, 'Z'))
        for letter in REGULAR_LETTER:
            for suit in VALID_SUIT:
                self.all_card_by_letter_suit.append(Card(suit, letter))


    def search_by_suit(self, suit: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.all_card_by_suit_letter):
            _.append(ind) if card.suit == suit else False
        return _

    def search_by_color(self, color: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.all_card_by_suit_letter):
            _.append(ind) if card.color == color else False
        return _

    def search_by_letter(self, letter: str or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.all_card_by_suit_letter):
            _.append(ind) if card.letter == letter else False
        return _

    def search_by_number(self, number: int or None) -> list[int]:
        _ = []
        for ind, card in enumerate(self.all_card_by_suit_letter):
            _.append(ind) if card.number == number else False
        return _
