#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from marsrover.rover import Rover


@pytest.fixture
def rover():
    return Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))


def test_rover_str(rover):
    assert str(rover) == 'RoverX (3, 5, N)'


def test_rover_current_position(rover):
    assert rover.current_position == 'RoverX:3 5 N'


def test_rover_turn_left(rover):
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 W'
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 S'
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 E'
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 N'


def test_rover_turn_right(rover):
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 E'
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 S'
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 W'
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 N'
