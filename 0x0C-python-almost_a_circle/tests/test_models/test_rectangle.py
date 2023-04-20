#!/usr/bin/python3
"""Unittest rectangle
-Test cases for the Rectangle class
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """Test Rectangle class: check for id."""

        r_0 = Rectangle(1, 2)
        self.assertEqual(r_0.id, 1)
        r_1 = Rectangle(2, 3)
        self.assertEqual(r_1.id, 2)
        r_2 = Rectangle(3, 4)
        self.assertEqual(r_2.id, 3)
        r_3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r_3.id, 12)
        r_4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r_4.id, 34)
        r_5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r_5.id, -5)
        r_6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r_6.id, 9)

    def test_2_1(self):
        """Test Rectangle class: check for attributes values."""

        r_1 = Rectangle(10, 2)
        self.assertEqual(r_1.width, 10)
        self.assertEqual(r_1.height, 2)
        self.assertEqual(r_1.x, 0)
        self.assertEqual(r_1.y, 0)
        r_2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r_2.width, 10)
        self.assertEqual(r_2.height, 2)
        self.assertEqual(r_2.x, 4)
        self.assertEqual(r_2.y, 5)

    def test_2_2(self):
        """Test class Rectangle: check for missing arguments."""

        with self.assertRaises(TypeError) as x:
            r_0 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))

        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r_1 = Rectangle()
        self.assertEqual(s, str(x.exception))

    def test_2_3(self):
        """Test class Rectangle: check for inheritance."""

        r_1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r_1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_3_0(self):
        """Test Rectangle class: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            r = Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "Foo", 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 8, 9, -65)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_4_0(self):
        """Test for public method area with normal types."""

        r_1 = Rectangle(3, 2)
        self.assertEqual(r_1.area(), 6)

        r_2 = Rectangle(75, 2)
        self.assertEqual(r_2.area(), 150)

        r_3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r_3.area(), 56)

    def test_4_1(self):
        """Test for public method area with wrong args."""

        with self.assertRaises(TypeError) as x:
            r_1 = Rectangle(3, 2)
            r_1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_5_0(self):
        """Test for public method display."""

        f = io.StringIO()
        r_1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r_1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_5_1(self):
        """Test for public method display with wrong args."""

        with self.assertRaises(TypeError) as x:
            r_1 = Rectangle(9, 6)
            r_1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_6_0(self):
        """Test for __str__ representation."""

        f = io.StringIO()
        r_1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test_7_0(self):
        """Test for public method display with x and y."""

        f = io.StringIO()
        r_1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r_1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)

    def test_8_0(self):
        """Test for public method update."""

        r_1 = Rectangle(10, 10, 10, 10)
        r_1.update(89)
        self.assertEqual(r_1.id, 89)
        r_1.update(89, 2)
        self.assertEqual(r_1.width, 2)
        r_1.update(89, 2, 3)
        self.assertEqual(r_1.height, 3)
        r_1.update(89, 2, 3, 4)
        self.assertEqual(r_1.x, 4)
        r_1.update(89, 2, 3, 4, 5)
        self.assertEqual(r_1.y, 5)
        r_1.update()
        self.assertEqual(str(r_1), "[Rectangle] (89) 4/5 - 2/3")

    def test_8_1(self):
        """Test for public method update with wrong types."""

        r_1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r_1.update("hi")
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r_1.update(65, 89, "hi")
        self.assertEqual("height must be an integer", str(x.exception))

    def test_9_0(self):
        """Test for public method update with kwargs."""

        r_1 = Rectangle(10, 10, 10, 10)
        r_1.update(height=1)
        self.assertEqual(r_1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r_1.y, 3)
        self.assertEqual(r_1.width, 4)
        self.assertEqual(r_1.x, 1)
        self.assertEqual(r_1.height, 2)

    def test_9_1(self):
        """Test for public method update with wrong types in kwargs."""

        r_1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r_1.update(id='hi')
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r_1.update(height=65, x=2, width="hi")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_13_0(self):
        """Test for public method to_dictionary."""

        r_1 = Rectangle(10, 2, 1, 9)
        r_1_dictionary = r_1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r_1_dictionary), len(r_dictionary))
        self.assertEqual(type(r_1_dictionary), dict)
        r_2 = Rectangle(1, 1)
        r_2.update(**r1_dictionary)
        r_2_dictionary = r_2.to_dictionary()
        self.assertEqual(len(r_1_dictionary), len(r_2_dictionary))
        self.assertEqual(type(r_2_dictionary), dict)
        self.assertFalse(r_1 == r_2)

    def test_13_1(self):
        """Test for public method to_dictionary with wrong args."""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r_1 = Rectangle(10, 2, 1, 9)
            r_1_dictionary = r_1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
