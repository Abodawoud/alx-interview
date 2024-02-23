#!/usr/bin/python3
"""Rotate a 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix: list):
    """rotate 90 clockwise"""
    n = len(matrix)
    matrix[:] = [[matrix[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i].reverse()
