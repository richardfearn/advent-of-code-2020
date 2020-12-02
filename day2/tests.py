import unittest

import day2
import utils


EXAMPLE = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):

        lines = EXAMPLE.strip().split("\n")

        self.assertEqual(
            [day2.part_1_is_valid(line) for line in lines],
            [True, False, True]
        )

        self.assertEqual(day2.part_1_valid_passwords(lines), 2)

    def test_with_input(self):
        lines = utils.read_input_lines(2)
        self.assertEqual(day2.part_1_valid_passwords(lines), 638)


class Part2Tests(unittest.TestCase):

    def test_example(self):

        lines = EXAMPLE.strip().split("\n")

        self.assertEqual(
            [day2.part_2_is_valid(line) for line in lines],
            [True, False, False]
        )

    def test_with_input(self):
        lines = utils.read_input_lines(2)
        self.assertEqual(day2.part_2_valid_passwords(lines), 699)
