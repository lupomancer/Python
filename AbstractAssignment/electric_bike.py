#!/usr/bin/env python3
#
# ElectricBike Class
#
# Cody Sayer and William Prout
#
# Ver 1.2
import auger

class ElectricBike:
    ID = 0
    MANUFACTURER = 1
    MODEL = 2
    YEAR = 3
    PRICE = 4
    WHEEL_SIZE = 5
    BATTERY_CAPACITY = 7
    MOTOR_TYPE = 8
    HUB_SIZE = 9
    CATEGORY = "Electric Bike"



    def __init__(self, bike):
        """initializes a bike object
        
        Arguments:
            bike {list} -- list of bike components
        """

        self._battery_capacity = bike[7]
        self._motor_type = bike [8]
        self._hub_size = bike[9]



    def get_battery_capacity(self):
        """returns battery capacity
        
        Returns:
            int -- battery capacity in kWh
        """

        return self._battery_capacity



    def get_motor_type(self):
        """returns motor type
        
        Returns:
            string -- motor type (brushless, stepper, etc)
        """

        return self._motor_type



    def get_hub_size(self):
        """returns drive hub size
        
        Returns:
            int -- drive hub size in inches
        """

        return self._hub_size



    def get_category(self):
        """returns bike category
        
        Returns:
            string -- bike category
        """

        return ElectricBike.CATEGORY


