import unittest

from day18 import part_1, part_2
from utils import read_input_lines

EXAMPLE_1 = "1 + 2 * 3 + 4 * 5 + 6"
EXAMPLE_2 = "1 + (2 * 3) + (4 * (5 + 6))"

EXAMPLE_3 = "2 * 3 + (4 * 5)"
EXAMPLE_4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
EXAMPLE_5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
EXAMPLE_6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


class Part1Tests(unittest.TestCase):

    def test_with_example_1(self):
        self.assertEqual(part_1(EXAMPLE_1), 71)

    def test_with_example_2(self):
        self.assertEqual(part_1(EXAMPLE_2), 51)

    def test_with_example_3(self):
        self.assertEqual(part_1(EXAMPLE_3), 26)

    def test_with_example_4(self):
        self.assertEqual(part_1(EXAMPLE_4), 437)

    def test_with_example_5(self):
        self.assertEqual(part_1(EXAMPLE_5), 12240)

    def test_with_example_6(self):
        self.assertEqual(part_1(EXAMPLE_6), 13632)

    def test_with_input(self):
        lines = read_input_lines(18)
        self.assertEqual(sum(part_1(line) for line in lines), 650217205854)


class Part2Tests(unittest.TestCase):

    def test_with_example_1(self):
        self.assertEqual(part_2(EXAMPLE_1), 231)

    def test_with_example_2(self):
        self.assertEqual(part_2(EXAMPLE_2), 51)

    def test_with_example_3(self):
        self.assertEqual(part_2(EXAMPLE_3), 46)

    def test_with_example_4(self):
        self.assertEqual(part_2(EXAMPLE_4), 1445)

    def test_with_example_5(self):
        self.assertEqual(part_2(EXAMPLE_5), 669060)

    def test_with_example_6(self):
        self.assertEqual(part_2(EXAMPLE_6), 23340)

    def test_with_input(self):
        lines = read_input_lines(18)
        self.assertEqual(sum(part_2(line) for line in lines), 20394514442037)
