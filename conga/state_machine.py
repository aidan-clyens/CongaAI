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
            # direction = self.get_direction(self.prev_pos, cell_pos)
            if self.check_move(self.prev_pos, cell_pos):
                self.current_state = State.CHOOSE_CELL
                print(self.board.move(self.prev_pos, cell_pos))
                print("Choose direction:", cell_pos)

    def check_cell(self, src_pos):
        src = self.board.board[src_pos[0]][src_pos[1]]
        return src.colour is not None

    def check_move(self, src_pos, dest_pos):
        [dx, dy] = self.get_direction(src_pos, dest_pos)

        if dx != 0 and abs(dx) != 2:
            return False

        if dy != 0 and abs(dy) != 2:
            return False

        if dx == 0 and dy == 0:
            return False

        middle_pos = [src_pos[0] + int(dx / 2), src_pos[1] + int(dy / 2)]
        src = self.board.board[src_pos[0]][src_pos[1]]
        middle = self.board.board[middle_pos[0]][middle_pos[1]]
        dest = self.board.board[dest_pos[0]][dest_pos[1]]

        if middle.colour is not None and middle.colour != src.colour:
            return False

        if dest.colour is not None and dest.colour != src.colour:
            return False

        return True

    def get_direction(self, src_pos, dest_pos):
        dx = dest_pos[0] - src_pos[0]
        dy = dest_pos[1] - src_pos[1]

        return [dx, dy]
