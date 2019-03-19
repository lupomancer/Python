#! /usr/bin/env python3
#
# intakes a list of sensor temperature readings and pulls/formats various information from it to return
#
# Author: Cody Sayer
# Version: 2.0
#


class ReadingStats:
    """Parses certain pieces of information from a given list"""

    def __init__(self, low_temp, avg_temp, high_temp, temp_range):
        """Initializes the sensor reading
        
        Arguments:
            low_temp {float} -- low temp reading
            avg_temp {float} -- average temp reading
            high_temp {float} -- high temp reading
            temp_range {float} -- reading range
        """


        self._validate_input_float("Low_temp", low_temp)
        self._low_temp = low_temp

        self._validate_input_float("Avg_temp", avg_temp)
        self._avg_temp = avg_temp

        self._validate_input_float("High_temp", high_temp)
        self._high_temp = high_temp

        self._validate_input_float("temp_Range", temp_range)
        self._temp_range = temp_range



    def get_lowest_reading(self):
        """retrieves anf returns the low temperature
        
        Returns:
            float -- lowest temperature recorded
        """

        return self._low_temp



    def get_average_reading(self):
        """retrieves anf returns the average temperature
        
        Returns:
            float -- average temperature
        """

        return self._avg_temp



    def get_highest_reading(self):
        """retrieves and returns the high temperature
        
        Returns:
            float -- highest temperature recorded
        """
        return self._high_temp



    def get_largest_reading_range(self):
        """retrieves and returns the temperature range
        
        Returns:
            float -- largest temperature range in the list
        """

        return self._temp_range





    @staticmethod
    def _validate_input_float(name, number):
        """validates that input is of float type
        
        Arguments:
            name {value name} -- given name for value
            number {input value} -- the value to be validated
        
        Raises:
            ValueError -- if value is undefined
            ValueError -- if value is not of float type
        """

        if number is None:
            raise ValueError(name + " cannot be undefined.")
        if not isinstance(number, float):
            raise ValueError(name + " must be float.")
