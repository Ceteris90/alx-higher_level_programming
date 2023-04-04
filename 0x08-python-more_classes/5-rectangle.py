#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ intiatialization of rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter of rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of rectangle width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter of height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height of rectangle"""
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
        str_repr = ''
        if self.__height == 0 or self.__width == 0:
            return str_repr
        else:
            for value_1 in range(0, self.__height):
                str_repr = str_repr + "{}".format('#'*self.__width)
                if value_1 != self.__height - 1:
                    str_repr = str_repr + '\n'
            return (str_repr)

    def __repr__(self):
        """ representation """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ delete an instance """
        print("Bye rectangle...")
