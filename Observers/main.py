#!/usr/bin/env python3
#
#
# Cody Sayer
#
# Ver. 1.0
from grid import Grid
from postition_observer import PositionOberserver
from edge_observer import EdgeObserver

def main():
    grid = Grid(7,5,3,2)
    pos = PositionOberserver(grid)
    edge = EdgeObserver(grid)
    grid.attatch(pos)
    grid.attatch(edge)
    grid.move_down()
    grid.move_down()
    grid.move_down()
    grid.move_up()
    grid.move_up()
    grid.move_up()
    grid.move_up()
    grid.move_up()
    grid.move_down()
    grid.move_left()
    grid.move_left()
    grid.move_left()
    grid.move_right()
    grid.move_right()
    grid.move_right()
    grid.move_right()
    grid.move_right()
    grid.move_right()
    grid.move_right()
    grid.move_right()
    grid.move_left()
    print(grid)
    print(str(grid))
    print(repr(grid))

if __name__ == "__main__":
    main()
