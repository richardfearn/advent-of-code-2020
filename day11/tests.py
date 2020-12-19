import unittest

from day11 import part_1_step_text, part_1
from day11 import part_2_text_count_visible, part_2_step_text, part_2
from day11 import text_count_occupied_seats, EMPTY, OCCUPIED
import utils

EXAMPLE_INITIAL_LAYOUT = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

PART_1_EXAMPLE_AFTER_1_ROUND = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""

PART_1_EXAMPLE_AFTER_2_ROUNDS = """
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
"""

PART_1_EXAMPLE_AFTER_3_ROUNDS = """
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
"""

PART_1_EXAMPLE_AFTER_4_ROUNDS = """
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
"""

PART_1_EXAMPLE_AFTER_5_ROUNDS = """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
"""

PART_2_EXAMPLE_1 = """
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""

PART_2_EXAMPLE_2 = """
.............
.L.L.#.#.#.#.
.............
"""

PART_2_EXAMPLE_3 = """
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
"""

PART_2_EXAMPLE_AFTER_1_ROUND = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""

PART_2_EXAMPLE_AFTER_2_ROUNDS = """
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
"""

PART_2_EXAMPLE_AFTER_3_ROUNDS = """
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
"""

PART_2_EXAMPLE_AFTER_4_ROUNDS = """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
"""

PART_2_EXAMPLE_AFTER_5_ROUNDS = """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
"""

PART_2_EXAMPLE_AFTER_6_ROUNDS = """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(part_1_step_text(EXAMPLE_INITIAL_LAYOUT), PART_1_EXAMPLE_AFTER_1_ROUND.strip())
        self.assertEqual(part_1_step_text(PART_1_EXAMPLE_AFTER_1_ROUND), PART_1_EXAMPLE_AFTER_2_ROUNDS.strip())
        self.assertEqual(part_1_step_text(PART_1_EXAMPLE_AFTER_2_ROUNDS), PART_1_EXAMPLE_AFTER_3_ROUNDS.strip())
        self.assertEqual(part_1_step_text(PART_1_EXAMPLE_AFTER_3_ROUNDS), PART_1_EXAMPLE_AFTER_4_ROUNDS.strip())
        self.assertEqual(part_1_step_text(PART_1_EXAMPLE_AFTER_4_ROUNDS), PART_1_EXAMPLE_AFTER_5_ROUNDS.strip())
        self.assertEqual(part_1_step_text(PART_1_EXAMPLE_AFTER_5_ROUNDS), PART_1_EXAMPLE_AFTER_5_ROUNDS.strip())
        self.assertEqual(text_count_occupied_seats(PART_1_EXAMPLE_AFTER_5_ROUNDS), 37)

    def test_with_input(self):
        layout = utils.read_input_lines(11)
        self.assertEqual(part_1(layout), 2470)


class Part2Tests(unittest.TestCase):

    def test_counts(self):
        self.assertEqual(part_2_text_count_visible(PART_2_EXAMPLE_1, 3, 4), {EMPTY: 0, OCCUPIED: 8})
        self.assertEqual(part_2_text_count_visible(PART_2_EXAMPLE_2, 1, 1), {EMPTY: 1, OCCUPIED: 0})
        self.assertEqual(part_2_text_count_visible(PART_2_EXAMPLE_3, 3, 3), {EMPTY: 0, OCCUPIED: 0})

    def test_example(self):
        self.assertEqual(part_2_step_text(EXAMPLE_INITIAL_LAYOUT), PART_2_EXAMPLE_AFTER_1_ROUND.strip())
        self.assertEqual(part_2_step_text(PART_2_EXAMPLE_AFTER_1_ROUND), PART_2_EXAMPLE_AFTER_2_ROUNDS.strip())
        self.assertEqual(part_2_step_text(PART_2_EXAMPLE_AFTER_2_ROUNDS), PART_2_EXAMPLE_AFTER_3_ROUNDS.strip())
        self.assertEqual(part_2_step_text(PART_2_EXAMPLE_AFTER_3_ROUNDS), PART_2_EXAMPLE_AFTER_4_ROUNDS.strip())
        self.assertEqual(part_2_step_text(PART_2_EXAMPLE_AFTER_4_ROUNDS), PART_2_EXAMPLE_AFTER_5_ROUNDS.strip())
        self.assertEqual(part_2_step_text(PART_2_EXAMPLE_AFTER_5_ROUNDS), PART_2_EXAMPLE_AFTER_6_ROUNDS.strip())
        self.assertEqual(part_2_step_text(PART_2_EXAMPLE_AFTER_6_ROUNDS), PART_2_EXAMPLE_AFTER_6_ROUNDS.strip())
        self.assertEqual(text_count_occupied_seats(PART_2_EXAMPLE_AFTER_6_ROUNDS), 26)

    def test_with_input(self):
        layout = utils.read_input_lines(11)
        self.assertEqual(part_2(layout), 2259)
