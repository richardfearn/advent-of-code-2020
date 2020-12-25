import unittest

from day21 import part_1, part_2, parse, find_ingredients_and_allergens
from utils import read_input_lines

EXAMPLE = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


class Part1Tests(unittest.TestCase):

    def test_with_example(self):
        self.assertEqual(part_1(EXAMPLE), 5)

    def test_with_input(self):
        lines = read_input_lines(21)
        self.assertEqual(part_1(lines), 2517)


class Part2Tests(unittest.TestCase):

    def test_find_ingredients_and_allergens_with_example(self):
        foods = parse(EXAMPLE)
        actual = find_ingredients_and_allergens(foods)
        expected = {"mxmxvkd": "dairy", "sqjhc": "fish", "fvjkl": "soy"}
        self.assertEqual(expected, actual)

    def test_with_example(self):
        self.assertEqual(part_2(EXAMPLE), "mxmxvkd,sqjhc,fvjkl")

    def test_with_input(self):
        lines = read_input_lines(21)
        self.assertEqual(part_2(lines), "rhvbn,mmcpg,kjf,fvk,lbmt,jgtb,hcbdb,zrb")
