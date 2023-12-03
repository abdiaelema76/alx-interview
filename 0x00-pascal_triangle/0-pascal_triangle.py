#!/usr/bin/python3
"""
A function that creates a pascal triangle
"""


def pascal_triangle(n):
    """
     a function that returns a list of lists of integers
     representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    # The First row
    triangle = [[1]]

    # generating subsequent rows
    for i in range(1, n):
        row = [1]  # each row in pascal triangle starts with 1
        # computing the values between the first and last 1's
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1[j]])

        row.append(1)  # each row in pascal triangle ends with 1
        triangle.append(row)
    return triangle
