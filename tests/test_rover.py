#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from marsrover.rover import Rover


@pytest.fixture
def rover():
    return Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))


def test_rover_str(rover):
    assert str(rover) == 'RoverX:3 5 N'


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


def test_move(rover):
    rover.move()
    assert rover.current_position == 'RoverX:3 6 N'
    rover.move()
    assert rover.current_position == 'RoverX:3 7 N'


def test_try_move_out_of_bounds(rover):
    # x < 0
    rover.turn_left()
    for _ in range(3):
        rover.move()
    assert rover.current_position == 'RoverX:0 5 W'
    rover.move()
    assert rover.current_position == 'RoverX:0 5 W'

    # y < 0
    rover.turn_left()
    for _ in range(5):
        rover.move()
    assert rover.current_position == 'RoverX:0 0 S'
    rover.move()
    assert rover.current_position == 'RoverX:0 0 S'

    # x > 8
    rover.turn_left()
    for _ in range(8):
        rover.move()
    assert rover.current_position == 'RoverX:8 0 E'
    rover.move()
    assert rover.current_position == 'RoverX:8 0 E'

    # y > 13
    rover.turn_left()
    for _ in range(13):
        rover.move()
    assert rover.current_position == 'RoverX:8 13 N'
    rover.move()
    assert rover.current_position == 'RoverX:8 13 N'


def test_execute_instructions(rover):
    rover.execute_instructions('LMMLMMMMR')
    assert rover.current_position == 'RoverX:1 1 W'

    rover.execute_instructions('RMMMRMMMLMMMMRMMMML')
    assert rover.current_position == 'RoverX:8 8 N'


def test_try_execute_unrecognized_instructions(rover):
    rover.execute_instructions('ABCDEFGHIJKNOPQSTUVWXYZ0123456789')
    assert rover.current_position == 'RoverX:3 5 N'
