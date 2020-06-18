import pygame

from conga import GameBoard, GameStateMachine
from conga import window_width, window_height, cell_size, white, black, grey

from agent import HumanPlayer, RandomPlayer


def run(board, game_sm):
    running = True
    while running:
        mouse_press = False
        cell_pos = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                mouse_press = True
                cell_pos = [
                    int(mouse_pos[0] / cell_size),
                    int(4 - mouse_pos[1] / cell_size)
                ]

        if game_sm.current_player == black:
            move = player_1.move(mouse_press, cell_pos)
            game_sm.update(move)
        else:
            move = player_2.move()
            game_sm.update(move)

        # Check win condition
        if game_sm.check_win():
            running = False
            print(game_sm.current_player, "wins!")

        display.fill(grey)
        board.draw(display, font)

        pygame.display.update()
        clock.tick(60)


def main():
    pygame.init()

    global display
    global clock
    global font

    # Init pygame display
    display = pygame.display.set_mode([window_width, window_height])
    pygame.display.set_caption("Conga")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial Bold", 50)

    # Init game board
    board = GameBoard()
    game_sm = GameStateMachine(board)

    # Init players
    global player_1
    global player_2
    player_1 = HumanPlayer(game_sm)
    player_2 = RandomPlayer(game_sm)

    # Run game
    run(board, game_sm)

    pygame.quit()


if __name__ == '__main__':
    main()
