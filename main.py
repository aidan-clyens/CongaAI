import pygame

from conga import GameBoard, GameState
from conga import window_width, window_height, cell_size, white, black, grey

from agent import HumanPlayer, RandomPlayer, AIPlayer


def run(board, game_sm):
    running = True
    move_count = 0
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

        display.fill(grey)
        board.draw(display, font)

        if game_sm.current_player == "black":
            player_1.move()
        else:
            player_2.move()

        pygame.display.update()
        clock.tick(60)

        move_count += 1

        # Check win condition
        winner = game_sm.get_winner()
        if winner is not None:
            running = False
            print(winner, "wins in", move_count, "moves!")


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
    game_sm = GameState(board)

    # Init players
    global player_1
    global player_2
    player_1 = AIPlayer(game_sm, "black")
    player_2 = RandomPlayer(game_sm)

    # Run game
    run(board, game_sm)

    pygame.quit()


if __name__ == '__main__':
    main()
