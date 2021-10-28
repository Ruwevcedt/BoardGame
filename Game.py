from Card import AllCard
from Nation import AllNation
from Nature import Nature


class Game:
    id: int
    all_card: AllCard
    nature: Nature
    all_nation: AllNation

    def __init__(self, id: int):
        self.id = id
        self.all_card = AllCard()
        self.nature = Nature()
        self.all_nation = AllNation()

        self.generate_deck()
        self.distribute_king()
        self.shuffle_deck()
        self.distribute_hands()
        _can_start = self.check_can_start()
        while len(_can_start[False]):
            for index in _can_start[False]:
                _foreigner: list = self.all_nation[index].castle.hands.pop_content(
                    suit=self.all_nation()[index].foreign_suit)
                self.nature.deck.put_content(_foreigner)
                self.all_nation[index].castle.hands.put_content(self.nature.deck_draw(len(_foreigner)))
            _can_start = self.check_can_start()
        print(f'Game: initial hands: {[nation.castle.hands for nation in self.all_nation()]}')

    def generate_deck(self):
        print('\nGame: generating deck')
        self.nature.deck.put_content(self.all_card())
        print(f'Game: deck generated: {self.nature.deck.content}')

    def shuffle_deck(self):
        print('\nGame: shuffling deck')
        self.nature.deck_shuffle()
        print(f'Game: deck shuffled: {self.nature.deck.content}')

    def distribute_king(self):
        print('\nGame: distributing king')
        for index, nation in enumerate(self.all_nation()):
            nation.castle.king.put_content(self.nature.deck.pop_content(suit=[nation.suit], letter=['K']))
        print(f'Game: king distributed: {[nation.castle.king for nation in self.all_nation()]}')

    def distribute_hands(self):
        print('\nGame: distribute hands')
        for _turn in range(5):
            for nation in self.all_nation():
                nation.castle.hands.put_content(self.nature.deck_draw(1))
        print(f'Game: hands distributed: {[nation.castle.hands for nation in self.all_nation()]}')

    def check_can_start(self):
        _can_start = {True: [], False: []}
        for index, nation in enumerate(self.all_nation()):
            _can_start[nation.is_stable()].append(index)
        return _can_start
