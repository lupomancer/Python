#!/usr/bin/env python3
#
# AbstractBike Class
#
# Cody Sayer and William Prout
#
# Ver 1.2
from electric_bike import ElectricBike
from motor_bike import MotorBike


class AbstractBike:



    def __init__(self, id, manufacturer, model, year, price, wheel_size, category, spec1, spec2, spec3):
        """initializes a bike object
        
        Arguments:
            id {int} -- bike ID number
            manufacturer {string} -- bike manufacturer
            model {string} -- name of bike model
            year {int} -- year of bike manufacture
            price {int} -- purchase price of bike
            wheel_size {int} -- bike wheel size
            category {string} -- bike category
            spec1 {multi} -- first of a multi-use variable
            spec2 {multi} -- second of a multi-use variable
            spec3 {multi} -- third of a multi-use variable
        """

        self._id = id
        self._manufacturer = manufacturer
        self._model = model
        self._year = year
        self._price = price
        self._wheel_size = wheel_size
        self._type = category
        self._spec1 = spec1
        self._spec2 = spec2
        self._spec3 = spec3
        self.bike = [id, manufacturer, model, year, price, wheel_size, category, spec1, spec2, spec3]



    def get_id(self):
        """returns bike ID
        
        Returns:
            int -- bike ID
        """

        return self._id




    def get_manufacturer(self):
        """returns manufacturer
        
        Returns:
            string -- bike manufacturer
        """

        return self._manufacturer



    def get_model(self):
        """returns model name
        
        Returns:
            string -- bike model
        """

        return self._model



    def get_year(self):
        """returns manufacture year
        
        Returns:
            int -- manufacture year
        """

        return self._year



    def get_price(self):
        """returns purchase price
        
        Returns:
            int -- purchase price
        """

        return self._price



    def get_wheel_size(self):
        """returns wheel size
        
        Returns:
            int -- wheel size
        """

        return self._wheel_size



    def get_details(self):
        bike = self.bike
        if self._type == "Electric Bike":
            bike_details = ElectricBike(bike)
            batt_cap = bike_details.get_battery_capacity()
            motor_type = bike_details.get_motor_type()
            hub_size = bike_details.get_hub_size()
            cat = bike_details.get_category()
            stat_list = [cat, batt_cap, motor_type, hub_size]
            return stat_list
        elif self._type == "Motorbike":
            bike_details = MotorBike(bike)
            fuel_cap = bike_details.get_fuel_capacity()
            engine_disp = bike_details.get_engine_displacement()
            street_safe = bike_details.get_street_legal()
            cat = bike_details.get_category()
            stat_list = [cat, fuel_cap, engine_disp, street_safe]
            return stat_list



    def get_category(self):
        return self._type
