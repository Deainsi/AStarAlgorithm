from functions import *


def main(win, width, height, rows, columns):
    grid = set_grid(rows, width, columns, height)

    start = None
    end = None

    run = True

    while run:
        draw(win, grid, rows, width, columns, height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, rows, width, columns, height)
                spot = grid[row][col]

                if not start and spot != end:
                    start = spot
                    start.set_start()

                elif not end and spot != start:
                    end = spot
                    end.set_end()

                elif spot != start and spot != end:
                    spot.set_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, rows, width, columns, height)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    algorithm(lambda: draw(win, grid, rows, width, columns, height), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = set_grid(rows, width, columns, height)
    pygame.quit()


if __name__ == '__main__':
    main(WIN, WIDTH, HEIGHT, ROWS, COLUMNS)
