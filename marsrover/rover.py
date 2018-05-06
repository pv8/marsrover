#!/usr/bin/env python3
import math


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

    def is_inside_boundaries(self, new_x, new_y):
        inside_limit_x = 0 <= new_x <= self._boundaries[0]
        inside_limit_y = 0 <= new_y <= self._boundaries[1]
        return inside_limit_x and inside_limit_y

    def move(self):
        new_x = self._x + round(math.cos(math.radians(self._direction_angle)))
        new_y = self._y + round(math.sin(math.radians(self._direction_angle)))

        # only move rover if it's inside the limits
        if self.is_inside_boundaries(new_x, new_y):
            self._x = new_x
            self._y = new_y

    def execute_instructions(self, instructions):
        for command in instructions:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move()

    def __repr__(self):
        return f'{self.name} ({self._x}, {self._y}, {self.direction})'
