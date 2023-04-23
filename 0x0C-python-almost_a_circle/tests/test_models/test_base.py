#!/usr/bin/python3
"""unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for the Base class."""

    def test_no_arg(self):
        b_1 = Base()
        b_2 = Base()
        self.assertEqual(b_1.id, b_2.id - 1)

    def test_three_bases(self):
        b_1 = Base()
        b_2 = Base()
        b_3 = Base()
        self.assertEqual(b_1.id, b_3.id - 2)

    def test_None_id(self):
        b_1 = Base(None)
        b_2 = Base(None)
        self.assertEqual(b_1.id, b_2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b_1 = Base()
        b_2 = Base(12)
        b_3 = Base()
        self.assertEqual(b_1.id, b_3.id - 1)

    def test_id_public(self):
        b_s = Base(12)
        b_s.id = 15
        self.assertEqual(15, b_s.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            b_s = Base(12)
            print(b_s.__nb_instances)

    def test_str_id(self):
        b_s = Base("hello")
        self.assertEqual("hello", b_s.id)

    def test_float_id(self):
        b_s = Base(5.5)
        self.assertEqual(5.5, b_s.id)

    def test_complex_id(self):
        b_s = Base(complex(5))
        self.assertEqual(complex(5), b_s.id)

    def test_dict_id(self):
        b_s = Base({"a": 1, "b": 2})
        self.assertEqual({"a": 1, "b": 2}, b_s.id)

    def test_bool_id(self):
        b_s = Base(True)
        self.assertEqual(True, b_s.id)

    def test_list_id(self):
        b_s = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b_s.id)

    def test_tuple_id(self):
        b_s = Base((1, 2))
        self.assertEqual((1, 2), b_s.id)

    def test_set_id(self):
        b_s = Base({1, 2, 3})
        self.assertEqual({1, 2, 3}, b_s.id)

    def test_frozenset_id(self):
        b_s = Base(frozenset({1, 2, 3}))
        self.assertEqual(frozenset({1, 2, 3}), b_s.id)

    def test_range_id(self):
        b_s = Base(range(5))
        self.assertEqual(range(5), b_s.id)

    def test_bytes_id(self):
        b_s = Base(b'Python')
        self.assertEqual(b'Python', b_s.id)

    def test_bytearray_id(self):
        b_s = Base(bytearray(b'abcefg'))
        self.assertEqual(bytearray(b'abcefg'), b_s.id)

    def test_memoryview_id(self):
        b_s = Base(memoryview(b'abcefg'))
        self.assertEqual(memoryview(b'abcefg'), b_s.id)

    def test_inf_id(self):
        b_s = Base(float('inf'))
        self.assertEqual(float('inf'), b_s.id)

    def test_NaN_id(self):
        b_s = Base(float('nan'))
        self.assertNotEqual(float('nan'), b_s.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r_1 = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r_1.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r_1 = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r_1.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r_1 = Rectangle(2, 3, 5, 19, 2)
        r_2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r_1.to_dictionary(), r2_.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        sq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s_1 = Square(10, 2, 3, 4)
        s_2 = Square(4, 5, 21, 2)
        list_dicts = [s_1.to_dictionary(), s_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r_1])
        with open("Rectangle.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r_1 = Rectangle(10, 7, 2, 8, 5)
        r_2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r_1, r_2])
        with open("Rectangle.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 105)

    def test_save_to_file_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 39)

    def test_save_to_file_two_squares(self):
        s_1 = Square(10, 7, 2, 8)
        s_2 = Square(8, 1, 2, 3)
        Square.save_to_file([s_1, s_2])
        with open("Square.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 39)

    def test_save_to_file_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file_name:
            self.assertEqual("[]", file_name.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file_name:
            self.assertEqual("[]", file_name.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r_1 = Rectangle(3, 5, 1, 2, 7)
        r_1_dictionary = r_1.to_dictionary()
        r_2 = Rectangle.create(**r_1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r_1))

    def test_create_rectangle_new(self):
        r_1 = Rectangle(3, 5, 1, 2, 7)
        r_1_dictionary = r_1.to_dictionary()
        r_2 = Rectangle.create(**r_1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r_2))

    def test_create_rectangle_is(self):
        r_1 = Rectangle(3, 5, 1, 2, 7)
        r_1_dictionary = r_1.to_dictionary()
        r_2 = Rectangle.create(**r_1_dictionary)
        self.assertIsNot(r_1, r_2)

    def test_create_rectangle_equals(self):
        r_1 = Rectangle(3, 5, 1, 2, 7)
        r_1_dictionary = r_1.to_dictionary()
        r_2 = Rectangle.create(**r_1_dictionary)
        self.assertNotEqual(r_1, r_2)

    def test_create_square_original(self):
        s_1 = Square(3, 5, 1, 7)
        s_1_dictionary = s_1.to_dictionary()
        s_2 = Square.create(**s_1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s_1))

    def test_create_square_new(self):
        s_1 = Square(3, 5, 1, 7)
        s_1_dictionary = s_1.to_dictionary()
        s_2 = Square.create(**s_1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s_2))

    def test_create_square_is(self):
        s_1 = Square(3, 5, 1, 7)
        s_1_dictionary = s_1.to_dictionary()
        s_2 = Square.create(**s_1_dictionary)
        self.assertIsNot(s_1, s_2)

    def test_create_square_equals(self):
        s_1 = Square(3, 5, 1, 7)
        s_1_dictionary = s_1.to_dictionary()
        s_2 = Square.create(**s_1_dictionary)
        self.assertNotEqual(s_1, s_2)


class TestBase_load_from_file(unittest.TestCase):
    """load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r_1, r_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r_1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r_1, r_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r_2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r_1, r_2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(items) == Rectangle for item in output))

    def test_load_from_file_first_square(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file([s_1, s_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s_1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file([s_1, s_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s_2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file([s_1, s_2])
        output = Square.load_from_file()
        self.assertTrue(all(type(item) == Square for item in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r_1])
        with open("Rectangle.csv", "r") as file_name:
            self.assertTrue("5,10,7,2,8", file_name.read())

    def test_save_to_file_csv_two_rectangles(self):
        r_1 = Rectangle(10, 7, 2, 8, 5)
        r_2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r_1, r_2])
        with open("Rectangle.csv", "r") as file_name:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", file_name.read())

    def test_save_to_file_csv_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s_1 = Square(10, 7, 2, 8)
        s_2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s_1, s_2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r_1, r_2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r_1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r_1, r_2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r_2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r_1, r_2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(objs) == Rectangle for objs in output))

    def test_load_from_file_csv_first_square(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s_1, s_2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s_1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s_1, s_2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s_2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s_1, s_2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(objs) == Square for objs in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()
