import re
from collections import namedtuple

ColourAndCount = namedtuple("ColorAndCount", ["colour", "count"])

SHINY_GOLD = "shiny gold"


def part_1(lines):

    graph = invert(parse_graph(lines))

    seen = set()
    explore = [SHINY_GOLD]

    while len(explore) > 0:
        current_colour = explore.pop(0)
        seen.add(current_colour)
        next_colours = graph[current_colour]
        explore = explore + next_colours

    return len(seen) - 1  # don't include "shiny gold" itself


def invert(graph):

    """Invert the graph. Instead of representing what each bag contains, the
    new graph represents which other bags contain each colour of bag."""

    inverted = {}

    for colour in graph.keys():
        inverted[colour] = []

    for colour, contents in graph.items():
        for other_bag in contents:
            inverted[other_bag.colour].append(colour)  # discard the counts - not needed for part 1

    return inverted


def part_2(lines):
    graph = parse_graph(lines)
    return total_bags(graph, SHINY_GOLD)


def total_bags(graph, colour):
    return sum(bag.count * (1 + total_bags(graph, bag.colour)) for bag in graph[colour])


def parse_graph(lines):

    if isinstance(lines, str):
        lines = lines.strip().split("\n")

    graph = {}

    for line in lines:
        bits = line.split(" contain ")
        colour = bits[0][:-5]
        contents = re.findall(r"([0-9]+) (\w+ \w+) bag", bits[1])
        graph[colour] = [ColourAndCount(bag[1], int(bag[0])) for bag in contents]

    return graph
