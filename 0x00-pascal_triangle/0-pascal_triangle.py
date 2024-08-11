#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ python implementation of pascal triangle """
    if n <= 0:
        return []
    triangle = [[1]]
    if n == 1:
        return triangle
    for i in range(n - 1):
        x = triangle[i]
        new_triangle = [1]
        for i in range(len(x) - 1):
            el = x[i] + x[i + 1]
            new_triangle.append(el)
        new_triangle.append(1)
        triangle.append(new_triangle)

    return triangle
