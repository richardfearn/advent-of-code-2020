import unittest

import day7
import utils

EXAMPLE_1 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

EXAMPLE_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(day7.part_1(EXAMPLE_1), 4)

    def test_with_input(self):
        lines = utils.read_input_lines(7)
        self.assertEqual(day7.part_1(lines), 248)


class Part2Tests(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(day7.part_2(EXAMPLE_1), 32)

    def test_second_example(self):
        self.assertEqual(day7.part_2(EXAMPLE_2), 126)

    def test_with_input(self):
        lines = utils.read_input_lines(7)
        self.assertEqual(day7.part_2(lines), 57281)
