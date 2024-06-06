#!/usr/bin/python3
""" The script contains a function to create a Pascal Triangle"""


def pascal_triangle(n):
    """The Pascal triangle returns a list of pascal triangle"""

    if n == 0:
        return []

    pascal_tri = [[1]]

    for i in range(1, n):
        new_row = [1]
        last_row = pascal_tri[-1]
        new_row.extend([last_row[j - 1] + last_row[j] for j in range(1, i)])
        new_row.append(1)

        pascal_tri.append(new_row)

    return pascal_tri
