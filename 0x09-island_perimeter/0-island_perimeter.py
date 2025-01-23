#!/usr/bin/python3
"""Island Perimeter mandatory."""


def test0(n):
    """
    Determine the opposite value of the given number.

    Args:
        n (int): A number in the grid (0 or 1).

    Returns:
        int: 0 if n is 1, or 1 if n is 0.
    """
    return 1 if n == 0 else 0


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A list of integers where:
            - 0 represents water
            - 1 represents land
            - Each cell is square, with a side length of 1.
            - Cells are connected horizontally/vertically (not diagonally).
            - The grid is rectangular, with width and height not exceeding 100.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
  
    # Validate grid dimensions
    assert (1 <= rows <= 100 and 1 <= cols <= 100), "length must be between 1 an 100"

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            # Validate grid values
            assert grid[i][j] in (0, 1), "Grid values must be either 0 or 1"

            if grid[i][j] == 1:
                # Check top neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check left neighbor
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
