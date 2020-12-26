import unittest

from day23 import part_1, part_2

EXAMPLE = "389125467"

INPUT = "712643589"


class Part1Tests(unittest.TestCase):

    def test_with_example_10_moves(self):
        self.assertEqual(part_1(EXAMPLE, 10), "92658374")

    def test_with_example_100_moves(self):
        self.assertEqual(part_1(EXAMPLE, 100), "67384529")

    def test_with_input(self):
        self.assertEqual(part_1(INPUT, 100), "29385746")


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_2(EXAMPLE, 10_000_000, True), 149245887792)

    def test_with_input(self):
        self.assertEqual(part_2(INPUT, 10_000_000, True), 680435423892)
