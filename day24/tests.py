import unittest

from day24 import part_1, part_2, part_2_multiple_days
from utils import read_input_lines, non_blank_lines

EXAMPLE = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

PART_2_COUNTS = """
Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(EXAMPLE), 10)

    def test_with_input(self):
        lines = read_input_lines(24)
        self.assertEqual(part_1(lines), 322)


class Part2Tests(unittest.TestCase):

    def test_with_example(self):

        expected_counts = non_blank_lines(PART_2_COUNTS)
        expected_counts = [c[4:].split(": ") for c in expected_counts]
        expected_counts = {int(c[0]): int(c[1]) for c in expected_counts}

        actual_counts = part_2_multiple_days(EXAMPLE, expected_counts.keys())
        self.assertEqual(expected_counts, actual_counts)

    def test_with_input(self):
        lines = read_input_lines(24)
        self.assertEqual(part_2(lines), 3831)
