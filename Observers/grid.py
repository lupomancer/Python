#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0

class Grid:
    """constructs and maintains a grid object
    """

    def __init__(self, width, height, init_x, init_y):

        """constructs the grid object
        
        Arguments:
            width {int} -- the width of the grid
            height {int} -- the height of the grid
            init_x {int} -- initial x coordinate for point
            init_y {int} -- initial y coordinate for point
        """
        self._width = width
        self._height = height
        self._curr_x = init_x
        self._curr_y = init_y
        self.observers = []



    def get_width(self):
        return self._width



    def get_height(self):
        return self._height



    def get_x(self):
        return self._curr_x



    def get_y(self):
        return self._curr_y



    def move_left(self):
        if self._curr_x == 0:
            pass
        else:
            self._curr_x = self._curr_x - 1
            self._update_observers()



    def move_right(self):
        if self._curr_x == self._width:
            pass
        else:
            self._curr_x = self._curr_x + 1
            self._update_observers()



    def move_up(self):
        if self._curr_y == 0:
            pass
        else:
            self._curr_y = self._curr_y - 1
            self._update_observers()



    def move_down(self):
        if self._curr_y == self._height:
            pass
        else:
            self._curr_y = self._curr_y + 1
            self._update_observers()



    def attatch(self, observer):
        self.observers.append(observer)



    def __str__(self):
        return 'Grid size is: %d x %d. Point coordinates are %d, %d.' % (self._width, self._height, self._curr_x, self._curr_y)



    def __repr__(self):
        return 'Grid size is: %d x %d. Point coordinates are %d, %d.\nThere are %d observers attatched.\nThe object ID is %d.' % (self._width, self._height, self._curr_x, self._curr_y, len(self.observers), id(self))



    def _update_observers(self):
        for observer in self.observers:
            observer()
