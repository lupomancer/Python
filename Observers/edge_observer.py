#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0
from grid import Grid


class EdgeObserver:
    """Observes and prints when a point on the grid is at one of the edges
    """
    def __init__(self, grid):
        self.grid = grid



    def __call__(self):
        if self.grid._curr_x == 0:
            print('X is at the left edge of the grid!')
        elif self.grid._curr_x == self.grid._width:
            print('X is at the right edhe of the grid!')
        else:
            pass

        if self.grid._curr_y == 0:
            print('Y is at the top edge of the grid!')
        elif self.grid._curr_y == self.grid._height:
            print('Y is at the bottom edge of the grid!')
        else:
            pass
