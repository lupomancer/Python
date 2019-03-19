#! /usr/bin/env python3
#
# intakes a list of sensor temperature readings and pulls/formats various information from it to return
#
# Author: Cody Sayer
# Version: 2.0
#
from pressure_reading import PressureReading
from abstract_sensor import AbstractSensor


class PressureSensor(AbstractSensor):
    """loads a row from the file and formats it for common use
    
    Arguments:
        AbstractSensor {input line} -- single line of read file
    
    Raises:
        ValueError -- if the line reading is not of correct length
    
    Returns:
        PressureReading -- instance of PressureReading
    """

    SEQUENCE_NUM = 0
    SENSOR_DATE = 1
    SENSOR_NAME = 2
    LOWEST_PRESSURE = 3
    AVERAGER_PRESSURE = 4
    HIGHEST_PRESSURE = 5
    STATUS = 6

    def _load_reading_row(self, row):
        """loads a row representing a reading from the CSV file
        
        Arguments:
            row {list} -- a row representing one reading from the csv file
        """

        if len(row) != 7:
            raise ValueError('Invalid data entry')

        sensor_reading = PressureReading(row[PressureSensor.SENSOR_DATE],
                                            int(row[PressureSensor.SEQUENCE_NUM]),
                                            row[PressureSensor.SENSOR_NAME],
                                            float(row[PressureSensor.LOWEST_PRESSURE]),
                                            float(row[PressureSensor.AVERAGER_PRESSURE]),
                                            float(row[PressureSensor.HIGHEST_PRESSURE]),
                                            row[PressureSensor.STATUS])

        return sensor_reading
