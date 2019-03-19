import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open
from pressure_sensor import PressureSensor
from pressure_reading import PressureReading
from reading_stats import ReadingStats
import csv
import inspect


class TestPressureSensor(TestCase):
    """ Unit Tests for the PressureSensor Class """

    TEST_READINGS = [
        ["1", "2018-09-23 19:56:01.345", "ABC Sensor Pres M100", "50.152", "51.367", "52.005", "GOOD"],
        ["2", "2018-09-23 19:57:02.321", "ABC Sensor Pres M100", "50.163", "51.435", "52.103", "GOOD"],
        ["3", "2018-09-23 19:58:01.224", "ABC Sensor Pres M100", "50.142",	"51.528", "51.803",	"GOOD"],
        ["4", "2018-09-23 19:59:03.843", "ABC Sensor Pres M100", "50.212",	"51.641", "52.017",	"GOOD"],
        ["5", "2018-09-23 20:00:01.143", "ABC Sensor Pres M100", "100", "100",	"100",	"HIGH_PRESSURE"],
        ["6", "2018-09-23 20:01:01.111", "ABC Sensor Pres M100", "51.244",	"51.355", "52.103",	"GOOD"],
        ["7", "2018-09-23 20:02:02.324", "ABC Sensor Pres M100", "51.112",	"52.345", "52.703",	"GOOD"],
        ["8", "2018-09-23 20:03:02.744", "ABC Sensor Pres M100", "50.513", "51.745", "52.105", "GOOD"],
        ["9", "2018-09-23 20:04:01.321", "ABC Sensor Pres M100", "50.333", "51.348", "51.943", "GOOD"],
        ["10", "2018-09-23 20:05:01.999", "ABC Sensor Pres M100", "50.332", "51.445", "52.013", "GOOD"],
        ["11", "2018-09-23 20:06:02.022", "ABC Sensor Pres M100", "0", "0", "0", "LOW_PRESSURE"]]

    # This mocks the builtin file open method in python always return '1' for the file data (we don't care
    # since we are mocking the csv reader as well.

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Creates a test fixture before each test method is run """
        self.logPoint()

        # This mocks the csv reader to return our test readings
        csv.reader = MagicMock(return_value=TestPressureSensor.TEST_READINGS)
        self.test_pressure_sensor = PressureSensor("testresults.csv")

    def test_pressure_sensor_readings(self):
        """ 010A - Valid Construction of the sensor """
        self.assertIsNotNone(self.test_pressure_sensor,"Test readings must be defined")

    def test_invalid_pressure_sensor_parameter(self):
        """ 010B - Invalid Construction of the sensor """

        # Must reject an undefined sensor path
        with self.assertRaises(ValueError):
            PressureSensor(None)

        # Must reject an empty sensor path
        with self.assertRaises(ValueError):
            PressureSensor("")

    def test_provide_sensor_name(self):
        """ 020A - Valid sensor name return """
        self.assertEqual(
            self.test_pressure_sensor.get_sensor_name(), "ABC Sensor Pres M100")

    def test_get_time_period(self):
        """ 030A - Valid sensor time period return """
        self.assertEqual(self.test_pressure_sensor.get_time_period()[0], '2018/09/23 19:56')
        self.assertEqual(self.test_pressure_sensor.get_time_period()[1], '2018/09/23 20:06')

    def test_get_reading_stats(self):
        """ 040A - Valid pressure stats return """
        self.assertEqual(
            self.test_pressure_sensor.get_reading_stats().get_lowest_reading(), 50.142)
        self.assertEqual(self.test_pressure_sensor.get_reading_stats(
        ).get_average_reading(), 51.57877777777777)
        self.assertEqual(
            self.test_pressure_sensor.get_reading_stats().get_highest_reading(), 52.703)
        self.assertEqual(self.test_pressure_sensor.get_reading_stats(
        ).get_largest_reading_range(), 1.9400000000000048)

    def test_get_error_readings(self):
        """ 050A - Valid error readings return """
        self.assertEqual(self.test_pressure_sensor.get_error_messages(), ['High Pressure (100 kPa) at 2018/09/23 20:00, Sequence: 5','Low Pressure (0 kPa) at 2018/09/23 20:06, Sequence: 11'])

    def tearDown(self):
        """ Prints a log point when test is finished """
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))


if __name__ == "__main__":
    unittest.main()
