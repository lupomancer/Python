#!/usr/bin/env python3
#
# MotorBike Class
#
# Cody Sayer and William Prout
#
# Ver 1.2



class MotorBike:
    ID = 0
    MANUFACTURER = 1
    MODEL = 2
    YEAR = 3
    PRICE = 4
    WHEEL_SIZE = 5
    FUEL_CAPACITY = 7
    ENGINE_DISPLACEMENT = 8
    STREET_LEGAL = 9
    CATEGORY = "Motorbike"



    def __init__(self, bike):
        """constructs a part of the bike with an incoming list
        
        Arguments:
            bike {list} -- list of bike components
        """

        self._fuel_capacity = bike[7]
        self._engine_displacement = bike[8]
        self._street_legal = bike[9]



    def get_fuel_capacity(self):
        """returns the fuel capacity of a motorbike
        
        Returns:
            float -- fuel capacity in Litres
        """

        return self._fuel_capacity



    def get_engine_displacement(self):
        """returns the engine displacement of a motorbike
        
        Returns:
            float -- engine displacement in litres
        """

        return self._engine_displacement



    def get_street_legal(self):
        """returns whether a motorbike is street legal or not
        
        Returns:
            boolean -- street legal status
        """

        return self._street_legal



    def get_category(self):
        """returns the category in which a bike resides
        
        Returns:
            string -- bike category
        """

        return MotorBike.CATEGORY
