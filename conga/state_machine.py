from enum import Enum

from .constants import cell_size


class State(Enum):
    CHOOSE_CELL = 1
    CHOOSE_DIRECTION = 2


class GameStateMachine:
    def __init__(self, board):
        self.board = board
        self.current_state = State.CHOOSE_CELL
        self.prev_pos = []

    def update(self, mouse_pos):
        cell_pos = [
            int(mouse_pos[0] / cell_size),
            int(4 - mouse_pos[1] / cell_size)
        ]

        if self.current_state == State.CHOOSE_CELL:
            if self.check_cell(cell_pos):
                self.current_state = State.CHOOSE_DIRECTION
                self.prev_pos = cell_pos
                print("Choose cell:", cell_pos)
        elif self.current_state == State.CHOOSE_DIRECTION:
            direction = self.get_direction(self.prev_pos, cell_pos)
            if self.check_move(direction):
                self.current_state = State.CHOOSE_CELL
                print(self.board.move(self.prev_pos, cell_pos))
                print("Choose direction:", cell_pos)

    def check_cell(self, src_pos):
        src = self.board.board[src_pos[0]][src_pos[1]]
        return src.colour is not None

    def check_move(self, direction):
        [dx, dy] = direction

        if dx != 0 and abs(dx) != 2:
            return False

        if dy != 0 and abs(dy) != 2:
            return False

        if dx == 0 and dy == 0:
            return False

        return True

    def get_direction(self, src_pos, dest_pos):
        dx = dest_pos[0] - src_pos[0]
        dy = dest_pos[1] - src_pos[1]

        return [dx, dy]
