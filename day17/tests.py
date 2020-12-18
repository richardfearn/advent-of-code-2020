import unittest

from day17 import part_1, part_2
from utils import read_input_lines

PART_1_EXAMPLE = """
.#.
..#
###
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(PART_1_EXAMPLE), 112)

    def test_with_input(self):
        lines = read_input_lines(17)
        self.assertEqual(part_1(lines), 223)


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_2(PART_1_EXAMPLE), 848)

    def test_with_input(self):
        lines = read_input_lines(17)
        self.assertEqual(part_2(lines), 1884)
