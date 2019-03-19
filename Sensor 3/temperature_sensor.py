#! /usr/bin/env python3
#
# intakes a list of sensor temperature readings and pulls/formats various information from it to return
#
# Author: Cody Sayer
# Version: 2.0
#
from temperature_reading import TemperatureReading
from abstract_sensor import AbstractSensor

class TemperatureSensor(AbstractSensor):

    SENSOR_DATE = 0
    SEQUENCE_NUM = 1
    SENSOR_NAME = 2
    LOWEST_TEMPERATURE = 3
    AVERAGER_TEMPERATURE = 4
    HIGHEST_TEMPERATURE = 5
    STATUS = 6

    def _load_reading_row(self, row):
        """loads a row representing a reading from the CSV file
        
        Arguments:
            row {list} -- a row representing one reading from the csv file
        """

        if len(row) != 7:
            raise ValueError('Invalid data entry')

        sensor_reading = TemperatureReading(row[TemperatureSensor.SENSOR_DATE],
                                            int(row[TemperatureSensor.SEQUENCE_NUM]),
                                            row[TemperatureSensor.SENSOR_NAME],
                                            float(row[TemperatureSensor.LOWEST_TEMPERATURE]),
                                            float(row[TemperatureSensor.AVERAGER_TEMPERATURE]),
                                            float(row[TemperatureSensor.HIGHEST_TEMPERATURE]),
                                            row[TemperatureSensor.STATUS])

        return sensor_reading
