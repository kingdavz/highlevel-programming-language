#!/usr/bin/python
"""A module that can calculate the area of a rectangle"""

def rectangle(l,w):
    return l*w



if __name__=="__main__":
    l = float(input("enter length of rectangle: "))
    w = float(input("enter width of rectangle: "))
    result = rectangle(l,w)
    print(result)
