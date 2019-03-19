#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0
from airport import Airport
from capacity_observer import CapacityObserver
from airplane_observer import AirplaneObserver

def main():
    """creates an instance of Airport and tests all the functions
    """

    airport = Airport('Vancouver Regional Airport', 4)
    cap = CapacityObserver(airport)
    air = AirplaneObserver(airport)
    airport.attatch_observer(air)
    airport.attatch_observer(cap)
    airport.land_airplane('A0001')
    airport.land_airplane('A0002')
    airport.land_airplane('B0011')
    airport.land_airplane('B0012')
    airport.set_max_capacity(15)
    print('%s current maximum capacity is %s' % (airport.get_airport_name(), airport.get_max_capacity()))
    airport.set_max_capacity(8)
    airport.depart_airplane('B0012')
    airport.depart_airplane('B0011')
    airport.depart_airplane('A0002')
    airport.depart_airplane('A0001')
    print(str(airport))



if __name__ == "__main__":
    main()
