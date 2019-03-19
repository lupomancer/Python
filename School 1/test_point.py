from unittest import TestCase
from point import Point


class TestPoint(TestCase):
    """ Unit Test for the Point Class """

    def test_constructor_valid(self):
        """ TP-010A: Tests the successful creation of a Point object """

        point = Point(10, 20)
        self.assertIsNotNone(point)

    def test_constructor_invalid(self):
        """ TP-010B: Tests for failed creation of Point object """

        self.assertRaisesRegex(ValueError, "Bad X", Point, 100001, 20)
        self.assertRaisesRegex(ValueError, "Bad Y", Point, 10, 100020)

    def test_move_valid(self):
        """ TP-020A: Tests the successful move of a Point's x/y coordinates """

        point = Point(10, 20)
        self.assertIsNotNone(point)
        self.assertEqual(10, point.get_x(), "X should be 10")
        self.assertEqual(20, point.get_y(), "Y should be 20")

        point.move(50, 75)
        self.assertEqual(50, point.get_x(), "X should be 50")
        self.assertEqual(75, point.get_y(), "Y should be 75")

    def test_move_invalid(self):
        """ TP-020B: Tests for failed move of a Point object """

        point = Point(10, 20)
        self.assertIsNotNone(point)

        self.assertRaisesRegex(ValueError, "Bad X", point.move, 100001, 20)
        self.assertRaisesRegex(ValueError, "Bad Y", point.move, 10, 100020)

    def test_reset_valid(self):
        """ TP-030A: Tests the successful reset of the Point's x/y coordinates """

        point = Point(10, 20)
        self.assertIsNotNone(point)
        self.assertEqual(10, point.get_x(), "X should be 10")
        self.assertEqual(20, point.get_y(), "Y should be 20")

        point.reset()
        self.assertEqual(0, point.get_x(), "X should be 0")
        self.assertEqual(0, point.get_y(), "Y should be 0")

    def test_get_x_valid(self):
        """ TP-040A: Tests the successful retrieval of the x coordinate of a Point object """

        point = Point(11, 12)
        self.assertIsNotNone(point)
        self.assertEqual(11, point.get_x(), "X should be 11")


    def test_get_y_valid(self):
        """ TP-050A: Tests the successful retrieval of the y coordinate of a Point object """

        point = Point(11, 12)
        self.assertIsNotNone(point)
        self.assertEqual(12, point.get_y(), "Y should be 12")






