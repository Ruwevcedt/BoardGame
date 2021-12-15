import random

from Card import Card, ALL_LETTER, ALL_MARK


class Location:
    suit: str
    name: str
    visible_to: list[str or None]
    content: list[Card]

    def __init__(self, suit: str or None, name: str, visible_to: list[str or None], content: list[Card]):
        self.suit = suit
        self.name = name
        self.visible_to = visible_to
        self.content: list = content

    def __repr__(self):
        return f"\n{self.name} containing {self.content}"

    def search_index_of_content(self,
                                suit: list = None,
                                letter: list = None) -> list[int]:
        index = []
        if suit and letter:
            for _index, _card in enumerate(self.content):
                if _card.suit in suit and _card.letter in letter:
                    index.append(_index)
        elif (suit is None) and letter:
            for _index, _card in enumerate(self.content):
                if _card.letter in letter:
                    index.append(_index)
        elif suit and (letter is None):
            for _index, _card in enumerate(self.content):
                if _card.suit in suit:
                    index.append(_index)
        return index

    def pop_content(self, suit: list = None, letter: list = None, number_of_cards_to_pop_out: int = None) -> list[Card]:
        _ = []
        if suit or letter:
            for _enum, _index in enumerate(self.search_index_of_content(suit=suit, letter=letter)):
                _.append(self.content.pop(_index - _enum))
        else:
            _.append(self.content.pop(random.randrange(len(self.content))))
        if number_of_cards_to_pop_out:
            _ = random.shuffle(_)[:number_of_cards_to_pop_out]
            self.put_content(_[number_of_cards_to_pop_out:])
            return _
        else:
            return _

    def put_content(self, card: list[Card] or Card):
        self.content.extend(card) if type(card) == list else self.content.append(Card)

    def sum_numbers_of_content(self):
        _ = []
        for card in self.content:
            _.append(ALL_LETTER.index(card.letter))
        return sum(_)

    def minimum_number_of_content(self):
        _ = []
        for card in self.content:
            _.append(ALL_LETTER.index(card.letter))
        return min(_)

    def maximum_number_of_content(self):
        _ = []
        for card in self.content:
            _.append(ALL_LETTER.index(card.letter))
        return max(_)

    def update_visibility(self, visible_to: list[str]):
        self.visible_to = visible_to


class Camp:
    name: str
    suit: str
    enemy: str

    squads: dict[str, Location]

    def __init__(self, name: str, suit: str, enemy: str, visible_to: list[str]):
        self.name = name
        self.suit = suit
        self.enemy = enemy

        self.squads = {
            'left': Location(suit=self.suit,
                             name='left_squad' + f" of {self.suit}  against {self.enemy}",
                             visible_to=visible_to,
                             content=[]),
            'center': Location(suit=self.suit,
                               name='center_squad' + f" of {self.suit}  against {self.enemy}",
                               visible_to=visible_to,
                               content=[]),
            'right': Location(suit=self.suit,
                              name='right_squad' + f" of {self.suit}  against {self.enemy}",
                              visible_to=visible_to,
                              content=[])
        }


class Field:
    name: str

    offensive_suit: str
    defensive_suit: str

    drafted: dict[str, Location]
    hired: dict[str, int]
    arranged: dict[str, Camp]
    operative: dict[str, Camp]

    def __init__(self, name: str, offensive: str, defensive: str):
        self.name = name
        self.offensive_suit = [offensive]
        self.defensive_suit = defensive

        for _suit in [self.offensive_suit, self.defensive_suit]:
            _enemy = self.offensive_suit if _suit == self.defensive_suit else self.defensive_suit
            self.hired[_suit] = 0
            self.drafted[_suit] = Location(suit=_suit, name='drafted' + f" of {_suit}  against {_enemy}",
                                           visible_to=[None, _suit], content=[])
            self.arranged[_suit] = Camp(name='arranged' + f" of {_suit}  against {_enemy}", suit=_suit, enemy=_enemy,
                                        visible_to=[None, _suit])
            self.operative[_suit] = Camp(name='operative' + f" of {_suit}  against {_enemy}", suit=_suit, enemy=_enemy,
                                         visible_to=ALL_MARK)
