import Game
import User

test_game = Game.Game(id=0, gamers=[User.Computer(id='0'), User.Computer(id='1'), User.Computer(id='2'),
                                    User.Computer(id='3')],
                      observers=[User.User(id='4')])
test_game.proceed_a_round()
print("end")
