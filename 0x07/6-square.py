#!/usr/bin/python
"""A module that creates an empty class"""

class Square:
    
    def __init__(self, size):
        """A method that initialize an instance attribute"""
        self.__size = size


if __name__ == "__main__":
    square = Square(5)
    print(type(square))
    print(square.__dict__)
    print(square.__size)