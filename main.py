import pygame
from enum import Enum

from conga import GameBoard, GameStateMachine
from conga import window_width, window_height, cell_size, white, black, grey


class State(Enum):
    CHOOSE_CELL = 1
    CHOOSE_DIRECTION = 2


prev_pos = []
current_state = State.CHOOSE_CELL


def update(game_sm, cell_pos):
    global current_state, prev_pos
    if current_state == State.CHOOSE_CELL:
        if game_sm.check_cell(cell_pos):
            current_state = State.CHOOSE_DIRECTION
            prev_pos = cell_pos
    elif current_state == State.CHOOSE_DIRECTION:
        if game_sm.check_move(prev_pos, cell_pos):
            current_state = State.CHOOSE_CELL
            move = [prev_pos, cell_pos]
            return move


def run(board, game_sm):
    running = True
    while running:
        mouse_press = False
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

        if mouse_press:
            move = update(game_sm, cell_pos)
            if move is not None:
                game_sm.update(move)

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
