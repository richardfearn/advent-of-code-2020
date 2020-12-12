import unittest

from day12 import part_1, part_2
import utils

EXAMPLE = """
F10
N3
F7
R90
F11
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(EXAMPLE), 25)

    def test_with_input(self):
        lines = utils.read_input_lines(12)
        self.assertEqual(part_1(lines), 415)


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_2(EXAMPLE), 286)

    def test_with_input(self):
        lines = utils.read_input_lines(12)
        self.assertEqual(part_2(lines), 29401)
