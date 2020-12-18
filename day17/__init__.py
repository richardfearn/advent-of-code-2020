from utils import to_lines


ACTIVE = "#"
INACTIVE = "."


def part_1(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    active_cubes = set()

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            coords = (x, y, 0)
            if lines[y][x] == ACTIVE:
                active_cubes.add(coords)

    for cycle in range(1, 7):

        (min_x, max_x) = min_max(active_cubes, 0)
        (min_y, max_y) = min_max(active_cubes, 1)
        (min_z, max_z) = min_max(active_cubes, 2)

        new_active_cubes = set()

        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):

                    pos = (x, y, z)

                    old_state = ACTIVE if (pos in active_cubes) else INACTIVE
                    neighbours = count_neighbours_part_1(active_cubes, x, y, z)
                    new_state = determine_new_state(old_state, neighbours)

                    if new_state == ACTIVE:
                        new_active_cubes.add(pos)

        active_cubes = new_active_cubes

    return len(active_cubes)


def count_neighbours_part_1(active_cubes, x, y, z):
    pos = (x, y, z)
    count = 0
    for oz in range(z - 1, z + 2):
        for oy in range(y - 1, y + 2):
            for ox in range(x - 1, x + 2):
                other = (ox, oy, oz)
                if (other != pos) and (other in active_cubes):
                    count += 1
    return count


def part_2(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    active_cubes = set()

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            coords = (x, y, 0, 0)
            if lines[y][x] == ACTIVE:
                active_cubes.add(coords)

    for cycle in range(1, 7):

        (min_x, max_x) = min_max(active_cubes, 0)
        (min_y, max_y) = min_max(active_cubes, 1)
        (min_z, max_z) = min_max(active_cubes, 2)
        (min_w, max_w) = min_max(active_cubes, 3)

        new_active_cubes = set()

        for w in range(min_w - 1, max_w + 2):
            for z in range(min_z - 1, max_z + 2):
                for y in range(min_y - 1, max_y + 2):
                    for x in range(min_x - 1, max_x + 2):

                        pos = (x, y, z, w)

                        old_state = ACTIVE if (pos in active_cubes) else INACTIVE
                        neighbours = count_neighbours_part_2(active_cubes, x, y, z, w)
                        new_state = determine_new_state(old_state, neighbours)

                        if new_state == ACTIVE:
                            new_active_cubes.add(pos)

        active_cubes = new_active_cubes

    return len(active_cubes)


def count_neighbours_part_2(active_cubes, x, y, z, w):
    pos = (x, y, z, w)
    count = 0
    for ow in range(w - 1, w + 2):
        for oz in range(z - 1, z + 2):
            for oy in range(y - 1, y + 2):
                for ox in range(x - 1, x + 2):
                    other = (ox, oy, oz, ow)
                    if (other != pos) and (other in active_cubes):
                        count += 1
    return count


def min_max(coords, i):
    values = [c[i] for c in coords]
    return min(values), max(values)


def determine_new_state(old_state, neighbours):
    if old_state == ACTIVE:
        return ACTIVE if (2 <= neighbours <= 3) else INACTIVE
    elif old_state == INACTIVE:
        return ACTIVE if (neighbours == 3) else INACTIVE
