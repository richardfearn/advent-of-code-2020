import unittest

from day16 import part_1, decode_your_ticket, part_2
from utils import read_input_lines

PART_1_EXAMPLE = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

PART_2_EXAMPLE = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(PART_1_EXAMPLE), 71)

    def test_with_input(self):
        lines = read_input_lines(16)
        self.assertEqual(part_1(lines), 21978)


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(decode_your_ticket(PART_2_EXAMPLE), {"class": 12, "row": 11, "seat": 13})

    def test_with_input(self):
        lines = read_input_lines(16)
        self.assertEqual(part_2(lines), 1053686852011)
