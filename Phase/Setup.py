from Table.Card import VALID_SUIT
from Table.World import World


class Setup:
    world: World

    def __init__(self, world: World):
        self.world = world

    def setup(self):
        self._deck_makeup(world=self.world)
        self._distribute_king(world=self.world)
        self._shuffle_deck(world=self.world)
        self._distribute_hands(world=self.world)
        while not self._check_nation_can_start(world=self.world):
            self._make_nation_can_start(world=self.world)

    def _deck_makeup(self, world: World):
        world.nature.deck.put_cards(cards=world.ideal_cards)

    def _distribute_king(self, world: World):
        _kings = world.nature.deck.pop_by_indexes(indexes=world.nature.deck.search_by_letter(letter='K'))
        for king in _kings:
            world.search_nation_by_suit(king.suit).castle.king.put_card(card=king)

    def _shuffle_deck(self, world: World):
        world.nature.deck.shuffle()

    def _distribute_hands(self, world: World):
        for i in range(5):
            for suit in VALID_SUIT:
                world.search_nation_by_suit(suit=suit).castle.hands.put_cards(world.nature.deck.draw(quantity=1))

    def _check_nation_can_start(self, world: World) -> bool:
        for suit in VALID_SUIT:
            if world.search_nation_by_suit(suit=suit).can_start_game():
                pass
            else:
                return False
        return True

    def _make_nation_can_start(self, world: World):
        for suit in VALID_SUIT:
            nation = world.search_nation_by_suit(suit=suit)
            if not nation.can_start_game():
                _domestic_cards = nation.castle.hands.pop_by_indexes(
                    indexes=nation.castle.hands.search_by_suit(suit=nation.suit)
                )
                _abandoned = len(nation.castle.hands.cards)
                world.nature.deck.put_cards(cards=nation.castle.hands.cards)
                nation.castle.hands.cards = _domestic_cards
                nation.castle.hands.put_cards(world.nature.deck.draw(quantity=_abandoned))
