#!/usr/bin/env python3


class Rover(object):
    """ Rover object
    :arg: name
    :arg initial_position: tuple with the initial position in the format: (x, y, orientation)
    :arg boundaries: plateau boundaries
    """
    def __init__(self, name, initial_position, boundaries):
        self.name = name
        self._x = initial_position[0]
        self._y = initial_position[1]
        self._direction = initial_position[2]
        self._boundaries = boundaries

    def __repr__(self):
        return f'{self.name} ({self._x}, {self._y}, {self._direction})'
