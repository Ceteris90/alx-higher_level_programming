#!/usr/bin/python3
"""Create a Rectangle class, inheriting from Base.
"""
import json
from models.base import Base


class Rectangle(Base):
    """Public instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle instance.
        Args:
            - __width: rec width
            - __height: rec height
            - __x: rec position
            - __y: rec position
            - id: rec id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @width.setter
    def width(self, value):
        """width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation"""
        stg = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return stg

    def update(self, *args, **kwargs):
        """Update
        Args:
            - id
            - width
            - height
            - x
            - y
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if not isinstance(args[0], (int, None)):
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, (int, None)):
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return a dictionary representation of a Rectangle instance."""
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict

if __name__ == "__main__":
    pass
