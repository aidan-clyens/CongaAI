import pygame

from .constants import cell_size, white, black


class GameBoard:
    def __init__(self):
        self.board = [[Cell() for i in range(4)] for j in range(4)]
        self.board[0][3] = Cell("white", 10)
        self.board[3][0] = Cell("black", 10)

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

    def draw(self, display, font):
        for x in range(4):
            for y in range(4):
                rect = pygame.Rect(
                    x*cell_size,
                    (3-y)*cell_size,
                    cell_size,
                    cell_size
                )
                pygame.draw.rect(display, black, rect, 1)

                cell = self.board[x][y]
                if cell.num_stones != 0:
                    if cell.colour == "white":
                        colour = white
                    else:
                        colour = black

                    text = font.render(
                        str(cell.num_stones),
                        False,
                        colour
                    )
                    text_pos = [
                        rect.x + int(cell_size / 8),
                        rect.y + int(cell_size / 8)
                    ]
                    display.blit(text, text_pos)

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

    def get_cells(self, colour):
        cells = []
        for x in range(4):
            for y in range(4):
                if self.board[x][y].colour == colour:
                    cells.append([x, y])

        return cells


class Cell:
    def __init__(self, colour=None, num_stones=0):
        self.colour = colour
        self.num_stones = num_stones
