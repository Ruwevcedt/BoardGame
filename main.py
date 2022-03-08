from Game import World, Game

test_game = Game(world=World(world_id=0))
test_game.round()

'''
while len(test_game.game.turn) > 1:
    test_game.round()
'''
