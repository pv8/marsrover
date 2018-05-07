#!/usr/bin/env python3
from collections import OrderedDict

import fileinput

from marsrover import utils
from .rover import Rover


def main():
    fi = fileinput.FileInput()
    boundaries = utils.parse_plateau(fi.readline())
    rovers = OrderedDict()
    errors_count = 0
    for line in fi:
        if not line.strip():
            break
        rover_data = utils.parse_rover_data(line.strip())
        if len(rover_data) == 4:  # Landing
            name, x, y, direction = rover_data
            rovers[name] = Rover(name=name, initial_position=(int(x), int(y), direction),
                                 boundaries=boundaries)
        elif len(rover_data) == 2:  # Instructions
            name, instructions = rover_data
            rover = rovers.get(name)
            if rover:
                rover.execute_instructions(instructions)
            else:
                rovers[f'E{errors_count}'] = f'[ERROR] Rover <{name}> has not been deployed yet!'

    for rover in rovers.values():
        print(rover)


if __name__ == '__main__':
    main()
