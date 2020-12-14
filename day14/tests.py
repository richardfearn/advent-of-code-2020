import unittest

from day14 import part_1, part_2, actual_addresses
from utils import read_input_lines

PART_1_EXAMPLE = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

PART_2_EXAMPLE = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(PART_1_EXAMPLE), 165)

    def test_with_input(self):
        program = read_input_lines(14)
        self.assertEqual(part_1(program), 12610010960049)


class Part2Tests(unittest.TestCase):

    def test_actual_addresses_1(self):
        self.assertEqual(actual_addresses("000000000000000000000000000000X1101X"), [26, 27, 58, 59])

    def test_actual_addresses_2(self):
        self.assertEqual(actual_addresses("00000000000000000000000000000001X0XX"), [16, 17, 18, 19, 24, 25, 26, 27])

    def test_with_example(self):
        self.assertEqual(part_2(PART_2_EXAMPLE), 208)

    def test_with_input(self):
        program = read_input_lines(14)
        self.assertEqual(part_2(program), 3608464522781)
