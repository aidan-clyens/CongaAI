from enum import Enum

from .constants import cell_size


class State(Enum):
    CHOOSE_CELL = 1
    CHOOSE_DIRECTION = 2


class GameStateMachine:
    def __init__(self):
        self.current_state = State.CHOOSE_CELL
        self.prev_pos = []

    def update(self, mouse_pos):
        cell_pos = [
            int(mouse_pos[0] / cell_size),
            int(4 - mouse_pos[1] / cell_size)
        ]

        if self.current_state == State.CHOOSE_CELL:
            self.current_state = State.CHOOSE_DIRECTION
            print("Choose cell:", cell_pos)
        elif self.current_state == State.CHOOSE_DIRECTION:
            self.current_state = State.CHOOSE_CELL
            valid = self.check_move(self.prev_pos, cell_pos)
            print("Choose direction:", cell_pos)
            print("Valid:", valid)

        self.prev_pos = cell_pos

    def check_move(self, src_pos, dest_pos):
        dx = abs(src_pos[0] - dest_pos[0])
        dy = abs(src_pos[1] - dest_pos[1])

        if dx != 0 and dx != 2:
            return False

        if dy != 0 and dy != 2:
            return False

        if dx == 0 and dy == 0:
            return False

        return True
