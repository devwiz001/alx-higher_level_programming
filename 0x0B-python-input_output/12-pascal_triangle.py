#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate.

    Returns:
    - list: A list of lists representing Pascal's triangle.
            Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # First element in every row is 1
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # Last element in every row is 1
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    for row in pascal_triangle(5):
        print(row)
