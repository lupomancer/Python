#! /usr/bin/env python3
#
# intakes a list of sensor temperature readings and pulls/formats various information from it to return
#
# Author: Cody Sayer
# Version: 2.0
#
from abstract_reading import AbstractReading
import datetime


class TemperatureReading(AbstractReading):
    """Temperature sensor class
    """

    HIGH_TEMP_ERROR = "HIGH_TEMP"
    LOW_TEMP_ERROR = "LOW_TEMP"

    def is_error(self):
        """checks if an error is present
        
        Returns:
            boolean -- True if error is present
        """

        if self.get_status() == 'OK':
            return False
        else:
            return True

    def get_error_msg(self):
        """retrieves and returns a formatted error message if present
        
        Returns:
            string -- formatted error message
        """

        status_display = None
        if self.get_status() == self.HIGH_TEMP_ERROR:
            status_display = "High Temperature (100%cC)" % self.DEGREE_SIGN
        elif self.get_status() == self.LOW_TEMP_ERROR:
            status_display = "Low Temperature (-50%cC)" % self.DEGREE_SIGN

        reading_datetime = datetime.datetime.strptime(self.format_datetime_string(), "%Y/%m/%d %H:%M")
        reading_display_datetime = reading_datetime.strftime('%Y/%m/%d %H:%M')

        reading_seq_num = self.get_sequence_num()

        error_msg = "%s at %s, Sequence: %d" % (
            status_display, reading_display_datetime, reading_seq_num)
        return error_msg
