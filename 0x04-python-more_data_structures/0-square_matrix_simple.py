#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    new_mtrx = [row.copy() for row in matrix]
    for r in range(rows):
        for c in range(cols):
            new_mtrx[r][c] = new_mtrx[r][c] ** 2
            return new_mtrx
