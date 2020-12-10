import unittest

import day10
import utils

EXAMPLE_1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

EXAMPLE_2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(day10.part_1_counts(EXAMPLE_1), (7, 5))

    def test_example_2(self):
        self.assertEqual(day10.part_1_counts(EXAMPLE_2), (22, 10))

    def test_with_input(self):
        joltages = utils.read_input_lines(10)
        self.assertEqual(day10.part_1(joltages), 2310)


class Part2Tests(unittest.TestCase):

    def test_example_tiny(self):
        joltages = [1, 4, 5, 6]
        self.assertEqual(day10.part_2(joltages), 2)

    def test_example_1(self):
        self.assertEqual(day10.part_2(EXAMPLE_1), 8)

    def test_example_2(self):
        self.assertEqual(day10.part_2(EXAMPLE_2), 19208)

    def test_with_input(self):
        joltages = utils.read_input_lines(10)
        self.assertEqual(day10.part_2(joltages), 64793042714624)
