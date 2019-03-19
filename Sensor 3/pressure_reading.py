#! /usr/bin/env python3
#
# intakes a list of sensor temperature readings and pulls/formats various information from it to return
#
# Author: Cody Sayer
# Version: 2.0
#
from abstract_reading import AbstractReading
import datetime


class PressureReading(AbstractReading):
    """Pressure Reading class
    """

    HIGH_PRESSURE_ERROR = "HIGH_PRESSURE"
    LOW_PRESSURE_ERROR = "LOW_PRESSURE"

    def is_error(self):
        """checks if error message is present
        
        Returns:
            boolean -- True if error message is present
        """

        if self.get_status() == 'GOOD':
            return False
        else:
            return True

    def get_error_msg(self):
        """retrieves and formats the error message
        
        Returns:
            string -- formatted error message
        """

        status_display = None
        if self.get_status() == self.HIGH_PRESSURE_ERROR:
            status_display = "High Pressure (100 kPa)"
        elif self.get_status() == self.LOW_PRESSURE_ERROR:
            status_display = "Low Pressure (0 kPa)"

        reading_datetime = datetime.datetime.strptime(self.format_datetime_string(), "%Y/%m/%d %H:%M")
        reading_display_datetime = reading_datetime.strftime('%Y/%m/%d %H:%M')

        reading_seq_num = self.get_sequence_num()

        error_msg = "%s at %s, Sequence: %d" % (status_display, reading_display_datetime, reading_seq_num)
        return error_msg
