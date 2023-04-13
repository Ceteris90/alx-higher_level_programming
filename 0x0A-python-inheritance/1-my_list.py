#!/usr/bin/python3
"""Creates a class inheriting from the list class.
"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """Sort list ascending"""

        my_new_list = self[:]
        my_new_list.sort()
        print("{}".format(my_new_list))
