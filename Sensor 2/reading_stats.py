#!/usr/bin/env python3
#
# intakes a list of sensor temperature readings and pulls/formats various information from it to return
#
# Author: Cody Sayer
# Version: 1.0
#
from datetime import datetime
from sensor_reading import SensorReading


class ReadingStats:
    """Parses certain pieces of information from a given list"""
    
    

    def __init__(self, sensor_results_list):
        """initialize the list of sensor results
        
        Arguments:
            sensor_results_list {list} -- a list of information pulled from the CSV
        """

        self._sensor_results_list = sensor_results_list



    def get_lowest_reading(self):
        """Uses the fuction get_low_temp within SensorReading to pull the lowest temperature from a given line of the list and compare to find the lowest overall temp
        
        Returns:
            float -- lowest temperature recorded
        """

        if len(self._sensor_results_list) == 0:
            return

        lowest_reading = None

        i = 0
        while i < len(self._sensor_results_list):
            for reading in self._sensor_results_list:
                #ignore bad readings
                if self._sensor_results_list[i].get_status() != "OK":
                    continue
                reading_low_temp = self._sensor_results_list[i].get_low_temp()
            if lowest_reading is None:
                lowest_reading = reading_low_temp
            elif reading_low_temp < lowest_reading:
                lowest_reading = reading_low_temp
            i += 1

        return lowest_reading



    def get_average_reading(self):
        """Uses the fuction get_avg_temp within SensorReading to pull the average temperature of all readings in the list
        
        Returns:
            float -- calculated average temperature from the list
        """

        num_ok_readings = 0
        total_temp = 0.0

        i = 0
        while i < len(self._sensor_results_list):
            for reading in self._sensor_results_list:
                reading_avg_temp = self._sensor_results_list[i].get_avg_temp()
            i += 1

            num_ok_readings += 1
            total_temp += reading_avg_temp

        average_reading = (total_temp / num_ok_readings)

        return average_reading



    def get_highest_reading(self):
        """Uses the fuction get_high_temp within SensorReading to pull the highest temperature from a given line of the list and compare to find the highest overall temp
        
        Returns:
            float -- highest temperature recorded
        """
        if len(self._sensor_results_list) == 0:
            return

        highest_reading = None

        i = 0
        while i < len(self._sensor_results_list):
            for reading in self._sensor_results_list:
                #ignore bad readings
                if self._sensor_results_list[i].get_status() != "OK":
                    continue
                reading_high_temp = self._sensor_results_list[i].get_low_temp()
            if highest_reading is None:
                highest_reading = reading_high_temp
            elif reading_high_temp > highest_reading:
                highest_reading = reading_high_temp
            i += 1

        return highest_reading



    def get_largest_reading_range(self):
        """Uses the get_low_temp and get_high_temp functions from SensorReading to compare and find the larges temperature range in the list
        
        Returns:
            float -- largest temperature range in the list
        """

        largest_reading_range = 0
        i = 0
        while i < len(self._sensor_results_list):
            for reading in self._sensor_results_list:
                reading_low_temp = self._sensor_results_list[i].get_low_temp()
                reading_high_temp = self._sensor_results_list[i].get_high_temp()
            i += 1

            curr_temp_range = reading_high_temp - reading_low_temp

            if curr_temp_range > largest_reading_range:
                largest_reading_range = curr_temp_range

        return largest_reading_range
