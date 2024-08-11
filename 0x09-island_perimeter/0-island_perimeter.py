#!/usr/bin/python3
"""
The island perimeter problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the
    of the island
    :param: grid: nested list of ints
    :return: int: perimeter of the island
    """

    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
