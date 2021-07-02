from queue import PriorityQueue

from Spot import Spot
from config import *


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def set_grid(rows, width, columns, height):
    grid = []
    gap_w = width // rows
    gap_h = height // columns
    for row in range(rows):
        grid.append([])
        for column in range(columns):
            spot = Spot(row, column, gap_w, gap_h, rows, columns)
            grid[row].append(spot)
    return grid


def draw_grid(win, rows, width, columns, height):
    gap_w = width // rows
    gap_h = height // columns
    for row in range(rows):
        pygame.draw.line(win, GRAY, (0, row * gap_h), (width, row * gap_h))
    for column in range(columns):
        pygame.draw.line(win, GRAY, (column * gap_w, 0), (column * gap_w, height))


def draw(win, grid, rows, width, columns, height):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width, columns, height)
    pygame.display.update()


def get_click_pos(pos, rows, width, columns, height):
    y, x = pos
    gap_w = width // rows
    gap_h = height // columns
    row = y // gap_h
    column = x // gap_w

    return row, column


def path(drw, current, came_from):
    while current in came_from:
        current = came_from[current]
        current.set_path()
        drw()


def algorithm(drw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.position(), end.position())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            path(drw, current, came_from)
            end.set_end()
            return True

        for neighbour in current.neighbors:
            if current.x != neighbour.x and current.y != neighbour.y:
                tg_score = g_score[current] + 1.4
            else:
                tg_score = g_score[current] + 1

            if tg_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tg_score
                f_score[neighbour] = tg_score + h(neighbour.position(), end.position())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.open()

                drw()

        if current != start:
            current.close()

    return False
