#!/usr/bin/python
"""A module that can calculate the area of a circle"""
import math

def area__of__circle(radius):
     
    if radius < 0:
        return "radius cannot be negative."
    return math.pi * radius ** 2

r = float(input("Enter the radius of the circle: "))


area = area__of__circle(r)
print(f"the area of the circle with radius {r} is: {area}")
print(f"the area of the circle with radius {r} is: {area}")
          