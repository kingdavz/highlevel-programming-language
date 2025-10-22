#!/usr/bin/python
"""A module that inherits Square class"""

ClassA = __import__("8-square").Square


class Square(ClassA):

    def __init__(self, size=0, position=(0, 0)):
        """Initializing method"""
        super().__init__(size, position)


    def __str__(self):
        """print class as string"""
        super().my_print()

if __name__ == "__main__":
    square = Square(5,(2, 2))
    print(square)