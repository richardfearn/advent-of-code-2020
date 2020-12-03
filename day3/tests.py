import unittest

import day3
import utils

EXAMPLE = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(day3.count_trees(EXAMPLE, (3, 1)), 7)

    def test_with_input(self):
        tree_map = utils.read_input(3)
        self.assertEqual(day3.count_trees(tree_map, slope=(3, 1)), 151)


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(day3.count_trees(EXAMPLE, (1, 1)), 2)
        self.assertEqual(day3.count_trees(EXAMPLE, (3, 1)), 7)
        self.assertEqual(day3.count_trees(EXAMPLE, (5, 1)), 3)
        self.assertEqual(day3.count_trees(EXAMPLE, (7, 1)), 4)
        self.assertEqual(day3.count_trees(EXAMPLE, (1, 2)), 2)
        self.assertEqual(day3.part_2(EXAMPLE), 336)

    def test_with_input(self):
        tree_map = utils.read_input(3)
        self.assertEqual(day3.part_2(tree_map), 7540141059)
