import unittest

import day9
import utils

EXAMPLE = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


class Part1Tests(unittest.TestCase):

    def test_is_valid_with_1_to_25_preamble(self):
        preamble = set(range(1, 26))
        self.assertTrue(day9.is_valid(preamble, 26))
        self.assertTrue(day9.is_valid(preamble, 49))
        self.assertFalse(day9.is_valid(preamble, 100))
        self.assertFalse(day9.is_valid(preamble, 50))

    def test_is_valid_with_preamble_plus_45(self):
        previous_numbers = set(list(range(1, 20)) + list(range(21, 26)) + [45])
        self.assertTrue(day9.is_valid(previous_numbers, 26))
        self.assertFalse(day9.is_valid(previous_numbers, 65))
        self.assertTrue(day9.is_valid(previous_numbers, 64))
        self.assertTrue(day9.is_valid(previous_numbers, 66))

    def test_example(self):
        self.assertEqual(day9.part_1(EXAMPLE, 5), 127)

    def test_with_input(self):
        lines = utils.read_input_lines(9)
        self.assertEqual(day9.part_1(lines, 25), 26134589)


class Part2Tests(unittest.TestCase):

    def test_example(self):
        invalid_number = 127
        self.assertEqual(day9.find_range(EXAMPLE, invalid_number), [15, 25, 47, 40])
        self.assertEqual(day9.part_2(EXAMPLE, invalid_number), 62)

    def test_with_input(self):
        invalid_number = 26134589
        lines = utils.read_input_lines(9)
        self.assertEqual(day9.part_2(lines, invalid_number), 3535124)
