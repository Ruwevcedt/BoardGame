import random

from Definition.Card import ALL_SUIT, ALL_LETTER
from Definition.Nation import Nation


class RandomAction:
    nation: Nation

    def __init__(self, nation: Nation):
        self.nation = nation

    def select_from_hands(self) -> int:
        return random.randint(0, len(self.nation.castle.hands.cards) - 1)

    def select_suits(self) -> list[str]:
        _quantity = random.randint(0, len(ALL_SUIT) - 1)
        _ = []
        for i in range(_quantity):
            _.append(random.choice(ALL_SUIT))
        _.sort(key=ALL_SUIT)
        return _

    def select_letters(self) -> list[str]:
        _quantity = random.randint(0, len(ALL_LETTER) - 1)
        _ = []
        for i in range(_quantity):
            _.append(random.choice(ALL_LETTER))
        _.sort(key=ALL_LETTER)
        return _


class Action:
    nation: Nation

    def __init__(self, nation: Nation):
        self.nation = nation

    def select_from_hands(self) -> int:
        _input = int(input("index_of_the_card_of_your_hands: "))
        if _input > len(self.nation.castle.hands.cards):
            print('over length')
            self.select_from_hands()
        else:
            return _input

    def select_suits(self) -> list[str]:
        _input = input("choose_suits_separate_by_space: ").split(" ")
        for char in _input:
            if char in ALL_SUIT:
                pass
            else:
                print("there is no such suit")
                self.select_suits()
        return _input

    def select_letters(self) -> list[str]:
        _input = input("choose_letters_separate_by_space: ").split(" ")
        for char in _input:
            if char in ALL_LETTER:
                pass
            else:
                print("there is no such letter")
                self.select_letters()
        return _input
