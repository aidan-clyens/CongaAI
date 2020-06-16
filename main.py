import pygame


white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

window_width = 600
window_height = 600

cell_size = int(window_height / 4)

display = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Conga")
clock = pygame.time.Clock()


def update():
    pass


def draw():
    # Draw grid
    for x in range(4):
        for y in range(4):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
            pygame.draw.rect(display, black, rect, 1)


def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill(white)

        update()
        draw()

        pygame.display.update()
        clock.tick(60)


def main():
    pygame.init()
    run()
    pygame.quit()


if __name__ == '__main__':
    main()
