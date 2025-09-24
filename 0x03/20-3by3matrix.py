#!/usr/bin/python
"""A module that can generate a 3 by 3 matrix"""

import random

def generate_matrix():
    matrix = []
    for _ in range(3):
        row = [random.randint(1,100) for _ in range(3)]
        matrix.append(row)
    return matrix

    
matrix = generate_matrix()
for row in matrix:
    print(row)

