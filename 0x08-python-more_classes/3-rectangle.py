#!/usr/bin/python3
""" Class Rectangle that define rectangle """


class Rectangle:
    """ Empty clas of a rectangle """
    def __init__(self, width=0, height=0):
        """ constructor after create an object """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ return rectangle area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ return rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Prints string representation """
        str_rep = ''
        if self.__height == 0 or self.__width == 0:
            return str_rep
        else:
            for i in range(0, self.__height):
                str_rep = str_rep + "{}".format('#'*self.__width)
                if i != self.__height - 1:
                    str_rep = str_rep + '\n'
            return (str_rep)
