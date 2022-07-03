import random

import Card
import Letter
import Location
import Nation
import Nature
import Suit
import User


class Game:
    id: int
    gamers: list[User]
    observers: list[User]

    card_pack: Location
    nature: Nature
    globe: dict[str:dict[str: User or Nation]] = {}

    turn: list[str]
    global_situation: list[list[bool]]

    def __init__(self, id: int, gamers: list[User], observers: list[User]):
        self.id = id

        random.shuffle(gamers)
        self.gamers = gamers[:4]
        self.observers = observers + gamers[4:]

        self.turn = Suit.REGULARSUIT
        self.nature = Nature.Nature()

        self.card_pack = Location.Location(suit=None, visibility=2, cards=[])
        self.card_pack.extend([Card.Card(suit=None, letter='Z')] * 2)
        for _suit in self.turn:
            self.card_pack.append(Card.Card(suit=_suit, letter='K'))
            for _letter in Letter.REGULARLETTER:
                self.card_pack.append(Card.Card(suit=_suit, letter=_letter))

        for _index, _suit in enumerate(self.turn):
            self.globe[_suit] = {"user": self.gamers[_index], "nation": Nation.Nation(suit=_suit)}
            self.globe[_suit]["nation"].king.extend(self.card_pack.search_cards(suits=[_suit], letters=['K']).copy())

        self.nature.deck.extend(
            self.card_pack.search_cards(suits=Suit.ALLSUIT, letters=['Z'] + Letter.REGULARLETTER).copy())
        random.shuffle(self.nature.deck)

        for _ in range(5):
            for _suit in self.turn:
                self._draw_card(suit=_suit, quantity=1)

        for _suit in self.turn:
            _hands = self.globe[_suit]["nation"].hands

            _count = len(_hands.search_cards(suits=[_suit], letters=Letter.ALLLETTER))
            while _count < 2:
                for _card in _hands:
                    if _card.suit != _suit:
                        self.nature.deck.append(_hands.pop(_hands.index(_card)))
                        self._draw_card(suit=_suit, quantity=1)
                _count = len(_hands.search_cards(suits=[_suit], letters=Letter.ALLLETTER))
            # print(f"suit:{_suit}\nhands:{_hands}\ncount={_count}\n")

        for _suit in self.turn:
            self._set_cabinet(suit=_suit)
            self._set_shadow_cabinet(suit=_suit)

        self._rearrange_turn()
        self.global_situation = [[False, False, False, False],
                                 [False, False, False, False],
                                 [False, False, False, False],
                                 [False, False, False, False]]

    def _coded_suit(self, suit: str) -> int:
        return Suit.REGULARSUIT.index(suit)

    def _point_target(self, suit: str) -> str:
        return Suit.REGULARSUIT[self.globe[suit]["user"].select_index_from_list(
            list=Suit.REGULARSUIT, quantity=1)[0]]

    def _make_decision(self, suit: str, contents: str = "") -> bool:
        # todo: alarm to user about contents
        return bool(self.globe[suit]["user"].select_index_from_list(list=[False, True], quantity=1)[0])

    def _draw_card(self, suit: str, quantity: int) -> None:
        self.globe[suit]["nation"].hands.extend(self.nature.deck.multiple_pop(indexes=list(range(0, quantity))))

    def _take_card(self, suit: str, target: str, quantity: int) -> None:
        _user = self.globe[suit]["user"]
        _nation = self.globe[suit]["nation"]

        _target_user = self.globe[target]["user"]
        _target_nation = self.globe[target]["nation"]

        _nation.hands.append(_target_nation.hands.multiple_pop(
            indexes=_user.select_index_from_list(
                list=list(range(0, len(_target_nation.hands))),
                quantity=quantity)))

    def _set_cabinet(self, suit: str) -> None:
        _nation = self.globe[suit]["nation"]
        _nation.cabinet_resign() if _nation.cabinet else False

        _qualified = _nation.hands.search_cards(suits=[None, suit], letters=Letter.ALLLETTER)
        _index = _nation.hands.index(
            _qualified[self.globe[suit]["user"].select_index_from_list(list=_qualified, quantity=1)[0]])

        _nation.cabinet.extend(_nation.hands.multiple_pop(indexes=[_index]))

    def _set_shadow_cabinet(self, suit: str) -> None:
        _nation = self.globe[suit]["nation"]
        _nation.shadow_cabinet_resign() if _nation.shadow_cabinet else False

        _qualified = _nation.hands.search_cards(suits=[None, suit], letters=Letter.ALLLETTER)
        _index = _nation.hands.index(
            _qualified[self.globe[suit]["user"].select_index_from_list(list=_qualified, quantity=1)[0]])

        _nation.shadow_cabinet.extend(_nation.hands.multiple_pop(indexes=[_index]))

    def _rearrange_turn(self) -> None:
        _turn = []
        _order = {_key: [] for _key in [f"{_card.suit} {_card.letter}" for _card in Card.POWERORDER]}
        for _suit in self.turn:
            _cabinet = self.globe[_suit]["nation"].cabinet[0]
            _order[f"{_cabinet.suit} {_cabinet.letter}"].append(_suit)
        for _card in Card.POWERORDER:
            random.shuffle(_order[f"{_card.suit} {_card.letter}"])
            _turn.extend(_order[f"{_card.suit} {_card.letter}"])
        self.turn = _turn

    def _is_offensive_to(self, suit: str) -> list[str]:
        _output = []
        for _index, _bool in enumerate(self.global_situation[self._coded_suit(suit=suit)]):
            _output.append(Suit.REGULARSUIT[_index]) if _bool else False
        return _output

    def _is_diffensive_to(self, suit: str) -> list[str]:
        _output = []
        suit_index = self._coded_suit(suit=suit)
        for _index, _suit in enumerate(Suit.REGULARSUIT):
            _output.append(_suit) if self.global_situation[_index][suit_index] else False
        return _output

    def proceed_a_round(self) -> None:
        # check alive
        _turn = self.turn.copy()
        for _suit in self.turn:
            _nation = self.globe[_suit]["nation"]
            if len(_nation.hands) == 0:
                if _nation.cabinet[0].letter == 'J':
                    self.nature.excepted_cards.append(_nation.king.pop(0))
                    _nation.king.append(_nation.cabinet.pop(0))

                    self._draw_card(suit=_suit, quantity=5)
                elif _nation.shadow_cabinet[0].letter == 'J':
                    _nation.shadow_cabinet.visibility = 2
                    self.nature.excepted_cards.append(_nation.king.pop(0))
                    _nation.king.append(_nation.shadow_cabinet.pop(0))
                    self._draw_card(suit=_suit, quantity=5)
                else:
                    _turn.remove(_suit)

                    _user = self.globe[_suit]["user"]
                    self.gamers.remove(_user)
                    self.observers.append(_user)
        self.turn = _turn.copy()
        # new year
        for _suit in self.turn:
            _user = self.globe[_suit]["user"]
            _nation = self.globe[_suit]["nation"]
            _cabinet = _nation.cabinet[0]
            _shadow_cabinet = _nation.shadow_cabinet[0]

            if _cabinet.letter == 'Q':
                self._draw_card(suit=_suit, quantity=2)
            elif _shadow_cabinet.letter == 'Q' and _shadow_cabinet.visibility == 1:
                _nation.shadow_cabinet.visibility = 2
                self._draw_card(suit=_suit, quantity=2)
            elif _cabinet.letter == 'A':
                self._take_card(suit=_suit, target=self._point_target(suit=_suit), quantity=1)
            elif _shadow_cabinet.letter == 'A' and _shadow_cabinet.visibility == 1:
                _nation.shadow_cabinet.visibility = 2
                self._take_card(suit=_suit, target=self._point_target(suit=_suit), quantity=1)
            else:
                self._draw_card(suit=_suit, quantity=1)
        # reshuffle cabinet
        for _suit in self.turn:
            self._set_cabinet(suit=_suit)
            self._set_shadow_cabinet(suit=_suit)
        self._rearrange_turn()
        # diplomacy
        for _suit in self.turn:
            _user = self.globe[_suit]["user"]
            _nation = self.globe[_suit]["nation"]
            _cabinet = _nation.cabinet[0]
            _shadow_cabinet = _nation.shadow_cabinet[0]

            _target_suit = self._point_target(suit=_suit)
            _target_user = self.globe[_target_suit]["user"]
            _target_nation = self.globe[_target_suit]["nation"]

            if _shadow_cabinet.letter == 'A' and self._make_decision(suit=_suit):
                _shadow_cabinet.visibility = 2
                _target_nation.shadow_cabinet.visibility = 2
                if _target_nation.shadow_cabinet.letter in ['J', 'Q', 'Z']:
                    self.nature.deck.append(_nation.shadow_cabinet.pop(0))
                else:
                    self.nature.deck.append(_target_nation.shadow_cabinet.pop(0))
                    _target_nation.shadow_cabinet.visibility = 1
            elif _shadow_cabinet.letter == 'Z' and self._make_decision(suit=_suit):
                _shadow_cabinet.visibility = 2
                _target_nation.shadow_cabinet.visibility = 2
                if _target_nation.shadow_cabinet.letter == 'Z':
                    self.nature.deck.append(_nation.shadow_cabinet.pop(0))
                else:
                    self.nature.deck.append(_target_nation.shadow_cabinet.pop(0))
                    _target_nation.shadow_cabinet.visibility = 1
            elif self._make_decision(suit=_suit):
                pass
            else:
                for _iter in range(2):
                    _suggestion = _user.select_index_from_list(
                        list=self.card_pack,
                        quantity=_user.select_index_from_list(
                            list=list(range(1, len(_nation.hands))),
                            quantity=1
                        )[0] + 1
                    )
                    _response = _target_user.select_index_from_list(
                        list=self.card_pack,
                        quantity=_target_user.select_index_from_list(
                            list=list(range(0, len(_suggestion))),
                            quantity=1
                        )[0] + 1
                    )
                if self._make_decision(suit=_suit) and self._make_decision(suit=_target_suit):
                    _target_nation.hands.extend(
                        _nation.hands.multiple_pop(_user.select_index_from_list(list=_nation.hands, quantity=1)))
        # collision
        for _suit in self.turn:
            if self._make_decision(suit=_suit):
                _target_suit = self._point_target(suit=_suit)
                while _target_suit in self._is_diffensive_to(suit=_suit):
                    _target_suit = self._point_target(suit=_suit)

                _target_nation = self.globe[_target_suit]["nation"]
                if _target_nation.hands.search_cards(suits=[_suit], letters=Letter.ALLLETTER):
                    _target_user = self.globe[_target_suit]["user"]

                    if _target_nation.shadow_cabinet[0].letter == 'A' and _target_nation.shadow_cabinet.visibility == 1:
                        _target_nation.shadow_cabinet.visibility = 2
                    elif _target_nation.shadow_cabinet[
                        0].letter == 'Z' and _target_nation.shadow_cabinet.visibility == 1:
                        _target_nation.shadow_cabinet.visibility = 2
                        self._take_card(suit=_target_suit, target=_suit, quantity=1)
                    elif self._make_decision(suit=_target_suit):
                        _target_user = self.globe[_target_suit]["user"]
                        self._take_card(suit=_suit, target=_target_suit, quantity=1)
                    else:
                        self.global_situation[self._coded_suit(suit=_suit)][self._coded_suit(suit=_target_suit)] = True
        # war
        for _suit in self.turn:
