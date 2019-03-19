#!/usr/bin/env python3
#
# parses a given CSV file and turns it into a list of temperature readings and returns various values from that list
#
# Author: Cody Sayer
# Version: 1.0
#
import csv
import datetime
from sensor_reading import SensorReading
from reading_stats import ReadingStats

sensor_results_list = []
DEGREE_SIGN = u'\N{DEGREE SIGN}'

class Sensor:
    """parses out a given CSV file into a list, then creating a list of said lists
    """

    def __init__(self, file):
        """Initialize the list of sensor data and sort it by sequence number
        
        Arguments:
            file {string} -- the name of the file that csv.reader opens
        """

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:

                # Converting all the types
                sensor_reading = [row[0], int(row[1]), row[2], float(row[3]), float(row[4]), float(row[5]), row[6]]
                sensor_reading = SensorReading(row[0], int(row[1]), row[2], float(row[3]), float(row[4]), float(row[5]), row[6])
                sensor_results_list.append(sensor_reading)
        # Sorting by sequence number
        sensor_results_list.sort(key=lambda reading: reading.get_sequence_num())



    def get_sensor_name(self):
        """returns sensor name
        
        Returns:
            string -- sensor name
        """

        if len(sensor_results_list) > 0:

            return sensor_results_list[1].get_sensor_model()



    def get_time_period(self):
        """gets time period by finding first and last time entries and formats them by YEAR/MONTH/DAY HOUR:MINUTE
        
        Returns:
            period_list -- a list comprised of start_display_time and end_display_time
        """

        if len(sensor_results_list) > 0:
            start_datetime = datetime.datetime.strptime(sensor_results_list[0].get_date_time(), "%Y-%m-%d %H:%M:%S.%f")
            end_datetime = datetime.datetime.strptime(sensor_results_list[len(sensor_results_list)-1].get_date_time(), "%Y-%m-%d %H:%M:%S.%f")

            start_display_datetime = start_datetime.strftime("%Y/%m/%d %H:%M")
            end_display_datetime = end_datetime.strftime("%Y/%m/%d %H:%M")

            period_list = [start_display_datetime, end_display_datetime]

        return period_list



    def get_reading_stats(self):
        """uses various methods from reading_stats to return the lowest temperature, average temperature, highest temperature, and the temperature range
        
        Returns:
            list -- a list comprised of lowTemp, avgTemp, highTemp, and tempRange
        """

        results = ReadingStats(sensor_results_list)
        lowTemp = results.get_lowest_reading()
        avgTemp = results.get_average_reading()
        highTemp = results.get_highest_reading()
        tempRange = results.get_largest_reading_range()
        reading_list = [lowTemp, avgTemp, highTemp, tempRange]

        return reading_list



    def get_error_messages(self):
        """Finds and returns error messages within the data and formats them into something human-readable
        
        Returns:
            list -- a list of all recorded error messages
        """

        if len(sensor_results_list) == 0:
            return

        error_msgs = []
        i = 0
        while i < len(sensor_results_list):
            for reading in sensor_results_list:

                status = sensor_results_list[i].get_status()
                if status != "OK":
                    status_display = ""
                    if status == "HIGH_TEMP":
                        status_display = "High Temperature Error (100%cC)" % (
                            DEGREE_SIGN)
                    elif status == "LOW_TEMP":
                        status_display = "Low Temperature Error (-50%cC)" % (
                            DEGREE_SIGN)

                    reading_datetime = datetime.datetime.strptime(
                        sensor_results_list[i].get_date_time(), "%Y-%m-%d %H:%M:%S.%f")
                    reading_display_datetime = reading_datetime.strftime(
                        '%Y/%m/%d %H:%M')

                    reading_seq_num = sensor_results_list[i].get_sequence_num()

                    high_msg = "%s at %s, Sequence: %d" % (
                        status_display, reading_display_datetime, reading_seq_num)
                    if high_msg not in error_msgs:
                        error_msgs.append(high_msg)
            i += 1

        return error_msgs
