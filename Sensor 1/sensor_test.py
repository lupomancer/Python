import datetime
from unittest import TestCase
from sensor_reading import SensorReading

class TestSensorReading(TestCase):

    def test_constructor(self):
        test_log = SensorReading("2018-09-23 19:56:01.345", "1", "ABC Sensor Temp M301A", "20.152", "21.367", "22.005", "OK")
        start_datetime = datetime.datetime.strptime(
            sensor_results_list[0][0], "%Y-%m-%d %H:%M:%S.%f")
