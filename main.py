from Definition.Game import Game
from Phase import Setup, NewYear, CabinetReshuffle, Diplomacy

test = Game(game_id=0)
Setup.Setup(game=test).setup()
NewYear.NewYear(game=test).new_year()
print('\n')
CabinetReshuffle.CabinetReshuffle(game=test).cabinet_reshuffle()
Diplomacy.Diplomacy(game=test)
print('\n')