#!/usr/bin/python3
""" class Rectangle define the rectangle """


class Rectangle():
    """
    class Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        contructor
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        perimeter of the rectangle
        """
        if (self.__width == 0 & self.__height == 0):
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))
