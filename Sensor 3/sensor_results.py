#! /usr/bin/env python3
#
# This is a script to read in and process temperature sensor readings
#
# Author: Cody Sayer
# Version: 2.0
#
from temperature_sensor import TemperatureSensor
from pressure_sensor import PressureSensor


DEGREE_SIGN = u'\N{DEGREE SIGN}'
PRESSURE_SIGN = 'kPa'

sensor_results_file = "temperature_results.csv"
sensor_results_file2 = "pressure_results.csv"
sensor_results_list = []


# Main Program
def main():
    """Main program  --  calls other methods and prints results in a human-readable format
    """

    sensor = TemperatureSensor(sensor_results_file)
    print()
    print("Sensor: %s" % (sensor.get_sensor_name()))
    print("Period: %s to %s" % (sensor.get_time_period()))
    print("Lowest Temp: %f%cC" % (sensor.get_reading_stats().get_lowest_reading(), DEGREE_SIGN))
    print("Average Temp: %f%cC" % (sensor.get_reading_stats().get_average_reading(), DEGREE_SIGN))
    print("Highest Temp: %f%cC" % (sensor.get_reading_stats().get_highest_reading(), DEGREE_SIGN))
    print("Largest Temp Range: %f%cC" % (sensor.get_reading_stats().get_largest_reading_range(), DEGREE_SIGN))
    if isinstance(sensor.get_error_messages(), list) > 0:
        print("Error Messages:")
        for msg in sensor.get_error_messages():
            print("  " + msg)
    else:
        print("No Error Readings")

    sensor = PressureSensor(sensor_results_file2)
    print()
    print("Sensor: %s" % (sensor.get_sensor_name()))
    print("Period: %s to %s" % (sensor.get_time_period()))
    print("Lowest Pressure: %f %s" % (sensor.get_reading_stats().get_lowest_reading(), PRESSURE_SIGN))
    print("Average Pressure: %f %s" % (sensor.get_reading_stats().get_average_reading(), PRESSURE_SIGN))
    print("Highest Pressure: %f %s" % (sensor.get_reading_stats().get_highest_reading(), PRESSURE_SIGN))
    print("Largest Pressure Range: %f %s" % (sensor.get_reading_stats().get_largest_reading_range(), PRESSURE_SIGN))
    if isinstance(sensor.get_error_messages(), list) > 0:
        print("Error Messages:")
        for msg in sensor.get_error_messages():
            print("  " + msg)
    else:
        print("No Error Readings")

if __name__ == "__main__":
    main()
