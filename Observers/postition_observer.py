#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0
from grid import Grid


class PositionOberserver:
    """observes and prints the position of a point on the grid
    """
    def __init__(self, grid):
        self.grid = grid



    def __call__(self):
        print('X = %d, Y = %d' % (self.grid._curr_x, self.grid._curr_y))
