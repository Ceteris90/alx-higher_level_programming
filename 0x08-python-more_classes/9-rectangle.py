#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty class Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ method is executed """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        str_repr = ''
        if self.__height == 0 or self.__width == 0:
            return str_repr
        else:
            sym = str(self.print_symbol)
            for i in range(0, self.__height):
                str_repr = str_repr + "{}".format(sym*self.__width)
                if i != self.__height - 1:
                    str_repr = str_repr + '\n'
            return (str_repr)

    def __repr__(self):
        """ representation """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(cls):
        """ instance """
        print("Bye rectangle...")
        cls.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ biggest rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ new rectangle instance """
        return cls(size, size)
