# Useful: https://www.redblobgames.com/grids/hexagons/

from utils import to_lines
import re
from collections import namedtuple

DIRECTION_REGEX = r"e|se|sw|w|nw|ne"


class Tile(namedtuple("Point", ["x", "y"])):

    def e(self):
        return Tile(self.x + 2, self.y)

    def se(self):
        return Tile(self.x + 1, self.y + 1)

    def sw(self):
        return Tile(self.x - 1, self.y + 1)

    def w(self):
        return Tile(self.x - 2, self.y)

    def nw(self):
        return Tile(self.x - 1, self.y - 1)

    def ne(self):
        return Tile(self.x + 1, self.y - 1)


def part_1(lines):
    black_tiles = flip_tiles(lines)
    return len(black_tiles)


def flip_tiles(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    tiles = [re.findall(DIRECTION_REGEX, line) for line in lines]

    black_tiles = set()

    for tile in tiles:

        pos = Tile(0, 0)

        for move in tile:
            if move == "e":
                pos = pos.e()
            elif move == "se":
                pos = pos.se()
            elif move == "sw":
                pos = pos.sw()
            elif move == "w":
                pos = pos.w()
            elif move == "nw":
                pos = pos.nw()
            elif move == "ne":
                pos = pos.ne()

        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)

    return black_tiles


def part_2_multiple_days(lines, days):

    black_tiles = flip_tiles(lines)

    counts = {}
    for day in range(1, max(days) + 1):
        black_tiles = run(black_tiles)
        if day in days:
            counts[day] = len(black_tiles)

    return counts


def part_2(lines):

    black_tiles = flip_tiles(lines)

    for day in range(100):
        black_tiles = run(black_tiles)

    return len(black_tiles)


def run(black_tiles):

    new_black_tiles = set(black_tiles)

    all_x = [p.x for p in black_tiles]
    all_y = [p.y for p in black_tiles]
    (min_x, max_x) = (min(all_x), max(all_x))
    (min_y, max_y) = (min(all_y), max(all_y))

    for y in range(min_y - 1, max_y + 2):

        (row_min_x, row_max_x) = (min_x - 1, max_x + 2)
        if parity(y) != parity(row_min_x):
            row_min_x -= 1
        if parity(y) != parity(row_max_x):
            row_max_x += 1

        for x in range(row_min_x, row_max_x, 2):

            p = Tile(x, y)
            neighbours = [p.e(), p.se(), p.sw(), p.w(), p.nw(), p.ne()]
            black_neighbours = [(n in black_tiles) for n in neighbours].count(True)

            if (p in black_tiles) and ((black_neighbours == 0) or (black_neighbours > 2)):
                new_black_tiles.remove(p)

            elif (p not in black_tiles) and (black_neighbours == 2):
                new_black_tiles.add(p)

    return new_black_tiles


def parity(n):
    return n % 2
