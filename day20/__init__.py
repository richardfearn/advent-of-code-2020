from math import sqrt, prod
from utils import to_lines, group_lines, chunks
import numpy as np

(TOP, RIGHT, BOTTOM, LEFT) = range(4)

SEA_MONSTER = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""


class Tile:

    def __init__(self, lines):

        self.num = int(lines[0][5:-1])

        pixels = lines[1:]
        pixels = [[int(p) for p in row.replace(".", "0").replace("#", "1")] for row in pixels]
        self.pixels = np.array(pixels)

        self.edges = None
        self.cache_edges()

    def cache_edges(self):

        self.edges = {}
        pixels = self.pixels

        for flipped in (False, True):

            if flipped:
                pixels = np.fliplr(pixels)

            self.edges[flipped] = {}

            for orientation in range(4):

                self.edges[flipped][orientation] = {
                    TOP: list(pixels[0]),
                    LEFT: list(pixels[:, 0]),
                    BOTTOM: list(pixels[-1]),
                    RIGHT: list(pixels[:, -1]),
                }

                pixels = np.rot90(pixels)

    def edge(self, flipped, orientation, edge):
        return self.edges[flipped][orientation][edge]

    def pixel_data(self, flipped, orientation):
        pixels = self.pixels
        if flipped:
            pixels = np.fliplr(pixels)
        for i in range(orientation):
            pixels = np.rot90(pixels)
        return pixels

    def __str__(self):
        return "Tile[num=%d, edges=%s]" % (self.num, self.edges)


class PlacedTile:

    def __init__(self, pos, tile, flipped, orientation):
        self.pos = pos
        self.tile = tile
        self.flipped = flipped
        self.orientation = orientation

    def edge(self, edge):
        return self.tile.edge(self.flipped, self.orientation, edge)

    def pixel_data(self):
        return self.tile.pixel_data(self.flipped, self.orientation)

    def __str__(self):
        return "PlacedTile[pos=%d, tile=%d, flipped=%s, orientation=%d]" % (
            self.pos, self.tile.num, self.flipped, self.orientation)

    def __repr__(self):
        return self.__str__()


def parse(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    tiles = group_lines(lines)

    tiles = [Tile(tile_lines) for tile_lines in tiles]
    tiles = {tile.num: tile for tile in tiles}
    return tiles


def part_1(lines):
    image = find_arrangement(lines)
    tile_nums = [[tile.tile.num for tile in row] for row in image]
    return prod((tile_nums[0][0], tile_nums[0][-1], tile_nums[-1][0], tile_nums[-1][-1]))


def find_arrangement(lines):
    tiles = parse(lines)
    grid_size = int(sqrt(len(tiles)))
    initial_state = []
    arrangement = dfs(tiles, grid_size, initial_state)
    return chunks(arrangement, grid_size)


def dfs(tiles, grid_size, state):

    placed_so_far = len(state)
    next_pos = placed_so_far
    (x, y) = (next_pos % grid_size, next_pos // grid_size)

    tiles_in_use = set(tile.tile.num for tile in state)
    candidates = set(tiles.keys()) - tiles_in_use

    for num in candidates:
        tile = tiles[num]

        for flipped in (False, True):
            for orientation in range(4):
                candidate = PlacedTile(next_pos, tile, flipped, orientation)

                ok = True

                if x > 0:
                    # must match tile to the left
                    left = state[next_pos - 1]
                    if left.edge(RIGHT) != candidate.edge(LEFT):
                        ok = False

                if y > 0:
                    # must match the tile above
                    above = state[next_pos - grid_size]
                    if above.edge(BOTTOM) != candidate.edge(TOP):
                        ok = False

                if ok:

                    new_arrangement = state[::] + [candidate]

                    if len(new_arrangement) == (grid_size * grid_size):
                        return new_arrangement

                    arrangement = dfs(tiles, grid_size, new_arrangement)
                    if arrangement:
                        return arrangement

    return None


def part_2(lines):

    (smp, smw, smh) = sea_monster()

    arrangement = find_arrangement(lines)
    pixels = [[t.pixel_data() for t in row] for row in arrangement]  # replace each tile with its pixels
    pixels = [[t[1:-1, 1:-1] for t in row] for row in pixels]  # remove border from each tile
    pixels = [np.concatenate(row, axis=1) for row in pixels]  # merge tiles in each row
    pixels = np.concatenate(pixels)  # merge rows into single grid

    for flipped in (False, True):

        if flipped:
            pixels = np.fliplr(pixels)

        for orientation in range(4):

            for y in range(0, len(pixels) - smh + 1):
                for x in range(0, len(pixels[0]) - smw + 1):

                    sub_image = pixels[y:y + smh, x:x + smw]
                    if all((sub_image[y][x] == 1) for (x, y) in smp):
                        for (sx, sy) in smp:
                            sub_image[sy][sx] = 0

            pixels = np.rot90(pixels)

    return np.count_nonzero(pixels == 1)


def sea_monster():
    pixels = [[int(p) for p in row.replace(" ", "0").replace("#", "1")] for row in SEA_MONSTER.split("\n")[1:-1]]
    (width, height) = (len(pixels[0]), len(pixels))
    pixels = [(x, y) for y in range(height) for x in range(width) if pixels[y][x] == 1]
    return pixels, width, height
