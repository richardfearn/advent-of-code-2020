from collections import namedtuple
import re

REGEX = "(\\d+)-(\\d+) ([a-z]): ([a-z]+)"

Policy = namedtuple("Policy", ["lowest", "highest", "letter"])


def parse(line):

    m = re.fullmatch(REGEX, line)

    lowest = int(m.group(1))
    highest = int(m.group(2))
    letter = m.group(3)
    policy = Policy(lowest, highest, letter)

    password = m.group(4)

    return policy, password


def part_1_valid_passwords(lines):
    return count_matching_lines(lines, part_1_is_valid)


def part_1_is_valid(line):
    (policy, password) = parse(line)
    count = password.count(policy.letter)
    return policy.lowest <= count <= policy.highest


def part_2_valid_passwords(lines):
    return count_matching_lines(lines, part_2_is_valid)


def part_2_is_valid(line):
    (policy, password) = parse(line)
    first_pos_matches = (password[policy.lowest - 1] == policy.letter)
    second_pos_matches = (password[policy.highest - 1] == policy.letter)
    return first_pos_matches ^ second_pos_matches


def count_matching_lines(lines, pred):
    return sum(1 for line in lines if pred(line))
