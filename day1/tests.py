import unittest

import day1
import utils


EXAMPLE = """
1721
979
366
299
675
1456
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        entries = [int(n) for n in EXAMPLE.split()]
        self.assertEqual(day1.part_1_answer(entries), 514579)

    def test_with_input(self):
        entries = [int(n) for n in utils.read_input_lines(1)]
        self.assertEqual(day1.part_1_answer(entries), 982464)


class Part2Tests(unittest.TestCase):

    def test_example(self):
        entries = [int(n) for n in EXAMPLE.split()]
        self.assertEqual(day1.part_2_answer(entries), 241861950)

    def test_with_input(self):
        entries = [int(n) for n in utils.read_input_lines(1)]
        self.assertEqual(day1.part_2_answer(entries), 162292410)
