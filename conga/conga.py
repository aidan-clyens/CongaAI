from .constants import white, black


class Conga:
    def __init__(self):
        self.board = [[Cell() for i in range(4)] for j in range(4)]
        self.board[0][3] = Cell(white, 10)
        self.board[3][0] = Cell(black, 10)

    def move(self, src_pos, dest_pos):
        [dx, dy] = self.get_direction(src_pos, dest_pos)

        src = self.board[src_pos[0]][src_pos[1]]
        cells = self.get_middle_cells(src_pos, dest_pos)

        for cell in cells:
            cell.colour = src.colour

        if len(cells) == 1:
            cells[0].num_stones += src.num_stones
        elif len(cells) == 2:
            cells[0].num_stones += 1
            cells[1].num_stones += src.num_stones - 1
        elif len(cells) == 3:
            cells[0].num_stones += 1
            cells[1].num_stones += 2
            cells[2].num_stones += src.num_stones - 3

        src.num_stones = 0
        src.colour = None

        for cell in cells:
            if cell.num_stones == 0:
                cell.colour = None

    def get_direction(self, src_pos, dest_pos):
        dx = dest_pos[0] - src_pos[0]
        dy = dest_pos[1] - src_pos[1]

        return [dx, dy]

    def get_middle_cells(self, src_pos, dest_pos):
        [dx, dy] = self.get_direction(src_pos, dest_pos)

        cells = []
        if dx == 0:
            for i in range(1, abs(dy)):
                x = src_pos[0]
                y = src_pos[1] + i if dy > 0 else src_pos[1] - i
                cells.append(self.board[x][y])
        elif dy == 0:
            for i in range(1, abs(dx)):
                x = src_pos[0] + i if dx > 0 else src_pos[0] - i
                y = src_pos[1]
                cells.append(self.board[x][y])
        else:
            for i in range(1, abs(dx)):
                x = src_pos[0] + i if dx > 0 else src_pos[0] - i
                y = src_pos[1] + i if dy > 0 else src_pos[1] - i
                cells.append(self.board[x][y])

        cells.append(self.board[dest_pos[0]][dest_pos[1]])

        return cells


class Cell:
    def __init__(self, colour=None, num_stones=0):
        self.colour = colour
        self.num_stones = num_stones
