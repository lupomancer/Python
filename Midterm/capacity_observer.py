#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0

from airport import Airport



class CapacityObserver:
    def __init__(self, airport):
        """creates an instance of Airport
        
        Arguments:
            airport {object} -- instance of Airport
        """

        self._airport = airport

    def __call__(self):
        """observes number of airplanes and references maximum airport capacity to give capacity percentages
        """

        if (len(self._airport._airplanes) == 0):
            print('%s is at 0%s of total capacity' % (self._airport._airport_name, '%'))
        elif (len(self._airport._airplanes) == (self._airport._max_capacity / 2)):
            print('%s is at 50%s of total capacity' % (self._airport._airport_name, '%'))
        elif (len(self._airport._airplanes) == (self._airport._max_capacity)):
            print('%s is at 100%s of total capacity' % (self._airport._airport_name, '%'))
        else:
            pass
