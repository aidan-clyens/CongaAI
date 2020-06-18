from enum import Enum
import random
import copy
import math


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


class AIPlayer:
    def __init__(self, game_sm, colour):
        self.game_sm = game_sm
        self.colour = colour
        self.max_depth = 2

    def move(self):
        best_move = None
        max_score = -math.inf

        if self.colour == "white":
            moves = self.game_sm.white_moves
        else:
            moves = self.game_sm.black_moves

        for move in moves:
            prev_board = copy.deepcopy(self.game_sm.board.board)
            score = self.minimax(
                        move,
                        self.game_sm.get_other_player(self.colour),
                        self.max_depth
                    )
            if score > max_score:
                max_score = score
                best_move = move
            self.game_sm.board.load_board(prev_board)
            self.game_sm.current_player = self.colour
        self.game_sm.update(best_move)
        print(len(self.game_sm.black_moves), len(self.game_sm.white_moves))

    def minimax(self, move, player, depth):
        if depth == 0 or self.game_sm.get_winner() is not None:
            return self.evaluate()

        self.game_sm.update(move)

        if player == "white":
            moves = self.game_sm.white_moves
        else:
            moves = self.game_sm.black_moves

        # Maximizing
        if player == self.colour:
            max_score = -math.inf
            for move in moves:
                prev_board = copy.deepcopy(self.game_sm.board.board)
                score = self.minimax(
                    move,
                    self.game_sm.get_other_player(player),
                    depth - 1
                )
                max_score = max(max_score, score)
                self.game_sm.board.load_board(prev_board)
                self.game_sm.current_player = player
            return max_score
        # Minimizing
        else:
            min_score = math.inf
            for move in moves:
                prev_board = copy.deepcopy(self.game_sm.board.board)
                score = self.minimax(
                    move,
                    self.game_sm.get_other_player(player),
                    depth - 1
                )
                min_score = min(min_score, score)
                self.game_sm.board.load_board(prev_board)
                self.game_sm.current_player = player
            return min_score

    def evaluate(self):
        # Number of black moves: +
        # Number of white moves: -
        return len(self.game_sm.black_moves) - len(self.game_sm.white_moves)
