import pygame

from conga import GameBoard, GameStateMachine
from conga import window_width, window_height, cell_size, grey, black


def draw(board):
    # Draw grid
    for x in range(4):
        for y in range(4):
            rect = pygame.Rect(
                x*cell_size,
                (3-y)*cell_size,
                cell_size,
                cell_size
            )
            pygame.draw.rect(display, black, rect, 1)

            cell = board.board[x][y]
            if cell.num_stones != 0:
                text = font.render(str(cell.num_stones), False, cell.colour)
                text_pos = [
                    rect.x + int(cell_size / 8),
                    rect.y + int(cell_size / 8)
                ]
                display.blit(text, text_pos)


def run(board, game_sm):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                game_sm.update(mouse_pos)

        display.fill(grey)

        draw(board)

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
