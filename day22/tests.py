import unittest

from day22 import part_1, part_2
from utils import read_input_lines

EXAMPLE = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(EXAMPLE), 306)

    def test_with_input(self):
        lines = read_input_lines(22)
        self.assertEqual(part_1(lines), 31455)


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_2(EXAMPLE), 291)

    def test_with_input(self):
        lines = read_input_lines(22)
        self.assertEqual(part_2(lines), 32528)
