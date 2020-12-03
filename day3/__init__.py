from collections import namedtuple
import math

TREE = "#"

Point = namedtuple("Point", ["x", "y"])


def count_trees(tree_map, slope):

    if isinstance(tree_map, str):
        tree_map = tree_map.split()

    height = len(tree_map)
    width = len(tree_map[0])

    num_trees = 0
    current_pos = Point(0, 0)

    while current_pos.y < height:

        if tree_map[current_pos.y][current_pos.x % width] == TREE:
            num_trees += 1

        current_pos = Point(current_pos.x + slope[0], current_pos.y + slope[1])

    return num_trees


def part_2(tree_map):

    if isinstance(tree_map, str):
        tree_map = tree_map.split()

    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )

    return math.prod(count_trees(tree_map, slope) for slope in slopes)
