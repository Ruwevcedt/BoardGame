from Table.Card import Card
from Table.Location import move_card
from Table.World import World


class Diplomacy:
    world: World

    def __init__(self, world: World):
        self.world = world


