from Table.World import World


class NewYear:
    world: World

    def __init__(self, world: World):
        self.world = world

    def new_year(self):
        self._check_is_it_alive(world=self.world)
        self._draw_cards(world=self.world)

    def _downfall(self, world: World, suit: str):
        world.turn.pop(world.turn.index(suit))

    def _check_is_it_alive(self, world: World):
        for suit in world.turn:
            nation = world.search_nation_by_suit(suit=suit)
            if not nation.castle.hands.cards:
                world.nature.excepted.put_card(nation.castle.king.pop_by_index(0))
                if nation.castle.cabinet.cabinet.cards is None and nation.castle.cabinet.shadow_cabinet.cards is None:
                    self._downfall(world=world, suit=suit)
                elif nation.castle.cabinet.cabinet.cards[0].letter == 'J':
                    nation.castle.king.put_card(nation.castle.cabinet.cabinet.pop_by_index(0))
                elif nation.castle.cabinet.shadow_cabinet.cards[0].letter == 'J':
                    nation.castle.cabinet.open_cabinet()
                    nation.castle.king.put_card(nation.castle.cabinet.shadow_cabinet.pop_by_index(0))
                else:
                    self._downfall(world=world, suit=suit)

    def _draw_cards(self, world: World):
        _quantity = 0
        for suit in world.turn:
            nation = world.search_nation_by_suit(suit=suit)
            if nation.castle.cabinet.cabinet.search_by_letter(letter='Q') is not None:
                _quantity = 2
            elif nation.castle.cabinet.shadow_cabinet.search_by_letter(letter='Q') is not None:
                nation.castle.cabinet.open_cabinet()
                _quantity = 2
            else:
                _quantity = 1
            nation.castle.hands.put_cards(world.nature.deck.draw(quantity=_quantity))
