import pygame

from .game_board import GameBoard
from .game_state import GameState
from .constants import window_width, window_height, cell_size, grey

from agent import HumanPlayer, RandomPlayer, AIPlayer


class Game:
    def __init__(self):
        pygame.init()

        # Init game board
        self.board = GameBoard()
        self.game_sm = GameState(self.board)

        # Init pygame display
        self.display = pygame.display.set_mode([window_width, window_height])
        pygame.display.set_caption("Conga")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial Bold", 50)

    def quit(self):
        pygame.quit()

    def set_player_1(self, player_type):
        self.player_1_type = player_type

        if player_type == "human":
            self.player_1 = HumanPlayer(self.game_sm)
        elif player_type == "random":
            self.player_1 = RandomPlayer(self.game_sm)
        elif player_type == "ai":
            self.player_1 = AIPlayer(self.game_sm, "black")

    def set_player_2(self, player_type):
        self.player_2_type = player_type

        if player_type == "human":
            self.player_2 = HumanPlayer(self.game_sm)
        elif player_type == "random":
            self.player_2 = RandomPlayer(self.game_sm)
        elif player_type == "ai":
            self.player_2 = AIPlayer(self.game_sm, "white")

    def run(self):
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

            if self.game_sm.current_player == "black":
                if self.player_1_type == "human":
                    self.player_1.move(mouse_press, cell_pos)
                else:
                    self.player_1.move()
            else:
                if self.player_2_type == "human":
                    self.player_2.move(mouse_press, cell_pos)
                else:
                    self.player_2.move()

            self.display.fill(grey)
            self.board.draw(self.display, self.font)
            pygame.display.update()
            self.clock.tick(60)

            move_count += 1

            # Check win condition
            winner = self.game_sm.get_winner()
            if winner is not None:
                running = False
                print(winner, "wins in", move_count, "moves!")
