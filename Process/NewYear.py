from Definition.Card import ALL_MARK
from Definition.Game import Game


class NewYear:
    def __call__(self, game: Game):
        self._check_is_it_alive(game=game)
        self._draw_cards(game=game)

    def _downfall(self, game: Game):
        for index, suit in enumerate(game.turn):
            False if game.search_nation_by_suit(suit=suit).is_it_alive() else game.turn.pop(index)

    def _check_is_it_alive(self, game: Game):
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            if not nation.castle.hands.cards:
                _dead_king = nation.castle.king.cards.pop(0)
                game.nature.excepted.cards.extend([_dead_king])
                if not nation.castle.cabinet.cabinet.cards and not nation.castle.cabinet.shadow_cabinet:
                    self._downfall(game=game)
                elif nation.castle.cabinet.cabinet.cards[0].letter == 'J':
                    nation.castle.king.put_cards([nation.castle.cabinet.cabinet.cards.pop(0)])
                elif nation.castle.cabinet.shadow_cabinet.cards[0].letter == 'J':
                    nation.castle.cabinet.open_cabinet()
                    nation.castle.king.put_cards([nation.castle.cabinet.shadow_cabinet.cards.pop(0)])
                    nation.castle.cabinet.visibility_initiation()
                else:
                    self._downfall(game=game)

    def _draw_cards(self, game: Game):
        _quantity = 0
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            if nation.castle.cabinet.cabinet.cards[0].letter == 'Q':
                _quantity = 2
            elif nation.castle.cabinet.shadow_cabinet.cards[0].letter == 'Q':
                nation.castle.cabinet.open_cabinet()
                _quantity = 2
            else:
                _quantity = 1
            nation.castle.hands.put_cards(game.nature.deck.draw(quantity=_quantity))
