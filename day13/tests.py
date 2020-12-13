import unittest

from day13 import part_1, part_2
from utils import to_lines, read_input_lines

PART_1_EXAMPLE = """
939
7,13,x,x,59,x,31,19
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(PART_1_EXAMPLE), 295)

    def test_with_input(self):
        lines = read_input_lines(13)
        self.assertEqual(part_1(lines), 259)


class Part2Tests(unittest.TestCase):

    def test_with_part_1_example(self):
        bus_ids = to_lines(PART_1_EXAMPLE)[1]
        self.assertEqual(part_2(bus_ids), 1068781)

    def test_with_part_2_example_1(self):
        self.assertEqual(part_2("17,x,13,19"), 3417)

    def test_with_part_2_example_2(self):
        self.assertEqual(part_2("67,7,59,61"), 754018)

    def test_with_part_2_example_3(self):
        self.assertEqual(part_2("67,x,7,59,61"), 779210)

    def test_with_part_2_example_4(self):
        self.assertEqual(part_2("67,7,x,59,61"), 1261476)

    def test_with_part_2_example_5(self):
        self.assertEqual(part_2("1789,37,47,1889"), 1202161486)

    def test_with_input(self):
        bus_ids = read_input_lines(13)[1]
        self.assertEqual(part_2(bus_ids), 210612924879242)
