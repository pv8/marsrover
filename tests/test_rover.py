#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `marsrover` package."""


from marsrover.rover import Rover


def test_rover_str():
    rover = Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))
    assert str(rover) == 'RoverX (3, 5, N)'


def test_rover_current_position():
    rover = Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))
    assert rover.current_position == 'RoverX:3 5 N'


def test_rover_turn_left():
    rover = Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 W'
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 S'
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 E'
    rover.turn_left()
    assert rover.current_position == 'RoverX:3 5 N'


def test_rover_turn_right():
    rover = Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 E'
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 S'
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 W'
    rover.turn_right()
    assert rover.current_position == 'RoverX:3 5 N'
