from .constants import white, black


class Conga:
    def __init__(self):
        self.board = [[Cell() for i in range(4)] for j in range(4)]
        self.board[0][3] = Cell(white, 10)
        self.board[3][0] = Cell(black, 10)


class Cell:
    def __init__(self, colour=None, num_stones=0):
        self.colour = colour
        self.num_stones = num_stones
