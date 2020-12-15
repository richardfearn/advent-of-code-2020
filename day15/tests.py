import unittest

from day15 import generate

PUZZLE_INPUT = [0, 14, 1, 3, 7, 9]

PART_1_EXAMPLE = [0, 3, 6]
PART_1_LENGTH = 2020

PART_2_LENGTH = 30000000


class Part1Tests(unittest.TestCase):

    def test_with_example_1(self):
        actual = [generate(PART_1_EXAMPLE, n) for n in range(4, 11)]
        self.assertEqual(actual, [0, 3, 3, 1, 0, 4, 0])

    def test_with_other_examples(self):
        self.assertEqual(generate([1, 3, 2], PART_1_LENGTH), 1)
        self.assertEqual(generate([2, 1, 3], PART_1_LENGTH), 10)
        self.assertEqual(generate([1, 2, 3], PART_1_LENGTH), 27)
        self.assertEqual(generate([2, 3, 1], PART_1_LENGTH), 78)
        self.assertEqual(generate([3, 2, 1], PART_1_LENGTH), 438)
        self.assertEqual(generate([3, 1, 2], PART_1_LENGTH), 1836)

    def test_with_input(self):
        self.assertEqual(generate(PUZZLE_INPUT, PART_1_LENGTH), 763)


class Part2Tests(unittest.TestCase):

    def test_with_examples(self):
        self.assertEqual(generate([0, 3, 6], PART_2_LENGTH), 175594)
        self.assertEqual(generate([1, 3, 2], PART_2_LENGTH), 2578)
        self.assertEqual(generate([2, 1, 3], PART_2_LENGTH), 3544142)
        self.assertEqual(generate([1, 2, 3], PART_2_LENGTH), 261214)
        self.assertEqual(generate([2, 3, 1], PART_2_LENGTH), 6895259)
        self.assertEqual(generate([3, 2, 1], PART_2_LENGTH), 18)
        self.assertEqual(generate([3, 1, 2], PART_2_LENGTH), 362)

    def test_with_input(self):
        self.assertEqual(generate(PUZZLE_INPUT, PART_2_LENGTH), 1876406)
