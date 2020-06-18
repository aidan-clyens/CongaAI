from conga import Game


def main():
    game = Game()
    game.set_player_1("ai")
    game.set_player_2("random")

    game.run()

    game.quit()


if __name__ == '__main__':
    main()
