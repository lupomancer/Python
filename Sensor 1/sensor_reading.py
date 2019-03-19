#!/usr/bin/env python3

from datetime import datetime

class SensorReading:
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

        self.validate_string("date_time", date_time)
        self._date_time = date_time

        self.validate_num("sequence_num", sequence_num)
        self._sequence_num = sequence_num

        self.validate_string("sensor_model", sensor_model)
        self._sensor_model = sensor_model

        self.validate_num("low_temp", low_temp)
        self._low_temp = low_temp

        self.validate_num("avg_temp", avg_temp)
        self._avg_temp = avg_temp

        self.validate_num("high_temp", high_temp)
        self._high_temp = high_temp

        self.validate_string("status", status)
        self._status = status



    def get_date_time(self):

        """retrieves the date and time from sensor reading
        
        Returns:
            string -- date and time of reading
        """

        return self._date_time



    def get_sequence_num(self):

        """retrieves the sequence number from sensor reading
        
        Returns:
            int -- sequence number of reading
        """

        return self._sequence_num



    def get_sensor_model(self):

        """retrieves the sensor model from sensor reading
        
        Returns:
            string -- sensor model of reading
        """

        return self._sensor_model



    def get_low_temp(self):

        """retrieves the low temp reading from sensor reading
        
        Returns:
            float -- low temp reading
        """

        return self._low_temp



    def get_avg_temp(self):

        """retrieves the average temp reading from sensor reading
        
        Returns:
            float -- average temp reading
        """

        return self._avg_temp



    def get_high_temp(self):

        """retrieves the high temp reading of sensor reading
        
        Returns:
            float -- high temp reading
        """

        return self._high_temp



    def get_status(self):

        """retrieves the status of the sensor at time of reading
        
        Returns:
            string -- sensor status at time of reading
        """

        return self._status

    """end getters
    """


    """begin setters
    """

    def set_date(self, date_string):

        """parses datetime from string and assigns to variable
        """

        self._date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")



    def set_sequence(self, sequence_num):

        """validates and sets sequence number
        """

        self.validate_num("sequence_num", sequence_num)
        self._sequence_num = sequence_num



    def set_sensor_model(self, sensor_model):

        """validates and sets sensor model
        """

        self.validate_string("sensor_model", sensor_model)
        self._sensor_model = sensor_model



    def set_low_temp(self, low_temp):

        """validates and sets low temp
        """

        self.validate_num("low_temp", low_temp)
        self._low_temp = low_temp



    def set_avg_temp(self, avg_temp):

        """validates and sets average temperature
        """

        self.validate_num("avg_temp", avg_temp)
        self._avg_temp = avg_temp



    def set_high_temp(self, high_temp):

        """validates and sets high temperature
        """

        self.validate_num("high_temp", high_temp)
        self._high_temp = high_temp



    def set_status(self, status):

        """validates and sets the sensor status
        """

        self.validate_string("status", status)
        self._status = status



    def get_display_date(self):

        """retrieves datetime formatted date
        
        Returns:
            datetime -- date and time formatted in Year/Month/Day Hour:Minute
        """

        return self._date.strftime("%Y/%m/%d %H:%M")



    def valid_status(self):

        """returns a valid status
        
        Returns:
            string -- that status as "OK", indicating no errors in a sensor reading
        """

        return self._status == "OK"



    def get_display_status(self, DEGREE_SIGN):

        """retrieves the sensor status and returns a formatted string
        
        Returns:
            string -- one of two error states for sensor status
        """

        if self._status == "HIGH_TEMP":
            return "High Temperature Error (100%cC)" % DEGREE_SIGN
        elif self._status == "LOW_TEMP":
            return "Low Temperature Error (-50%cC)" % DEGREE_SIGN



    @staticmethod
    def validate_string(name, string):

        """validates a string to disallow empty or unassigned strings
        
        Raises:
            ValueError -- invalid error message
            ValueError -- empty error message
        """

        if string is None:
            raise ValueError(name + "cannot be invalid.")
        if string == "":
            raise ValueError(name + "cannot be empty.")

    @staticmethod
    def validate_num(name, num):

        """validates a num to disallow unassigned numbers
        
        Raises:
            ValueError -- empty error message
        """

        if num is None:
            raise ValueError(name + "cannot be invalid.")