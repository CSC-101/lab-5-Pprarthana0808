import data
import lab5
import unittest
from data import Time, Point
from lab5 import time_add, is_descending, largest_between, furthest_from_origin

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_one(self):
        time1 = Time(1, 30, 45)
        time2 = Time(2, 15, 20)
        result = time_add(time1, time2)
        self.assertEqual(repr(result), "Time(3, 46, 5)")

    def test_time_add_two(self):
        time1 = Time(5, 59, 59)
        time2 = Time(4, 0, 2)
        result = time_add(time1, time2)
        self.assertEqual(repr(result), "Time(10, 0, 1)")

    # Part 4
    def test_is_descending_one(self):
        self.assertTrue(is_descending([5.0, 4.5, 3.3, 2.2, 1.1]))
    def test_is_descending_two(self):
        self.assertTrue(is_descending([7.0]))

    # Part 5
    def test_largest_between_one(self):
        lst = [10, 5, 20, 15, 30, 25]
        result = largest_between(lst, 1, 4)
        self.assertEqual(result, 4)  # 30 is the largest value

    def test_largest_between_two(self):
        lst = [10, 5, 20, 15, 30, 25]
        result = largest_between(lst, 4, 1)
        self.assertIsNone(result)

    # Part 6
    def test_furthest_from_origin_one(self):
        points = [Point(1, 2), Point(3, 4), Point(-5, -6)]
        result = furthest_from_origin(points)
        self.assertEqual(result, 2)

    def test_furthest_from_origin_two(self):
        points = [Point(2, 2), Point(-2, -2)]
        result = furthest_from_origin(points)
        self.assertEqual(result, 0)





if __name__ == '__main__':
    unittest.main()
