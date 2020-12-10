import unittest

import day8
from day8 import JMP, NOP, LOOP, TERMINATED
import utils

EXAMPLE = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

UNCORRECTABLE_PROGRAM = """
jmp 0
jmp 0
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(day8.part_1(EXAMPLE), 5)

    def test_with_input(self):
        lines = utils.read_input_lines(8)
        self.assertEqual(day8.part_1(lines), 1727)


class Part2Tests(unittest.TestCase):

    def test_example_with_first_instruction_changed(self):
        instructions = day8.parse(EXAMPLE)
        instructions[0][0] = JMP
        self.assertEqual(day8.execute(instructions)[0], LOOP)

    def test_example_with_second_to_last_instruction_changed(self):
        instructions = day8.parse(EXAMPLE)
        instructions[-2][0] = NOP
        self.assertEqual(day8.execute(instructions), (TERMINATED, 8))

    def test_with_example(self):
        self.assertEqual(day8.part_2(EXAMPLE), 8)

    def test_with_input(self):
        lines = utils.read_input_lines(8)
        self.assertEqual(day8.part_2(lines), 552)

    def test_exception_is_raised_for_uncorrectable_program(self):
        with self.assertRaises(Exception) as context:
            day8.part_2(UNCORRECTABLE_PROGRAM)
        self.assertEqual("infinite loop", str(context.exception))


class GraphvizTests(unittest.TestCase):

    def test_graphviz_for_example(self):
        day8.graphviz(EXAMPLE, "example")

    def test_graphviz_for_input(self):
        lines = utils.read_input_lines(8)
        day8.graphviz(lines, "input")

    def test_graphviz_for_uncorrectable(self):
        day8.graphviz(UNCORRECTABLE_PROGRAM, "uncorrectable")
