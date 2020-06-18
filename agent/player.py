from enum import Enum
import random


class State(Enum):
    CHOOSE_CELL = 1
    CHOOSE_DIRECTION = 2


class HumanPlayer:
    def __init__(self, game_sm):
        self.game_sm = game_sm
        self.prev_pos = []
        self.current_state = State.CHOOSE_CELL

    def move(self, mouse_press, cell_pos):
        if mouse_press:
            if self.current_state == State.CHOOSE_CELL:
                if self.game_sm.check_cell(cell_pos):
                    self.current_state = State.CHOOSE_DIRECTION
                    self.prev_pos = cell_pos
            elif self.current_state == State.CHOOSE_DIRECTION:
                if self.game_sm.check_move(self.prev_pos, cell_pos):
                    self.current_state = State.CHOOSE_CELL
                    move = [self.prev_pos, cell_pos]
                    self.game_sm.update(move)


class RandomPlayer:
    def __init__(self, game_sm):
        random.seed()
        self.game_sm = game_sm

    def move(self):
        moves = self.game_sm.get_all_moves(self.game_sm.current_player)
        move = random.choice(moves)
        self.game_sm.update(move)
