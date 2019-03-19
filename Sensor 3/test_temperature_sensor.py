import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open
from temperature_sensor import TemperatureSensor
from temperature_reading import TemperatureReading
from reading_stats import ReadingStats
import csv
import inspect

class TestTemperatureSensor(TestCase):
    """ Unit Tests for the TemperatureSensor Class """

    TEST_READINGS = [
        ["2018-09-23 19:56:01.345", "1", "ABC Sensor Temp M301A", "20.152", "21.367", "22.005", "OK"],
        ["2018-09-23 19:57:02.321", "1", "ABC Sensor Temp M301A", "20.163", "21.435", "22.103", "OK"],
        ["2018-09-23 19:58:01.324", "3", "ABC Sensor Temp M301A", "20.142",	"21.528", "21.803",	"OK"],
        ["2018-09-23 19:59:04.000", "4", "ABC Sensor Temp M301A", "20.212",	"21.641", "22.017",	"OK"],
        ["2018-09-23 20:00:01.453", "5", "ABC Sensor Temp M301A", "100.000", "100.000",	"100.000",	"HIGH_TEMP"],
        ["2018-09-23 20:01:01.111", "6", "ABC Sensor Temp M301A", "21.244",	"21.355", "22.103",	"OK"],
        ["2018-09-23 20:02:02.324", "7", "ABC Sensor Temp M301A", "21.112",	"22.345", "22.703",	"OK"],
        ["2018-09-23 20:03:02.744", "8", "ABC Sensor Temp M301A", "20.513", "21.745", "22.105", "OK"],
        ["2018-09-23 20:04:01.123", "9", "ABC Sensor Temp M301A", "20.333", "21.348", "21.943", "OK"],
        ["2018-09-23 20:04:01.999", "10", "ABC Sensor Temp M301A", "20.332", "21.445", "22.013", "OK"],
        ["2018-09-23 20:04:02.001", "11", "ABC Sensor Temp M301A", "-50.000", "-50.000", "-50.000", "LOW_TEMP"] ]

    # This mocks the builtin file open method in python always return '1' for the file data (we don't care
    # since we are mocking the csv reader as well.

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Creates a test fixture before each test method is run """
        self.logPoint()

        # This mocks the csv reader to return our test readings
        csv.reader = MagicMock(
            return_value=TestTemperatureSensor.TEST_READINGS)
        self.test_temperature_sensor = TemperatureSensor("testresults.csv")

    def test_temperature_sensor_readings(self):
        """ 010A - Valid Construction of the sensor """
        self.assertIsNotNone(self.test_temperature_sensor,"Test readings must be defined")

    def test_invalid_temperature_sensor_parameter(self):
        """ 010B - Invalid Construction of the sensor """

        # Must reject an undefined sensor path
        with self.assertRaises(ValueError):
            TemperatureSensor(None)

        # Must reject an empty sensor path
        with self.assertRaises(ValueError):
            TemperatureSensor("")

    def test_provide_sensor_name(self):
        """ 020A - Valid sensor name return """
        self.assertEqual(
            self.test_temperature_sensor.get_sensor_name(), "ABC Sensor Temp M301A")

    def test_get_time_period(self):
        """ 030A - Valid sensor time period return """
        self.assertEqual(self.test_temperature_sensor.get_time_period()[0], '2018/09/23 19:56')
        self.assertEqual(self.test_temperature_sensor.get_time_period()[1], '2018/09/23 20:04')

    def test_get_reading_stats(self):
        """ 040A - Valid temperature stats return """
        self.assertEqual(
            self.test_temperature_sensor.get_reading_stats().get_lowest_reading(), 20.142)
        self.assertEqual(self.test_temperature_sensor.get_reading_stats(
        ).get_average_reading(), 21.578777777777777)
        self.assertEqual(
            self.test_temperature_sensor.get_reading_stats().get_highest_reading(), 22.703)
        self.assertEqual(self.test_temperature_sensor.get_reading_stats(
        ).get_largest_reading_range(), 1.9400000000000013)

    def test_get_error_readings(self):
        """ 050A - Valid error readings return """
        self.assertEqual(self.test_temperature_sensor.get_error_messages(), ['High Temperature (100°C) at 2018/09/23 20:00, Sequence: 5','Low Temperature (-50°C) at 2018/09/23 20:04, Sequence: 11'])

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
