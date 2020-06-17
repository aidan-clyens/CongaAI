import pygame


pygame.init()

white = pygame.Color(255, 255, 255)
grey = pygame.Color(127, 127, 127)
black = pygame.Color(0, 0, 0)

window_width = 600
window_height = 600

cell_size = int(window_height / 4)

display = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Conga")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial Bold", 50)


class Cell:
    def __init__(self, colour=None, num_stones=0):
        self.colour = colour
        self.num_stones = num_stones


board = [[Cell() for i in range(4)] for j in range(4)]
board[0][3] = Cell(white, 10)
board[3][0] = Cell(black, 10)


def update():
    pass


def draw():
    # Draw grid
    for x in range(4):
        for y in range(4):
            rect = pygame.Rect(x*cell_size, (3-y)*cell_size, cell_size, cell_size)
            pygame.draw.rect(display, black, rect, 1)

            cell = board[x][y]
            if cell.num_stones != 0:
                text = font.render(str(cell.num_stones), False, cell.colour)
                text_pos = [rect.x + cell_size / 8, rect.y + cell_size / 8]
                display.blit(text, text_pos)


def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill(grey)

        update()
        draw()

        pygame.display.update()
        clock.tick(60)


def main():
    run()
    pygame.quit()


if __name__ == '__main__':
    main()
