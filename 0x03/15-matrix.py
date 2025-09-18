#!/usr/bin/python
"""A module that adds two 2-dimensional matrixes together"""

def add_matrices(matrix1 , matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            sum_value = matrix1[i][j] + matrix2[i][j]
            row.append(sum_value)
        result.append(row)

    return result
A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]
result = add_matrices(A,B)
print(result)