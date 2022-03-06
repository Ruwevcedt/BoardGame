from Definition.Card import AllCard, VALID_MARK
from Definition.Game import Game


class Setup:
    def __call__(self, game: Game):
        self._deck_makeup(game=game)
        self._distribute_king(game=game)
        self._shuffle_deck(game=game)
        self._distribute_hands(game=game)
        while not self._check_nation_can_start(game=game):
            self._make_nation_can_start(game=game)
        self._shuffle_deck(game=game)

    def _deck_makeup(self, game: Game):
        game.nature.deck.content = AllCard().all_card

    def _distribute_king(self, game: Game):
        _kings = game.nature.deck.pop_by_indexes(indexes=game.nature.deck.search_by_letter(letter='K'))
        for king in _kings:
            game.search_nation_by_suit(king.suit).castle.king.content = [king]

    def _shuffle_deck(self, game: Game):
        game.nature.deck.shuffle()

    def _distribute_hands(self, game: Game):
        for i in range(5):
            for suit in VALID_MARK:
                game.search_nation_by_suit(suit=suit).castle.hands.put_cards(game.nature.deck.draw(quantity=1))

    def _check_nation_can_start(self, game: Game) -> bool:
        _can_start = True
        for suit in VALID_MARK:
            _can_start = _can_start and game.search_nation_by_suit(suit=suit).can_start_game()
        return _can_start

    def _make_nation_can_start(self, game: Game):
        for suit in VALID_MARK:
            nation = game.search_nation_by_suit(suit=suit)
            if not nation.can_start_game():
                _domestic_cards = nation.castle.hands.pop_by_indexes(
                    indexes=nation.castle.hands.search_by_suit(suit=nation.suit)
                )
                game.nature.deck.put_cards(cards=nation.castle.hands.content)
                nation.castle.hands.content = _domestic_cards
