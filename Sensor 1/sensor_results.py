
#
# This is a script to read in and process temperature sensor readings
#
# Author: Joe Developer
# Version: 1.0
#
import csv
import datetime
from sensor_reading import SensorReading

DEGREE_SIGN = u'\N{DEGREE SIGN}'
sensor_results_file = "sensor_results.csv"
sensor_results_list = []


# Load csv rows into the sensor results array
# This is our list of lists
def load_data_from_csv():
    with open(sensor_results_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:

            # Converting all the types
            sensor_reading = [row[0], int(row[1]), row[2], float(row[3]), float(row[4]), float(row[5]), row[6]]
            sensor_reading = SensorReading(row[0], int(row[1]), row[2], float(row[3]), float(row[4]), float(row[5]), row[6])
            sensor_results_list.append(sensor_reading)

    # Sorting by sequence number
    sensor_results_list.sort(key=lambda reading: reading.get_sequence_num())

# Displays the name of the sensor taking the readings
def display_sensor_name():
    if len(sensor_results_list) > 0:
        print("Sensor: %s" % (sensor_results_list[1].get_sensor_model()))
    else:
        print("No Sensor Results")


# Displays the time period of the readings (first reading to last reading)
def display_time_period():
    i = 0
    if len(sensor_results_list) > 0:
        start_datetime = datetime.datetime.strptime(
            sensor_results_list[i].get_date_time(), "%Y-%m-%d %H:%M:%S.%f")
        end_datetime = datetime.datetime.strptime(
            sensor_results_list[len(sensor_results_list)-1].get_date_time(), "%Y-%m-%d %H:%M:%S.%f")

        start_display_datetime = start_datetime.strftime("%Y/%m/%d %H:%M")
        end_display_datetime = end_datetime.strftime("%Y/%m/%d %H:%M")

        print("Period: %s to %s" %(start_display_datetime, end_display_datetime))
    else:
        print("No Results")


# Calculates and displays the temperature statistics
def display_temperature_stats():
    if len(sensor_results_list) == 0:
        return

    num_ok_readings = 0
    total_temp = 0.0

    lowest_temp = None
    highest_temp = None

    largest_temp_range = 0.0
    i = 0
    while i < len(sensor_results_list):
        for reading in sensor_results_list:
            # Ignore bad readings
            if sensor_results_list[i].get_status() != "OK":
                continue

            reading_low_temp = sensor_results_list[i].get_low_temp()
            reading_avg_temp = sensor_results_list[i].get_avg_temp()
            reading_high_temp = sensor_results_list[i].get_high_temp()

        if lowest_temp is None:
            lowest_temp = reading_low_temp
        elif reading_low_temp < lowest_temp:
            lowest_temp = reading_low_temp

        if highest_temp is None:
            highest_temp = reading_high_temp
        elif reading_high_temp > highest_temp:
            highest_temp = reading_high_temp
        i += 1


        num_ok_readings += 1
        total_temp += reading_avg_temp

        curr_temp_range = reading_high_temp - reading_low_temp

        if curr_temp_range > largest_temp_range:
            largest_temp_range = curr_temp_range

    average_temp = (total_temp / num_ok_readings)

    print("Lowest Temperature: %f%cC" % (lowest_temp, DEGREE_SIGN))
    print("Average Temperature: %f%cC" % (average_temp, DEGREE_SIGN))
    print("Highest Temperature: %f%cC" % (highest_temp, DEGREE_SIGN))

    if largest_temp_range > 0.0:
        print("Largest Temp Range: %f%cC" % (largest_temp_range, DEGREE_SIGN))
    else:
        print("Largest Temp Range: Invalid or No Variation")


# Displays any erroneous readings (HIGH_TEMP or LOW_TEMP)
def display_error_readings():

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
                    status_display = "High Temperature Error (100%cC)" % (DEGREE_SIGN)
                elif status == "LOW_TEMP":
                    status_display = "Low Temperature Error (-50%cC)" % (DEGREE_SIGN)

                reading_datetime = datetime.datetime.strptime(sensor_results_list[i].get_date_time(), "%Y-%m-%d %H:%M:%S.%f")
                reading_display_datetime = reading_datetime.strftime('%Y/%m/%d %H:%M')

                reading_seq_num = sensor_results_list[i].get_sequence_num()

                high_msg = "%s at %s, Sequence: %d" % (
                    status_display, reading_display_datetime, reading_seq_num)
                if high_msg not in error_msgs:
                    error_msgs.append(high_msg)
        i += 1

    if len(error_msgs) > 0:
        print("Error Readings:")
        for msg in error_msgs:
            print("  " + msg)
    else:
        print("No Error Readings")

# Main Program
def main():
    load_data_from_csv()

    display_sensor_name()
    display_time_period()
    display_temperature_stats()
    display_error_readings()


if __name__ == "__main__":
    main()
