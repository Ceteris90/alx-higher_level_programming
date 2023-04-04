#!/usr/bin/python3
"""
class Rectangle define rectangle
"""


class Rectangle():
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        instantiation method
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ provides __str__
            or print()
        """
        print_rec = ""
        if self.width == 0 or self.height == 0:
            return print_rec

        for value_1 in range(0, self.height):
            for value_2 in range(0, self.width):
                print_rec += '#'
            if value_1 != self.height - 1:
                print_rec += '\n'
        return print_rec

    def __repr__(self):
        """ provides __repr__ method
            or eval().
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ area of rectangle instance """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of a rectangle instance """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
