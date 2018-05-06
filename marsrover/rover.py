#!/usr/bin/env python3


class Rover(object):
    """ Rover object
    :arg: name
    :arg initial_position: tuple with the initial position in the format: (x, y, orientation)
    :arg boundaries: plateau boundaries
    """

    CARDINALS_ANGLES = {
        'E': 0,
        'N': 90,
        'W': 180,
        'S': 270,
    }

    # reverse index for getting cardinal position of a angle
    ANGLES_CARDINALS = {angle: cardinal for cardinal, angle in CARDINALS_ANGLES.items()}

    def __init__(self, name, initial_position, boundaries):
        self.name = name
        self._x = initial_position[0]
        self._y = initial_position[1]
        self._direction_angle = self.CARDINALS_ANGLES.get(initial_position[2])
        self._boundaries = boundaries

    @property
    def current_position(self):
        return f'{self.name}:{self._x} {self._y} {self.direction}'

    @property
    def direction(self):
        return self.ANGLES_CARDINALS.get(self._direction_angle)

    def _rotate(self, angle):
        self._direction_angle = (self._direction_angle + angle) % 360

    def turn_left(self):
        self._rotate(90)

    def turn_right(self):
        self._rotate(-90)

    def __repr__(self):
        return f'{self.name} ({self._x}, {self._y}, {self.direction})'
