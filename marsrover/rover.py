#!/usr/bin/env python3
import math
from collections import OrderedDict


class Plateau(object):
    def __init__(self, boundaries):
        self._boundaries = boundaries
        self._x_limit = boundaries[0]
        self._y_limit = boundaries[1]
        self._rovers = OrderedDict()
        self._positions_index = {}

    def deploy_rover(self, rover):
        is_inside_boundaries = self.inside_boundaries(rover)
        is_position_available = self.position_available(rover)

        if is_inside_boundaries and is_position_available:
            rover.plateau = self
            self._rovers[rover.name] = rover
            self._positions_index[(rover.x_pos, rover.y_pos)] = rover

    def get_rover(self, rover_name):
        return self._rovers.get(rover_name)

    def on_rover_move(self, rover, desired_coordinates):
        is_inside_boundaries = self.inside_boundaries(rover, desired_coordinates)
        is_position_available = self.position_available(rover, desired_coordinates)

        return is_inside_boundaries and is_position_available

    def inside_boundaries(self, rover, desired_coordinates=None):
        if desired_coordinates:
            x = desired_coordinates[0]
            y = desired_coordinates[1]
        else:
            x = rover.x_pos
            y = rover.y_pos

        return 0 <= x <= self._x_limit and 0 <= y <= self._y_limit

    def position_available(self, rover, desired_coordinates=None):
        if desired_coordinates:
            x = desired_coordinates[0]
            y = desired_coordinates[1]
        else:
            x = rover.x_pos
            y = rover.y_pos

        for name, deployed_rover in self._rovers.items():
            collision = (deployed_rover.x_pos, deployed_rover.y_pos) == (x, y)
            if rover.name != name and collision:
                return False
        return True

    def deployed_rovers(self):
        return self._rovers.values()


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

    def __init__(self, name, initial_position):
        self.name = name
        self._x = initial_position[0]
        self._y = initial_position[1]
        self._direction_angle = self.CARDINALS_ANGLES.get(initial_position[2])
        self.plateau = None

    @property
    def current_position(self):
        return f'{self.name}:{self.x_pos} {self.y_pos} {self.direction}'

    @property
    def direction(self):
        return self.ANGLES_CARDINALS.get(self._direction_angle)

    @property
    def coordinates(self):
        return self.x_pos, self.y_pos

    @property
    def x_pos(self):
        return self._x

    @property
    def y_pos(self):
        return self._y

    def _rotate(self, angle):
        self._direction_angle = (self._direction_angle + angle) % 360

    def turn_left(self):
        self._rotate(90)

    def turn_right(self):
        self._rotate(-90)

    def move(self):
        new_x = self._x + round(math.cos(math.radians(self._direction_angle)))
        new_y = self._y + round(math.sin(math.radians(self._direction_angle)))

        movement_allowed = self.plateau.on_rover_move(self, (new_x, new_y))
        if movement_allowed:
            self._x = new_x
            self._y = new_y

        return movement_allowed

    def execute_instructions(self, instructions):
        executed = []
        for command in instructions:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                if not self.move():
                    break
            else:  # unrecognized instruction
                continue
            executed.append(command)
        return ''.join(executed)

    def __str__(self):
        return self.current_position
