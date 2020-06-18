from conga import Game
import sys


def main(args):
    if len(args) < 2:
        print("Usage: python main.py 'player 1 type' 'player 2 type'")
        print("Player type: human, random, ai")
        exit()

    assert args[0] in ["human", "random", "ai"]
    assert args[1] in ["human", "random", "ai"]

    game = Game()
    game.set_player_1(args[0])
    game.set_player_2(args[1])

    game.run()

    game.quit()


if __name__ == '__main__':
    main(sys.argv[1:])
