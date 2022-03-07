from Definition.Card import VALID_SUIT
from Definition.Game import Game


class Setup:
    def __init__(self, game: Game):
        self._deck_makeup(game=game)
        self._distribute_king(game=game)
        self._shuffle_deck(game=game)
        self._distribute_hands(game=game)
        while not self._check_nation_can_start(game=game):
            self._make_nation_can_start(game=game)
        self._shuffle_deck(game=game)

    def _deck_makeup(self, game: Game):
        game.nature.deck.put_cards(cards=game.ideal_cards)

    def _distribute_king(self, game: Game):
        _kings = game.nature.deck.pop_by_indexes(indexes=game.nature.deck.search_by_letter(letter='K'))
        for king in _kings:
            game.search_nation_by_suit(king.suit).castle.king.put_card(card=king)

    def _shuffle_deck(self, game: Game):
        game.nature.deck.shuffle()

    def _distribute_hands(self, game: Game):
        for i in range(5):
            for suit in VALID_SUIT:
                game.search_nation_by_suit(suit=suit).castle.hands.put_cards(game.nature.deck.draw(quantity=1))

    def _check_nation_can_start(self, game: Game) -> bool:
        for suit in VALID_SUIT:
            if game.search_nation_by_suit(suit=suit).can_start_game():
                pass
            else:
                return False
        return True

    def _make_nation_can_start(self, game: Game):
        for suit in VALID_SUIT:
            nation = game.search_nation_by_suit(suit=suit)
            if not nation.can_start_game():
                _domestic_cards = nation.castle.hands.pop_by_indexes(
                    indexes=nation.castle.hands.search_by_suit(suit=nation.suit)
                )
                _abandoned = len(nation.castle.hands.cards)
                game.nature.deck.put_cards(cards=nation.castle.hands.cards)
                nation.castle.hands.cards = _domestic_cards
                nation.castle.hands.put_cards(game.nature.deck.draw(quantity=_abandoned))
