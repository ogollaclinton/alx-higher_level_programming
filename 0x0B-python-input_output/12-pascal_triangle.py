#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        v = triangles[-1]
        tmp = [1]
        for i in range(len(v) - 1):
            tmp.append(v[i] + v[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
