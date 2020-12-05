import unittest

import day5
import utils

EXAMPLE_1 = "FBFBBFFRLR"

EXAMPLE_2 = "BFFFBBFRRR"
EXAMPLE_3 = "FFFBBBFRRR"
EXAMPLE_4 = "BBFFBBFRLL"


class Part1Tests(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(day5.seat_number(EXAMPLE_1), (44, 5))
        self.assertEqual(day5.seat_id(EXAMPLE_1), 357)

    def test_other_examples(self):

        self.assertEqual(day5.seat_number(EXAMPLE_2), (70, 7))
        self.assertEqual(day5.seat_id(EXAMPLE_2), 567)

        self.assertEqual(day5.seat_number(EXAMPLE_3), (14, 7))
        self.assertEqual(day5.seat_id(EXAMPLE_3), 119)

        self.assertEqual(day5.seat_number(EXAMPLE_4), (102, 4))
        self.assertEqual(day5.seat_id(EXAMPLE_4), 820)

    def test_with_input(self):
        boarding_passes = utils.read_input(5)
        self.assertEqual(day5.part_1(boarding_passes), 801)


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        boarding_passes = utils.read_input(5)
        self.assertEqual(day5.part_2(boarding_passes), 597)
