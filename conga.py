import pygame


display = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Conga")
clock = pygame.time.Clock()


def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)


def main():
    pygame.init()
    run()
    pygame.quit()


if __name__ == '__main__':
    main()
