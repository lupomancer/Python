#! /usr/bin/env python3
#
# Gets and retusrns valuse from a single line of temperature sensor data
#
# Author: Cody Sayer
# Version: 2.0
#
import csv
from reading_stats import ReadingStats


class AbstractSensor:
    """parses out a given CSV file into a list, then creating a list of said lists
    """


    DEGREE_SIGN = u'\N{DEGREE SIGN}'

    def __init__(self, file):
        """Initialize the list of sensor data and sort it by sequence number
        
        Arguments:
            file {string} -- the name of the file that csv.reader opens
        """
        self._validate_string("file", file)
        sensor_results_list = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                sensor_reading = self._load_reading_row(row)
                sensor_results_list.append(sensor_reading)

        sensor_results_list.sort(key=lambda reading: reading.get_sequence_num())
        self._sensor_results_list = sensor_results_list



    def get_sensor_name(self):
        """retrieves and returns the sensor name from the reading line
        
        Returns:
            string -- sensor name
        """

        return self._sensor_results_list[0].get_sensor_model()



    def get_time_period(self):
        """retrieves and returns the time period of the sensor reading
        
        Returns:
            datetime -- the start and end times of the sensor reading
        """

        date1 = self._sensor_results_list[0].format_datetime_string()
        date2 = self._sensor_results_list[-1].format_datetime_string()
        return (date1, date2)



    def get_reading_stats(self):
        """retrieves and returns the readings from the reading line
        
        Returns:
            float -- various readings from reading line
        """

        if len(self._sensor_results_list) == 0:
            return

        num_ok_readings = 0
        total_temp = 0.0

        lowread = None
        highread = None

        temp_range = 0.0

        for reading in self._sensor_results_list:
            if reading.is_error():
                continue

            reading_low_temp = reading.get_low_reading()
            reading_avg_temp = reading.get_average_reading()
            reading_high_temp = reading.get_high_reading()

            if lowread is None:
                lowread = reading_low_temp
            elif reading_low_temp < lowread:
                lowread = reading_low_temp

            if highread is None:
                highread = reading_high_temp
            elif reading_high_temp > highread:
                highread = reading_high_temp

            num_ok_readings += 1
            total_temp += reading_avg_temp

            current_temp_range = reading_high_temp - reading_low_temp

            if current_temp_range > temp_range:
                temp_range = current_temp_range

            avgread = (total_temp / num_ok_readings)

        return ReadingStats(lowread, avgread, highread, temp_range)



    def get_error_messages(self):
        """retrieves and returns error messages if present
        
        Returns:
            list -- a list of all present error messages
        """

        if len(self._sensor_results_list) == 0:
            return

        error_msgs = []

        for reading in self._sensor_results_list:
            if reading.is_error():
                error_msgs.append(reading.get_error_msg())

        if len(error_msgs) > 0:
            return error_msgs
        else:
            return "No Error Readings"



    def _load_reading_row(self):
        """loads the reading row from file
        
        Raises:
            NotImplementedError -- if the load_reading_row function is not implemented
        """

        raise NotImplementedError()






    @staticmethod
    def _validate_string(display_name, input_value):
        """validates if input is of string type
        
        Arguments:
            display_name {value name} -- the given name for the value
            input_value {value} -- the value to be validated
        
        Raises:
            ValueError -- if value is not of string type
            ValueError -- if value is empty
        """

        if not isinstance(input_value, str):
            raise ValueError(display_name + " must be a string type")
        if input_value == '':
            raise ValueError(display_name + " cannot be empty")
