from enum import Enum
import random


class State(Enum):
    CHOOSE_CELL = 1
    CHOOSE_DIRECTION = 2


class HumanPlayer:
    def __init__(self):
        self.prev_pos = []
        self.current_state = State.CHOOSE_CELL

    def move(self, game_sm, mouse_press, cell_pos):
        if mouse_press:
            if self.current_state == State.CHOOSE_CELL:
                if game_sm.check_cell(cell_pos):
                    self.current_state = State.CHOOSE_DIRECTION
                    self.prev_pos = cell_pos
            elif self.current_state == State.CHOOSE_DIRECTION:
                if game_sm.check_move(self.prev_pos, cell_pos):
                    self.current_state = State.CHOOSE_CELL
                    move = [self.prev_pos, cell_pos]
                    return move


class RandomPlayer:
    def move(self, game_sm):
        moves = game_sm.get_all_moves(game_sm.current_player)
        return random.choice(moves)
