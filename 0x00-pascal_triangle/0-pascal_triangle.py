#!/usr/bin/python3
"""
  Pascal's Triangle
"""

def pascal_triangle(n):
  """
    Returns a list of lists of integers representing the Pascal's triangle of n
  """
  if n <= 0:
    return []

  triangle = []
  first_row = [1]
  second_row = [1, 1]

  triangle.append(first_row)
  triangle.append(second_row)

  for i in range(1, n - 1):
    row = [1]
    for j in range(len(triangle[i]) - 1):
      row.append(triangle[i][j] + triangle[i][j + 1])
    row.append(1)
    triangle.append(row)

  return triangle
