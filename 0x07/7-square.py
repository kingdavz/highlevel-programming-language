#!/usr/bin/python
"""A module that defines a Square class with size validation"""

class Square:

    def __init__(self, size=0):
        """A method that initialize an instance attribute"""
        try:
            self.__size = size
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")
            elif self.__size < 0:
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError) as e:
            print(e)

    def area(self):
        """A method that returns the area of the square"""
        return self.__size ** 2

if __name__=="__main__":
    try:
        square = Square("a")
        print(type(square))
        print(square.__dict__)
        #print(square.__size)
    except Exception as e:
        print(e)


    square = Square(5)
    print(square.area())           

