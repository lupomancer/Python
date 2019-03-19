#!/usr/bin/env python3
#
# This is a script to read in and process temperature sensor readings
#
# Author: Cody Sayer
# Version: 1.0
#
import csv
import datetime
from sensor_reading import SensorReading
from reading_stats import ReadingStats
from sensor import Sensor

DEGREE_SIGN = u'\N{DEGREE SIGN}'
sensor_results_file = "sensor_results.csv"


# Main Program
def main():
    """Main program  --  calls other methods and prints results in a human-readable format
    """

    sensor_data = Sensor(sensor_results_file)
    print("Sensor: %s" % (sensor_data.get_sensor_name()))
    print('Period: %s to %s' %(sensor_data.get_time_period()[0], sensor_data.get_time_period()[1]))
    print("Lowest Temperature: %f%cC" %(sensor_data.get_reading_stats()[0], DEGREE_SIGN))
    print("Average Temperature: %f%cC" %(sensor_data.get_reading_stats()[1], DEGREE_SIGN))
    print("Highest Temperature: %f%cC" %(sensor_data.get_reading_stats()[2], DEGREE_SIGN))
    print("Largest Temp Range: %f%cC" % (sensor_data.get_reading_stats()[3], DEGREE_SIGN))
    for msg in sensor_data.get_error_messages():
        print("  " + msg)



if __name__ == "__main__":
    main()
