#!/usr/bin/python3
"""Solving N Queens with Backtracking"""
import sys


def nqueens(n, y, board):
    """
    Method: nqueens - place n queens
            on an n by n board so that
            no queens are attacking any
            others.
    Parameters: n is an int that sets
                board size and # of queens
    Return: All possible solutions to
            placement, in list of lists form
    """
    for x in range(n):
        hold = 0
        # Check if the current position (y, x) is safe
        for q in board:
            if x == q[1] or y - x == q[0] - q[1] or x - q[1] == q[0] - y:
                hold = 1
                break
        if hold == 0:
            board.append([y, x])  # Place the queen
            if y != n - 1:  # If not the last row, keep searching
                nqueens(n, y + 1, board)
            else:  # If last row, print the solution
                print([[r[1] for r in board] for board in [board]])
            del board[-1]  # Remove the queen for backtracking


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n, 0, [])


if __name__ == '__main__':
    main()
