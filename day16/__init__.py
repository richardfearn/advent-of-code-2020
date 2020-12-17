from utils import to_lines, group_lines
from math import prod


################################################################################


def parse(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    (rules, your_ticket, nearby_tickets) = group_lines(lines)

    rules = [parse_rule(line) for line in rules]
    your_ticket = parse_ticket(your_ticket[1])
    nearby_tickets = [parse_ticket(line) for line in nearby_tickets[1:]]

    return rules, your_ticket, nearby_tickets


def parse_rule(line):
    (field, ranges) = line.split(": ")
    ranges = ranges.split(" or ")
    ranges = [[int(n) for n in r.split("-")] for r in ranges]
    return field, ranges


def parse_ticket(line):
    return [int(n) for n in line.split(",")]


################################################################################


def part_1(lines):
    rules, your_ticket, nearby_tickets = parse(lines)
    all_ranges = [rule_range for rule in rules for rule_range in rule[1]]
    all_values = [value for ticket in nearby_tickets for value in ticket]
    return sum(value for value in all_values if not valid_value(value, all_ranges))


def valid_value(value, all_ranges):
    return any(rule_range[0] <= value <= rule_range[1] for rule_range in all_ranges)


################################################################################


def decode_your_ticket(lines):
    rules, your_ticket, nearby_tickets = parse(lines)
    field_positions = find_field_positions(rules, nearby_tickets)
    return {field: your_ticket[pos] for (field, pos) in field_positions.items()}


def part_2(lines):
    rules, your_ticket, nearby_tickets = parse(lines)
    field_positions = find_field_positions(rules, nearby_tickets)
    departure_fields = [pos for (field, pos) in field_positions.items() if field.startswith("departure")]
    return prod(your_ticket[pos] for pos in departure_fields)


################################################################################


def find_field_positions(rules, nearby_tickets):

    valid_tickets = all_valid_tickets(rules, nearby_tickets)

    num_fields = len(rules)

    candidates = [find_candidate_fields(rules, valid_tickets, i) for i in range(num_fields)]

    field_positions = {}
    while len(field_positions) < num_fields:

        (pos, field) = find_position_with_one_candidate_field(candidates)
        field_positions[field] = pos

        # that field is no longer a candidate for any other position
        for c in candidates:
            c.discard(field)

    return field_positions


def all_valid_tickets(rules, nearby_tickets):
    all_ranges = [rule_range for rule in rules for rule_range in rule[1]]
    valid_tickets = [t for t in nearby_tickets if valid_ticket(t, all_ranges)]
    return valid_tickets


def valid_ticket(t, all_ranges):
    return all(valid_value(n, all_ranges) for n in t)


def find_candidate_fields(rules, valid_tickets, pos):
    values = [ticket[pos] for ticket in valid_tickets]
    return set(rule[0] for rule in rules if all_values_valid_for_rule(rule, values))


def all_values_valid_for_rule(rule, values):
    return all(valid_value(v, rule[1]) for v in values)


def find_position_with_one_candidate_field(candidates):
    for (pos, fields) in enumerate(candidates):
        if len(fields) == 1:
            return pos, list(fields)[0]
