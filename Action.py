import random

from Table.Card import ALL_SUIT, ALL_LETTER
from Table.Nation import Nation


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
        print(self.nation.castle.hands.cards)
        _input = int(input("index_of_hands: "))
        if _input > len(self.nation.castle.hands.cards):
            print('IndexError: list index out of range')
            self.select_from_hands()
        else:
            return _input

    def select_suits(self) -> list[str]:
        print(ALL_SUIT)
        _input = input("choose_suits_separate_by_space: ").split(" ")
        for char in _input:
            if char in ALL_SUIT:
                pass
            else:
                print('NoSuchElementException: no such element')
                self.select_suits()
        return _input

    def select_letters(self) -> list[str]:
        print(ALL_LETTER)
        _input = input("choose_letters_separate_by_space: ").split(" ")
        for char in _input:
            if char in ALL_LETTER:
                pass
            else:
                print('NoSuchElementException: no such element')
                self.select_letters()
        return _input
