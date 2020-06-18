class GameState:
    def __init__(self, board):
        self.board = board
        self.current_player = "black"
        self.prev_pos = []

    def update(self, move):
        if move is None:
            return
        self.board.move(move[0], move[1])
        # Change player after a successful move
        if self.current_player == "white":
            self.current_player = "black"
        elif self.current_player == "black":
            self.current_player = "white"

    def check_cell(self, src_pos):
        src = self.board.board[src_pos[0]][src_pos[1]]
        if src.colour is None or src.colour != self.current_player:
            return False

        moves = self.get_all_moves_from_src(src_pos)
        if len(moves) == 0:
            return False

        return True

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

    def check_win(self):
        return len(
            self.get_all_moves(self.get_other_player(self.current_player))
            ) == 0

    def get_all_moves(self, player):
        moves = []
        for cell in self.board.get_cells(player):
            moves += self.get_all_moves_from_src(cell)

        return moves

    def get_all_moves_from_src(self, src_pos):
        moves = []
        for x in range(4):
            for y in range(4):
                if self.check_move(src_pos, [x, y]):
                    moves.append([src_pos, [x, y]])

        return moves

    def get_other_player(self, player):
        if player == "white":
            return "black"
        else:
            return "white"
