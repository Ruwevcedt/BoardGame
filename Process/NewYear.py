from Definition.Game import Game
from Definition.Card import ALL_MARK

class NewYear:
    def __call__(self, game: Game):
        self._draw_cards(game=game)

    def _draw_cards(self, game: Game):
        _quantity = 0
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            if nation.castle.cabinet.light.content[0].letter == 'Q' or \
                (nation.castle.cabinet.dark.content[0].letter == 'Q' and nation.castle.cabinet.dark.visible_to == ALL_MARK):
                _quantity = 2
            else:
                _quantity = 1
            nation.castle.hands.put_cards(game.nature.deck.draw(quantity=_quantity))
