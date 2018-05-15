#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import ExitStack
from io import StringIO

from unittest import mock

from marsrover.cli import main


class MockFileInputBase(object):
    def __init__(self):
        self.input_data = None

    def __next__(self):
        if len(self.input_data) == 0:
            raise StopIteration
        return self.input_data.pop(0)

    def __iter__(self):
        return self

    def readline(self):
        return self.input_data.pop(0)


def assert_mock_input(mock_class, expected_output):
    with ExitStack() as stack:
        stack.enter_context(mock.patch('fileinput.FileInput', new=mock_class))
        mock_stdout = stack.enter_context(mock.patch('sys.stdout', new_callable=StringIO))

        main()
        assert mock_stdout.getvalue() == expected_output


def test_cli_default_input():
    class MockFileInput(MockFileInputBase):
        def __init__(self):
            super().__init__()
            self.input_data = [
                'Plateau:5 5',
                'Rover1 Landing:1 2 N',
                'Rover1 Instructions:LMLMLMLMM',
                'Rover2 Landing:3 3 E',
                'Rover2 Instructions:MMRMMRMRRM',
            ]

    expected_output = (
        'Rover1:1 3 N\n'
        'Rover2:5 1 E\n'
    )

    assert_mock_input(MockFileInput, expected_output)


def test_cli_input_with_blank_line():
    class MockFileInput(MockFileInputBase):
        def __init__(self):
            super().__init__()
            self.input_data = [
                'Plateau:5 5',
                'Rover1 Landing:1 2 N',
                'Rover1 Instructions:LMLMLMLMM',
                '',
                'Rover2 Landing:3 3 E',
                'Rover2 Instructions:MMRMMRMRRM',
            ]

    expected_output = (
        'Rover1:1 3 N\n'
    )

    assert_mock_input(MockFileInput, expected_output)


def test_cli_input_with_instructions_error():
    class MockFileInput(MockFileInputBase):
        def __init__(self):
            super().__init__()
            self.input_data = [
                'Plateau:5 5',
                'Rover1 Landing:1 2 N',
                'Rover1 Instructions:LMLMLMLMM',
                'Rover2 Instructions:MMRMMRMRRM',
                'Rover2 Landing:3 3 E',
                'Rover2 Instructions:MMRMMRMRRM',
            ]

    expected_output = (
        'Rover1:1 3 N\n'
        '[ERROR] Rover <Rover2> has not been deployed yet!\n'
        'Rover2:5 1 E\n'
    )

    assert_mock_input(MockFileInput, expected_output)


def test_landing_rover_on_taken_position():
    class MockFileInput(MockFileInputBase):
        def __init__(self):
            super().__init__()
            self.input_data = [
                'Plateau:5 5',
                'Rover1 Landing:1 2 N',
                'Rover2 Landing:1 2 E',
            ]

    expected_output = (
        'Rover1:1 2 N\n'
        '[ERROR] Rover <Rover2> cannot be deployed on (1, 2)!\n'
    )
    assert_mock_input(MockFileInput, expected_output)
