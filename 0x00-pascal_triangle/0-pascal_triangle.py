#!/usr/bin/python3
"""Python volvio!"""

def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []

    triangulo = [[1]]
    for i in range(1, n):
        fila = [1]
        for j in range(1, i):
            fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
        fila.append(1)
        triangulo.append(fila)
    return triangulo
