#!/usr/bin/env python3

import re


PLATEAU_PATTERN = re.compile(r'Plateau:(\d+) (\d+)')
ROVER_LANDING_PATTERN = re.compile(r'(\w+) Landing:(\d+) (\d+) ([NSWE])')
ROVER_INSTRUCTIONS_PATTERN = re.compile(r'(\w+) Instructions:([LMR]+)')


def _match_input(pattern, input_line):
    m = pattern.match(input_line)
    if m:
        return m.groups()


def parse_plateau(input_line):
    data = _match_input(PLATEAU_PATTERN, input_line)
    return int(data[0]), int(data[1])


def parse_rover_data(input_line):
    data = _match_input(ROVER_LANDING_PATTERN, input_line)
    if data:
        return data[0], int(data[1]), int(data[2]), data[3]
    return _match_input(ROVER_INSTRUCTIONS_PATTERN, input_line)
