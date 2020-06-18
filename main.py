import pygame

from conga import GameBoard, GameStateMachine
from conga import window_width, window_height, cell_size, grey


def run(board, game_sm):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                cell_pos = [
                    int(mouse_pos[0] / cell_size),
                    int(4 - mouse_pos[1] / cell_size)
                ]
                game_sm.update(cell_pos)

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

    # Run game
    run(board, game_sm)

    pygame.quit()


if __name__ == '__main__':
    main()
