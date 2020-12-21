import unittest

from day19 import part_1_single, part_1, part_2
from utils import read_input_lines

PART_1_EXAMPLE_1 = """
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
"""

PART_1_EXAMPLE_2 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
"""

PART_1_EXAMPLE_2_VALID = """
aaaabb
aaabab
abbabb
abbbab
aabaab
aabbbb
abaaab
ababbb
"""

PART_1_EXAMPLE_3 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

PART_2_EXAMPLE = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""


class Part1Tests(unittest.TestCase):

    def test_with_example_1(self):
        self.assertTrue(part_1_single(PART_1_EXAMPLE_1, "aab"))
        self.assertTrue(part_1_single(PART_1_EXAMPLE_1, "aba"))

    def test_with_example_2(self):
        for message in PART_1_EXAMPLE_2_VALID.strip().split("\n"):
            self.assertTrue(part_1_single(PART_1_EXAMPLE_2, message))

    def test_with_example_3(self):
        self.assertEqual(part_1(PART_1_EXAMPLE_3), 2)

    def test_with_input(self):
        lines = read_input_lines(19)
        self.assertEqual(part_1(lines), 115)


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_2(PART_2_EXAMPLE), 12)

    def test_with_input(self):
        lines = read_input_lines(19)
        self.assertEqual(part_2(lines), 237)
