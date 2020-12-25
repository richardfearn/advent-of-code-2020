import unittest

from day25 import part_1
from utils import read_input_lines

EXAMPLE = [5764801, 17807724]


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(EXAMPLE), 14897079)

    def test_with_input(self):
        lines = read_input_lines(25)
        self.assertEqual(part_1(lines), 297257)
