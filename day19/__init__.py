from utils import to_lines, group_lines
import re
from itertools import groupby


def part_1_single(rules, message):
    rules = to_lines(rules)
    rules = process_rules(rules)
    regex = rules[0]
    return re.fullmatch(regex, message) is not None


def part_1(lines):
    (rules, messages) = parse_rules_and_messages(lines)
    rules = process_rules(rules)
    regex = rules[0]
    return [re.fullmatch(regex, m) is not None for m in messages].count(True)


def parse_rules_and_messages(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    return group_lines(lines)


def part_2(lines):
    (rules, messages) = parse_rules_and_messages(lines)
    rules = process_rules(rules, skip={42, 31})
    return [part_2_match(rules, m) for m in messages].count(True)


def part_2_match(rules, msg):

    # Use 'x' and 'y' to denote strings that match rules 42/31 respectively
    token_42 = "x"
    token_31 = "y"

    replacements = {
        42: token_42,
        31: token_31,
    }

    pieces = []
    while len(msg) > 0:
        for (num, replacement) in replacements.items():
            full_regex = "(?P<piece>%s)(?P<rest>.*)" % rules[num]
            m = re.fullmatch(full_regex, msg)
            if m is not None:
                pieces.append(replacement)
                msg = m.group("rest")

    groups = [(piece, len(list(pieces))) for (piece, pieces) in groupby(pieces)]
    return (len(groups) == 2) and \
           (groups[0][0] == token_42) and (groups[1][0] == token_31) and \
           (groups[0][1] > groups[1][1])


def process_rules(rules, skip=None):

    if skip is None:
        skip = {}

    rules = [r.split(": ") for r in rules]
    rules = {int(r[0]): r[1].split(" ") for r in rules}

    # Convert any numbers to ints
    for rule in rules.values():
        for i in range(len(rule)):
            try:
                rule[i] = int(rule[i])
            except ValueError:
                pass

    # Replace a terminal symbol in a list with the symbol itself
    for (num, rule) in rules.items():
        if (len(rule) == 1) and isinstance(rule[0], str):
            rules[num] = rule[0][1]  # just the character - no apostrophes

    # Repeatedly inline rules that don't refer to other rules
    finished = False
    while not finished:

        # Find a rule that just has a string on the RHS
        pos = None
        for (num, rule) in rules.items():
            if (num != 0) and (num not in skip) and isinstance(rule, str):
                pos = num
                break

        # Substitute it into other rules that use it
        if pos is not None:
            regex = "(" + rules[pos] + ")"
            for (num, rule) in rules.items():
                if isinstance(rule, list):
                    for i in range(len(rule)):
                        if rule[i] == pos:
                            rule[i] = regex
                    # If rule no longer refers to other rules, convert to regex
                    if all(isinstance(token, str) for token in rule):
                        rules[num] = "".join(rule)
            rules.pop(pos)

        else:
            finished = True

    return rules
