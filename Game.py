from Card import AllCard, Card
from Location import Field
from Nation import AllNation, Nation
from Nature import Nature


class Game:
    id: int
    all_card: AllCard
    nature: Nature
    all_nation: AllNation
    all_war: list[Field]

    def __init__(self, id: int):
        self.id = id
        self.all_card = AllCard()
        self.nature = Nature()
        self.all_nation = AllNation()

        self._generate_deck()
        self._distribute_king()
        self.shuffle_deck()
        self._distribute_hands()
        _can_start = self._check_can_start()
        while len(_can_start[False]):
            for index in _can_start[False]:
                _foreigner: list = self.all_nation[index].castle.hands.pop_content(
                    suit=self.all_nation()[index].foreign_suit)
                self.nature.deck.put_content(_foreigner)
                self.all_nation[index].castle.hands.put_content(self.nature.deck_draw(len(_foreigner)))
            _can_start = self._check_can_start()
        print(f'Game: initial hands: {[nation.castle.hands for nation in self.all_nation()]}')

    def _generate_deck(self):
        print('\nGame: generating deck')
        self.nature.deck.put_content(self.all_card())
        print(f'Game: deck generated: {self.nature.deck.content}')

    def shuffle_deck(self):
        print('\nGame: shuffling deck')
        self.nature.deck_shuffle()
        print(f'Game: deck shuffled: {self.nature.deck.content}')

    def _distribute_king(self):
        print('\nGame: distributing king')
        for nation in self.all_nation():
            nation.castle.king.put_content(self.nature.deck.pop_content(suit=[nation.suit], letter=['K']))
        print(f'Game: king distributed: {[nation.castle.king for nation in self.all_nation()]}')

    def _distribute_hands(self):
        print('\nGame: distribute hands')
        for _turn in range(5):
            for nation in self.all_nation():
                self.draw(nation)
        print(f'Game: hands distributed: {[nation.castle.hands for nation in self.all_nation()]}')

    def _check_can_start(self):
        _can_start = {True: [], False: []}
        for index, nation in enumerate(self.all_nation()):
            _can_start[nation.is_stable()].append(index)
        return _can_start

    def draw(self, nation: Nation):
        nation.castle.hands.put_content(self.nature.deck_draw(1))

    def set_cabinet(self, nation: Nation, visible_cabinet: Card or None, invisible_cabinet: Card or None):
        _temp_visible_cabinet, _temp_invisible_cabinet = \
            nation.castle.visible_cabinet.pop_content(number_of_cards_to_pop_out=1), \
            nation.castle.invisible_cabinet.pop_content(number_of_cards_to_pop_out=1)
        nation.castle.hands.put_content([_temp_visible_cabinet, _temp_invisible_cabinet])

        nation.castle.visible_cabinet.put_content(visible_cabinet)
        nation.castle.invisible_cabinet.put_content(invisible_cabinet)

    def open_war(self, offensive_nation: Nation, defensive_nation: Nation):
        war_field = Field(
            name=f"war from {offensive_nation.suit} to {defensive_nation.suit}",
            offensive=offensive_nation.suit,
            defensive=defensive_nation.suit
        )
        offensive_nation.open_war(war_field)
        defensive_nation.open_war(war_field)
        self.all_war.append(war_field)

    def draft_army(self, nation: Nation, card: Card):

    def hire_mercenary(self, nation: Nation):
        _card: Card = self.nature.deck_draw(number=1)
        if _card.number is None:
            self.nature.back_to_deck(card=_card)
        else:



    def close_war(self, war: Field):
        _offensive_nation: str = war.offensive_suit
        _defensive_nation: str = war.defensive_suit

        self.all_nation(suit=_offensive_nation)\
            .close_war(with_nation=_defensive_nation)
        self.all_nation(suit=_defensive_nation)\
            .close_war(with_nation=_offensive_nation)
        self.all_war.remove(war)