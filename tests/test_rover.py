#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from marsrover.rover import Rover, Plateau


@pytest.fixture
def plateau():
    return Plateau(boundaries=(8, 13))


@pytest.fixture
def rover(plateau):
    rover = Rover(name='RoverX', initial_position=(3, 5, 'N'))
    plateau.deploy_rover(rover)
    return rover


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
    instructions = 'LMMLMMMMR'
    executed_instructions = rover.execute_instructions(instructions)
    assert rover.current_position == 'RoverX:1 1 W'
    assert executed_instructions == instructions

    instructions = 'RMMMRMMMLMMMMRMMMML'
    executed_instructions = rover.execute_instructions('RMMMRMMMLMMMMRMMMML')
    assert rover.current_position == 'RoverX:8 8 N'
    assert executed_instructions == instructions


def test_try_execute_unrecognized_instructions(rover):
    executed_instructions = rover.execute_instructions('ABCDEFGHIJKNOPQSTUVWXYZ0123456789')
    assert rover.current_position == 'RoverX:3 5 N'
    assert executed_instructions == ''


def test_execute_instructions_with_noise(rover):
    executed_instructions = rover.execute_instructions('LMMxLMMxMMRx')
    assert rover.current_position == 'RoverX:1 1 W'
    assert executed_instructions == 'LMMLMMMMR'


def test_deploy_multiple_rovers(plateau):
    rover_a = Rover(name='RoverA', initial_position=(1, 2, 'N'))
    plateau.deploy_rover(rover_a)
    rover_a.execute_instructions('LMLMLMLMM')
    assert rover_a.current_position == 'RoverA:1 3 N'

    rover_b = Rover(name='RoverB', initial_position=(3, 3, 'E'))
    plateau.deploy_rover(rover_b)
    rover_b.execute_instructions('MMRMMRMRRM')
    assert rover_b.current_position == 'RoverB:5 1 E'

    assert len(plateau.deployed_rovers()) == 2


def test_cannot_add_rover_at_taken_position(plateau):
    rover_a = Rover(name='RoverA', initial_position=(1, 2, 'N'))
    plateau.deploy_rover(rover_a)
    rover_b = Rover(name='RoverB', initial_position=(1, 2, 'E'))
    plateau.deploy_rover(rover_b)
    assert len(plateau.deployed_rovers()) == 1


def test_should_stop_before_collision(plateau):
    rover_a = Rover(name='RoverA', initial_position=(1, 2, 'N'))
    plateau.deploy_rover(rover_a)
    rover_a.execute_instructions('LMLMLMLMM')  # 1 3 N
    assert rover_a.current_position == 'RoverA:1 3 N'

    rover_b = Rover(name='RoverB', initial_position=(3, 3, 'E'))
    plateau.deploy_rover(rover_b)
    executed_instructions = rover_b.execute_instructions('LLMMMRMLM')
    assert rover_b.current_position == 'RoverB:2 3 W'
    assert executed_instructions == 'LLM'

    assert len(plateau.deployed_rovers()) == 2
