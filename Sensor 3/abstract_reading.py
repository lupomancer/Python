#! /usr/bin/env python3
#
# Gets and retusrns valuse from a single line of temperature sensor data
#
# Author: Cody Sayer
# Version: 2.0
#
from datetime import datetime

class AbstractReading:
    """Maintains the details of each sensor reading
    """

    DATE_TIME_STR = "Date Time"
    SEQUENCE_NUM_STR = "Sequence Number"
    SENSOR_MODEL_STR = "Sensor Model"
    LOW_TEMP_STR = "Low temp"
    AVERAGE_TEMP_STR = "Average temp"
    HIGH_TEMP_STR = "High temp"
    STATUS_STR = "Status"
    STRPTIME = "%Y-%m-%d %H:%M:%S.%f"
    STRFTIME = "%Y/%m/%d %H:%M"
    DEGREE_SIGN = u'\N{DEGREE SIGN}'
    HIGH_READ_ERROR = "HIGH_READ"
    LOW_READ_ERROR = "LOW_READ"

    def __init__(self, date_time, sequence_num, sensor_model, low_temp, avg_temp, high_temp, status):
        """constructor for the SensorReading class
        
        Arguments:
            date_time {string} -- the date and time from the CSV
            sequence_num {int} -- the sequence number if the sensor reading
            sensor_model {string} -- the model information of the sensor
            low_temp {float} -- the low temp reading from the sensor
            avg_temp {float} -- the avg temp reading from the sensor
            high_temp {float} -- the high temp reading from the sensor
            status {string} -- the status of the sensor during the reading
        """

        AbstractReading._validate_input(AbstractReading.DATE_TIME_STR, date_time)
        AbstractReading._validate_string(AbstractReading.DATE_TIME_STR, date_time)
        self._date_time = date_time

        AbstractReading._validate_input(AbstractReading.SEQUENCE_NUM_STR, sequence_num)
        AbstractReading._validate_int(AbstractReading.SEQUENCE_NUM_STR, sequence_num)
        self._sequence_num = sequence_num

        AbstractReading._validate_input(AbstractReading.SENSOR_MODEL_STR, sensor_model)
        AbstractReading._validate_string(AbstractReading.SENSOR_MODEL_STR, sensor_model)
        self._sensor_model = sensor_model

        AbstractReading._validate_input(AbstractReading.LOW_TEMP_STR, low_temp)
        AbstractReading._validate_float(AbstractReading.LOW_TEMP_STR, low_temp)
        self._low_read = low_temp

        AbstractReading._validate_input(AbstractReading.AVERAGE_TEMP_STR, avg_temp)
        AbstractReading._validate_float(AbstractReading.AVERAGE_TEMP_STR, avg_temp)
        self._average_read = avg_temp

        AbstractReading._validate_input(AbstractReading.HIGH_TEMP_STR, high_temp)
        AbstractReading._validate_float(AbstractReading.HIGH_TEMP_STR, high_temp)
        self._high_read = high_temp

        AbstractReading._validate_input(AbstractReading.STATUS_STR, status)
        AbstractReading._validate_string(AbstractReading.STATUS_STR, status)
        self._status = status



    def format_datetime_string(self):
        """Retrieves the datetime and formats into Y/M/D H:M
        
        Returns:
            datetime -- the datetime from a sensor reading
        """

        return datetime.strptime(self._date_time, "%Y-%m-%d %H:%M:%S.%f").strftime("%Y/%m/%d %H:%M")



    def format_output_strings(self):
        """Returns a message if error is detected in log
        
        Returns:
            string -- error message
        """

        if self._status == AbstractReading.HIGH_READ_ERROR:
            status_display = "High reading Error (100%cC)" % AbstractReading.DEGREE_SIGN
            reading_display_datetime = self.format_datetime_string()
            reading_seq_num = self.get_sequence_num()
            return "%s at %s, Sequence: %d" % (status_display, reading_display_datetime, reading_seq_num)

        elif self._status == AbstractReading.LOW_READ_ERROR:
            status_display = "Low reading Error (-50%cC)" % AbstractReading.DEGREE_SIGN
            reading_display_datetime = self.format_datetime_string()
            reading_seq_num = self.get_sequence_num()
            return "%s at %s, Sequence: %d" % (status_display, reading_display_datetime, reading_seq_num)



    def get_sequence_num(self):
        """retrieves and returns the sequence number from the reading line
        
        Returns:
            int -- sequence number
        """

        return self._sequence_num



    def get_sensor_model(self):
        """retrieves and returns the sensor model from the reading line
        
        Returns:
            string -- sensor model
        """

        return self._sensor_model



    def get_low_reading(self):
        """retrieves and returns the lowest reading from the reading line
        
        Returns:
            float -- low reading
        """

        return self._low_read



    def get_average_reading(self):
        """retrieves and returns the average reading from the reading line
        
        Returns:
            float -- average reading
        """

        return self._average_read



    def get_high_reading(self):
        """retrieves and returns the highest reading from the reading line
        
        Returns:
            float -- high reading
        """

        return self._high_read



    def get_reading_range(self):
        """calculates and returns the reading range from the reading line
        
        Returns:
            float -- reading range
        """

        return self._high_read - self._low_read



    def get_status(self):
        """retrieves and returns the status message of a reading line
        
        Returns:
            string -- sensor status
        """

        return self._status



    def is_error(self):
        """checks if there is an error
        
        Raises:
            NotImplementedError -- is_error test not implemented
        """

        raise NotImplementedError()



    def get_error_msg(self):
        """retrieves the error message if present
        
        Raises:
            NotImplementedError -- get_error_message not implemented
        """

        raise NotImplementedError()





    @staticmethod
    def _validate_string(display_name, input_value):
        """validates a string
        
        Arguments:
            display_name {value name} -- the actual name assigned to the value
            input_value {input} -- the input to be validated
        
        Raises:
            ValueError -- if it is not a string
        """

        if input_value != str(input_value):
            raise ValueError(display_name + " must be a string type")



    @staticmethod
    def _validate_int(display_name, input_value):
        """validates the input value to make sure it is of int type
        
        Arguments:
            display_name {value name} -- the given name for a value
            input_value {input} -- the input to be validated
        
        Raises:
            ValueError -- if it is not an integer
        """

        if input_value != int(input_value):
            raise ValueError(display_name + " must be a integer type")



    @staticmethod
    def _validate_float(display_name, input_value):
        """validates the input value to make sure it is of float type
        
        Arguments:
            display_name {value name} -- the given name for a value
            input_value {input} -- the input to be validated
        
        Raises:
            ValueError -- if it is not a float
        """

        if input_value != float(input_value):
            raise ValueError(display_name, " must be a float type")



    @staticmethod
    def _validate_input(display_name, input_value):
        """validates the input to make sure it is not None or empty
        
        Arguments:
            display_name {value name} -- the given name for a value
            input_value {input} -- the input to be validated
        
        Raises:
            ValueError -- if input is undefined
            ValueError -- if input is empty
        """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")
