#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0

class Airport:
    """a model of an airport with airport name and max capacity variables, as well as a list to hold airplane tail IDs

    1. __call__ and __str__ are special built-in methods like __init__
    2. The observers act on conditions of variables withing Airport, which updates said observers via a method
    3. The UML demonstrates Encapsulation by hiding private methods and variables and only showing them to exterior parties via getter methods.
    """

    def __init__(self, airport_name, max_capacity):
        """populates private variables for an instance of Airport
        
        Arguments:
            airport_name {string} -- name of instantiated airport
            max_capacity {int} -- number of planes that tarmac can hold
        """

        self._airplanes = []
        self._airport_name = airport_name
        self._max_capacity = max_capacity
        self.observers = []



    def get_num_airplanes(self):
        """fetches current number of airplanes on tarmac
        
        Returns:
            int -- number of airplanes on tarmac
        """

        return len(self._airplanes)



    def get_airport_name(self):
        """returns the airport name
        
        Returns:
            string -- airport name
        """

        return self._airport_name



    def get_max_capacity(self):
        """returns max capacity
        
        Returns:
            int -- max capacity
        """

        return self._max_capacity



    def set_max_capacity(self, capacity):
        """sets max capacity
        
        Arguments:
            capacity {int} -- input capacity
        """

        if (
            capacity > 0 and
            capacity <= 10
        ):
            self._max_capacity = capacity
            self._update_observers()
        else:
            self._max_capacity = self._max_capacity



    def land_airplane(self, airplane_id):
        """adds a plane to the airplanes list based on ID
        
        Arguments:
            airplane_id {string} -- airplane ID to be added
        """

        self._airplanes.append(airplane_id)
        self._update_observers()



    def depart_airplane(self, airplane_id):
        """removes a plane from the airplanes list based on ID
        
        Arguments:
            airplane_id {string} -- airplane ID to be removed
        """

        self._airplanes.remove(airplane_id)
        self._update_observers()



    def __str__(self):
        """gives a string to be printed when str(object) is called
        
        Returns:
            string -- current airport stats
        """

        planes = ', '.join(self._airplanes)
        if len(self._airplanes) == 0:
            planes = 'Empty'
        return '%s currently has %d plane(s) on the tarmac (%s)' % (self._airport_name, self.get_num_airplanes(), planes)



    def attatch_observer(self, obs):
        """adds an observer to the observers list
        
        Arguments:
            obs {string} -- observer name
        """

        self.observers.append(obs)



    def _update_observers(self):
        """runs the observers for all observers in the list
        """

        for observer in self.observers:
            observer()
