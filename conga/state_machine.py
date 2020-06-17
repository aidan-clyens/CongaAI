from enum import Enum

from .constants import cell_size, black, white


class State(Enum):
    CHOOSE_CELL = 1
    CHOOSE_DIRECTION = 2


class GameStateMachine:
    def __init__(self, board):
        self.board = board
        self.current_state = State.CHOOSE_CELL
        self.current_player = black
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
        elif self.current_state == State.CHOOSE_DIRECTION:
            if self.check_move(self.prev_pos, cell_pos):
                self.current_state = State.CHOOSE_CELL
                self.board.move(self.prev_pos, cell_pos)
                # Change player after a successful move
                if self.current_player == white:
                    self.current_player = black
                elif self.current_player == black:
                    self.current_player = white

    def check_cell(self, src_pos):
        src = self.board.board[src_pos[0]][src_pos[1]]
        return src.colour is not None and src.colour == self.current_player

    def check_move(self, src_pos, dest_pos):
        [dx, dy] = self.board.get_direction(src_pos, dest_pos)

        if not ((dx == 0 or dy == 0) or (abs(dx) == abs(dy))):
            return False

        if dx == 0 and dy == 0:
            return False

        cells = self.board.get_middle_cells(src_pos, dest_pos)
        src = self.board.board[src_pos[0]][src_pos[1]]

        if len(cells) > src.num_stones:
            return False

        for cell in cells:
            if cell.colour is not None and cell.colour != src.colour:
                return False

        return True
