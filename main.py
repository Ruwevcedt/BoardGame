from Definition.Game import Game
from Process import Setup, NewYear, CabinetReshuffle, Diplomacy

test = Game(game_id=0)
Setup.Setup(game=test)
NewYear.NewYear(game=test)