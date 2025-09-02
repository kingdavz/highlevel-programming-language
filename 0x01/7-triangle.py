#!/usr/bin/python
"""A module that implements a function that can calculate the area of a triangle, rectangle and circle"""

def triangle(b,h):
    return 0.5*b*h


if __name__=="__main__":
    b = int(input("enter the base of a triangle: "))
    h = int(input("enter height of a triangle: "))
    result = triangle(b,h)
    print(result)