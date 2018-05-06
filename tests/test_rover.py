#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `marsrover` package."""


from marsrover.rover import Rover


def test_rover_str():
    rover = Rover(name='RoverX', initial_position=(3, 5, 'N'), boundaries=(8, 13))
    assert str(rover) == 'RoverX (3, 5, N)'
