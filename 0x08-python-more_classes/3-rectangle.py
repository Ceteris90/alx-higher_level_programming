#!/usr/bin/python3


class Rectangle():
    """rectangle class for storing rectangle data
    """
    def __init__(self, width=0, height=0):
        """ instantiation method for object creation
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ provides __str__ method
            or print() is called
        """
        print_rect = ""
        if self.__width == 0 or self.__height == 0:
            return print_rect

        for value_1 in range(0, self.__height):
            for value_2 in range(0, self.__width):
                print_rect += '#'
            if value_1 != self.__height - 1:
                print_rect += '\n'
        return print_rect

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ gets the area of rectangle instance """
        return (self.__width * self.__height)

    def perimeter(self):
        """ gets the perimeter of a rectangle instance """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
