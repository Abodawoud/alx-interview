#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """rotate 90 clockwise"""
    n = len(matrix)
    matrix[:] = [[matrix[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i].reverse()
