import unittest

import day4.parser
import day4.part1
import day4.part2
import utils

PART_1_EXAMPLE = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


PART_2_INVALID_EXAMPLES = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

PART_2_VALID_EXAMPLES = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):

        passports = day4.parser.parse_input(PART_1_EXAMPLE)

        self.assertTrue(day4.part1.is_valid(passports[0]))
        self.assertFalse(day4.part1.is_valid(passports[1]))
        self.assertTrue(day4.part1.is_valid(passports[2]))
        self.assertFalse(day4.part1.is_valid(passports[3]))

        self.assertEqual(day4.part1.count_valid_passports(PART_1_EXAMPLE), 2)

    def test_with_input(self):
        lines = utils.read_input_lines(4)
        self.assertEqual(day4.part1.count_valid_passports(lines), 242)


class Part2Tests(unittest.TestCase):

    def test_field_value_examples(self):

        self.assertTrue(day4.part2.is_valid_byr("2002"))
        self.assertFalse(day4.part2.is_valid_byr("2003"))

        self.assertTrue(day4.part2.is_valid_hgt("60in"))
        self.assertTrue(day4.part2.is_valid_hgt("190cm"))
        self.assertFalse(day4.part2.is_valid_hgt("190in"))
        self.assertFalse(day4.part2.is_valid_hgt("190"))

        self.assertTrue(day4.part2.is_valid_hcl("#123abc"))
        self.assertFalse(day4.part2.is_valid_hcl("#123abz"))
        self.assertFalse(day4.part2.is_valid_hcl("123abc"))

        self.assertTrue(day4.part2.is_valid_ecl("brn"))
        self.assertFalse(day4.part2.is_valid_ecl("wat"))

        self.assertTrue(day4.part2.is_valid_pid("000000001"))
        self.assertFalse(day4.part2.is_valid_pid("0123456789"))

        # For full coverage of is_valid_year
        self.assertFalse(day4.part2.is_valid_iyr("12345"))

    def test_invalid_examples(self):
        passports = day4.parser.parse_input(PART_2_INVALID_EXAMPLES)
        for p in passports:
            self.assertFalse(day4.part2.is_valid(p))

    def test_valid_examples(self):
        passports = day4.parser.parse_input(PART_2_VALID_EXAMPLES)
        for p in passports:
            self.assertTrue(day4.part2.is_valid(p))

    def test_with_input(self):
        lines = utils.read_input_lines(4)
        self.assertEqual(day4.part2.count_valid_passports(lines), 186)
