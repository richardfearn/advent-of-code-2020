import unittest

import day6
import utils

EXAMPLE_1 = """
abcx
abcy
abcz
"""

EXAMPLE_2 = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


class Part1Tests(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(day6.count_questions_part_1(EXAMPLE_1.split()), 6)

    def test_second_example(self):

        groups = utils.group_lines(EXAMPLE_2)

        self.assertEqual(
            [day6.count_questions_part_1(g) for g in groups],
            [3, 3, 3, 1, 1]
        )

        self.assertEqual(day6.part_1(EXAMPLE_2), 11)

    def test_with_input(self):
        lines = utils.read_input_lines(6)
        self.assertEqual(day6.part_1(lines), 6885)


class Part2Tests(unittest.TestCase):

    def test_second_example(self):

        groups = utils.group_lines(EXAMPLE_2)

        self.assertEqual(
            [day6.count_questions_part_2(g) for g in groups],
            [3, 0, 1, 1, 1]
        )

        self.assertEqual(day6.part_2(EXAMPLE_2), 6)

    def test_with_input(self):
        lines = utils.read_input_lines(6)
        self.assertEqual(day6.part_2(lines), 3550)
