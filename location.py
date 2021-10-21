import random

from card import Card, ALL_LETTER, VALID_MARK


class Location:
    suit: str
    name: str
    content: list[Card]

    def __init__(self, suit: str or None, name: str, content: list[Card]):
        self.suit = suit
        self.name = name
        self.content: list = content

    def __repr__(self):
        return f"\n{self.name}  containing {self.content}"

    def search_card(self, suit: list = None,
                    letter: list = None,
                    card: Card = None,
                    show_card: bool = False) -> dict[str, list]:
        index = []
        cards = []
        if card:
            return {'index': [self.content.index(card)], 'cards': [card]}
        elif suit and letter:
            for _index, _card in enumerate(self.content):
                if _card.suit in suit and _card.letter in letter:
                    index.append(_index)
                    cards.append(_card) if show_card else False
        elif (suit is None) and letter:
            for _index, _card in enumerate(self.content):
                if _card.letter in letter:
                    index.append(_index)
                    cards.append(_card) if show_card else False
        elif suit and (letter is None):
            for _index, _card in enumerate(self.content):
                if _card.suit in suit:
                    index.append(_index)
                    cards.append(_card) if show_card else False
        return {'index': index, 'cards': cards} if show_card else {'index': index}

    def pop_random_card(self):
        return self.content.pop(random.randrange(len(self.content)))

    def show_citizen(self):
        return self.search_card(suit=[self.suit], show_card=True)['cards']

    def show_foreigner(self):
        _ = []
        for card in self.content:
            _.append(card) if card.suit != self.suit else False
        return _

    def minimum_number(self):
        _ = []
        for card in self.content:
            _.append(ALL_LETTER.index(card.letter))
        return min(_)

    def update_location_visible_to(self, owner: bool = False, all: bool = False):
        for card in self.content:
            card.location = self.name
            card.update_observability(owner, all)


class Nature:
    deck: Location
    excepted: Location

    def __init__(self):
        self.deck = Location(None, 'deck', [])
        self.excepted = Location(None, 'excepted', [])

    def __repr__(self):
        return f"MOTHER NATURE\ndeck:   {self.deck.content}\nexcepted:  {self.excepted.content}"

    def initiate_observability(self):
        self.deck.update_location_visible_to()
        self.excepted.update_location_visible_to(all=True)

    def deck_shuffle(self):
        random.shuffle(self.deck.content)

    def deck_draw(self, number: int = 0):
        _ = self.deck.content[:number]
        self.deck.content = self.deck.content[number:]
        return _


class Castle:
    suit: str
    king: Location
    visible_cabinet: Location
    invisible_cabinet: Location
    hands: Location
    drafted: Location

    def __init__(self, suit: str):
        self.suit = suit
        self.king = Location(self.suit, 'king' + f"     of {self.suit}", [])
        self.visible_cabinet = Location(self.suit, 'visible_cabinet' + f"   of {self.suit}", [])
        self.invisible_cabinet = Location(self.suit, 'invisible_cabinet' + f"   of {self.suit}", [])
        self.hands = Location(self.suit, 'hands' + f"   of {self.suit}", [])
        self.drafted = Location(self.suit, 'draft' + f"     of {self.suit}", [])

    def initiate_observability(self):
        self.king.update_location_visible_to(all=True)
        self.visible_cabinet.update_location_visible_to(all=True)
        self.invisible_cabinet.update_location_visible_to(owner=True)
        self.hands.update_location_visible_to(owner=True)
        self.drafted.update_location_visible_to(all=True)


class Camp:
    name: str
    suit: str
    enemy: str

    left_corp: Location
    center_corp: Location
    right_corp: Location

    def __init__(self, name: str, suit: str, enemy: str):
        self.name = name
        self.suit = suit
        self.enemy = enemy

        self.left_corp = Location(self.suit, 'left_corp' + f"   of {self.suit}  against {self.enemy}", [])
        self.center_corp = Location(self.suit, 'center_corp' + f"   of {self.suit}  against {self.enemy}", [])
        self.right_corp = Location(self.suit, 'right_corp' + f"     of {self.suit}  against {self.enemy}", [])

    def update_observability(self, owner=False, all=False):
        self.left_corp.update_location_visible_to(owner=owner, all=all)
        self.center_corp.update_location_visible_to(owner=owner, all=all)
        self.right_corp.update_location_visible_to(owner=owner, all=all)


class Field:
    name: str
    suit: str
    enemy: str

    drafted: Location
    arranged: Camp
    operative: Camp

    def __init__(self, name: str, suit: str, enemy: str):
        self.name = name
        self.suit = suit
        self.enemy = enemy

        self.drafted = Location(self.suit, 'drafted' + f"   of {self.suit}  against {self.enemy}", [])
        for _suit in VALID_MARK:
            if _suit != self.suit:
                self.arranged = Camp('arranged' + f"    of {self.suit}  against {self.enemy}", self.suit, _suit)
                self.operative = Camp('operative' + f"  of {self.suit}  against {self.enemy}", self.suit, _suit)

    def initiate_observability(self):
        self.drafted.update_location_visible_to(owner=True)
        self.arranged.update_observability(owner=True)
        self.operative.update_observability(all=True)


class Nation:
    suit: str
    castle: Castle
    war: dict[str, Field]

    def __init__(self, suit: str):
        self.suit = suit
        self.castle = Castle(suit=self.suit)

        self.war = {}
        for _suit in VALID_MARK:
            if _suit != self.suit:
                self.war[_suit] = Field('war' + f" of {self.suit} with {_suit}", self.suit, _suit)

    def __repr__(self):
        return f"nation of {self.suit}"

    def is_stable(self):
        return True if len(self.castle.hands.search_card(suit=[self.suit])['index']) >= 2 else False


print('\nlocation: generating nature')
NATURE = Nature()
print('location: NATURE generated: ', NATURE)

print('\nlocation: generating all nation')
ALL_NATION = []
for suit in VALID_MARK:
    ALL_NATION.append(Nation(suit))
print('location: ALL_NATION generated: ', ALL_NATION)
