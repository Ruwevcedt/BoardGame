import random

from Definition.Card import ALL_SUIT, ALL_LETTER
from Definition.Nation import Nation


class RandomAction:
    nation: Nation

    def __init__(self, nation: Nation):
        self.nation = nation

    def select_from_hands(self) -> int:
        return random.randint(len(self.nation.castle.hands.cards))

    def select_suits(self) -> list[str]:
        _ = random.randint(0, len(ALL_SUIT))
        __ = random.randint(_, len(ALL_SUIT))
        return ALL_SUIT[_:__]

    def select_letters(self) -> list[str]:
        _ = random.randint(0, len(ALL_LETTER))
        __ = random.randint(_, len(ALL_LETTER))
        return ALL_SUIT[_:__]
