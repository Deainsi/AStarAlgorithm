
from config import *


class Spot:
    def __init__(self, row, col, width, height, total_rows, total_columns):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.color = WHITE
        self.neighbors = []
        self.height = height
        self.width = width
        self.total_rows = total_rows
        self.total_columns = total_columns

    def position(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == PURPLE

    def close(self):
        self.color = RED

    def open(self):
        self.color = GREEN

    def set_barrier(self):
        self.color = BLACK

    def set_start(self):
        self.color = YELLOW

    def set_end(self):
        self.color = PURPLE

    def set_path(self):
        self.color = MAGENTA

    def reset(self):
        self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_neighbours(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
            if self.col < self.total_columns - 1 and not grid[self.row + 1][self.col + 1].is_barrier():
                self.neighbors.append(grid[self.row + 1][self.col + 1])
            if self.col > 0 and not grid[self.row + 1][self.col - 1].is_barrier():
                self.neighbors.append(grid[self.row + 1][self.col - 1])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
            if self.col < self.total_columns - 1 and not grid[self.row - 1][self.col + 1].is_barrier():
                self.neighbors.append(grid[self.row - 1][self.col + 1])
            if self.col > 0 and not grid[self.row - 1][self.col - 1].is_barrier():
                self.neighbors.append(grid[self.row - 1][self.col - 1])

        if self.col < self.total_columns - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
