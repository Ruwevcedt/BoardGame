from Definition.Game import Game


class NewYear:
    def __call__(self, game: Game):
        self._draw_cards(game=game)

    def _draw_cards(self, game: Game):
        for suit in game.turn:
            nation = game.search_nation_by_suit(suit=suit)
            nation.castle.hands.put_cards(
                game.nature.deck.draw(
                    quantity=2 if nation.castle.cabinet.light.content[0].letter == 'Q' else 1
                )
            )
