from Definition.Game import Game


class NewYear:
    game: Game

    def __init__(self, game: Game):
        self.game = game

    def new_year(self):
        self._check_is_it_alive(game=self.game)
        self._draw_cards(game=self.game)

    def _downfall(self, game: Game, suit: str):
        game.turn.pop(game.turn.index(suit))

    def _check_is_it_alive(self, game: Game):
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            if not nation.castle.hands.cards:
                game.nature.excepted.put_card(nation.castle.king.pop_by_index(0))
                if nation.castle.cabinet.cabinet.cards is None and nation.castle.cabinet.shadow_cabinet.cards is None:
                    self._downfall(game=game, suit=suit)
                elif nation.castle.cabinet.cabinet.cards[0].letter == 'J':
                    nation.castle.king.put_card(nation.castle.cabinet.cabinet.pop_by_index(0))
                elif nation.castle.cabinet.shadow_cabinet.cards[0].letter == 'J':
                    nation.castle.cabinet.open_cabinet()
                    nation.castle.king.put_card(nation.castle.cabinet.shadow_cabinet.pop_by_index(0))
                else:
                    self._downfall(game=game, suit=suit)

    def _draw_cards(self, game: Game):
        _quantity = 0
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            if nation.castle.cabinet.cabinet.search_by_letter(letter='Q') is not None:
                _quantity = 2
            elif nation.castle.cabinet.shadow_cabinet.search_by_letter(letter='Q') is not None:
                nation.castle.cabinet.open_cabinet()
                _quantity = 2
            else:
                _quantity = 1
            nation.castle.hands.put_cards(game.nature.deck.draw(quantity=_quantity))
