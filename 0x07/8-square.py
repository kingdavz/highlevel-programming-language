#!/usr/bin/python
"""A module thauses getter and setter to set private instance attribute"""


class Square:

    def __init__(self, size = 0, position = (0, 0)):
        """Initializes a new Square instance
           Args:
                size (int): size of the square
        """
        self.size = size
        self.position = position    


    @property
    def size(self):
        """
           A getter method to retrieve size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
           A setter method to set size of the square
           Args:
                size (int): size of the square side
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except Exception as e:
            print(e)

    @property
    def position(self):
        """A getter method that retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """A setter method"""
        try:
            if not isinstance(value,tuple) and len(value) == 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value
        except Exception as e:
            print(e)

    def area(self):
        """A method that returns the area of the square"""
        return self.__size ** 2
    

    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                     for _ in range(self.size,):
                        print(" " * self.position[1], "#" * self.size)
            else:
                for _ in range(self.size):
                    print( "#" * self.size)
            
    
if __name__=="__main__":
    try:
        square = Square(5, (2,2))
        square.my_print()
        print(square.area())
        print(square.size)
    except Exception as e:
        print(e)
