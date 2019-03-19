#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0

from airport import Airport



class AirplaneObserver:
    def __init__(self, airport):
        """creates an instance of Airport
        
        Arguments:
            airport {object} -- an instance of Airport
        """

        self._airport = airport

    def __call__(self):
        """observes airport and reports how many planes are on the runway as well as tail IDs
        """

        planes = ', '.join(self._airport._airplanes)
        if len(self._airport._airplanes) == 0:
            planes = 'Empty'
        print('%s currently has %d plane(s) on the tarmac (%s)' % (self._airport._airport_name, self._airport.get_num_airplanes(), planes))
