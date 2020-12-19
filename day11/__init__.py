(FLOOR, FLOOR_SYMBOL) = (0, ".")
(EMPTY, EMPTY_SYMBOL) = (1, "L")
(OCCUPIED, OCCUPIED_SYMBOL) = (2, "#")

SYMBOL_TO_CODE = {
    FLOOR_SYMBOL: FLOOR,
    EMPTY_SYMBOL: EMPTY,
    OCCUPIED_SYMBOL: OCCUPIED,
}

CODE_TO_SYMBOL = {
    FLOOR: FLOOR_SYMBOL,
    EMPTY: EMPTY_SYMBOL,
    OCCUPIED: OCCUPIED_SYMBOL,
}


################################################################################


def part_1_step_text(layout):
    return to_text(part_1_step(from_text(layout)))


def part_2_step_text(layout):
    return to_text(part_2_step(from_text(layout)))


def part_2_text_count_visible(layout, x, y):
    layout = from_text(layout)
    width = len(layout[0])
    height = len(layout)
    return count_visible(layout, x, y, width, height)


def text_count_occupied_seats(layout):
    return layout.count("#")


################################################################################


def part_1(layout):
    return find_occupied_seats_at_end(layout, part_1_step)


def part_1_step(layout):
    return do_step(layout, part_1_new_state)


def part_1_new_state(layout, x, y, width, height):

    old_state = layout[y][x]
    adjacent_occupied_seats = count_adjacent_occupied(layout, x, y, width, height)

    if (old_state == EMPTY) and (adjacent_occupied_seats == 0):
        return OCCUPIED
    elif (old_state == OCCUPIED) and (adjacent_occupied_seats >= 4):
        return EMPTY
    else:
        return old_state


def count_adjacent_occupied(layout, x, y, width, height):
    occupied = 0
    for oy in range(y - 1, y + 2):
        for ox in range(x - 1, x + 2):
            if not ((oy == y) and (ox == x)):
                if (0 <= ox < width) and (0 <= oy < height) and (layout[oy][ox] == OCCUPIED):
                    occupied += 1
    return occupied


################################################################################


def part_2(layout):
    return find_occupied_seats_at_end(layout, part_2_step)


def part_2_step(layout):
    return do_step(layout, part_2_new_state)


def part_2_new_state(layout, x, y, width, height):

    old_state = layout[y][x]
    visible_seats = count_visible(layout, x, y, width, height)

    if (old_state == EMPTY) and (visible_seats[OCCUPIED] == 0):
        return OCCUPIED
    elif (old_state == OCCUPIED) and (visible_seats[OCCUPIED] >= 5):
        return EMPTY
    else:
        return old_state


def count_visible(layout, x, y, width, height):

    counts = {
        EMPTY: 0,
        OCCUPIED: 0,
    }

    offsets = (
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
    )

    for offset in offsets:

        (nx, ny) = (x, y)
        done = False

        while not done:

            nx += offset[0]
            ny += offset[1]

            if (nx < 0) or (nx == width) or (ny < 0) or (ny == height):
                done = True

            elif layout[ny][nx] in (EMPTY, OCCUPIED):
                counts[layout[ny][nx]] += 1
                done = True

    return counts


################################################################################


def find_occupied_seats_at_end(initial_layout, step_function):
    initial_layout = from_text(initial_layout)
    final_layout = run_until_no_changes(initial_layout, step_function)
    return count_occupied_seats(final_layout)


def run_until_no_changes(layout, step_function):
    while True:
        next_layout = step_function(layout)
        if next_layout == layout:
            return layout
        layout = next_layout


def do_step(layout, new_state_function):

    width = len(layout[0])
    height = len(layout)

    new_layout = []
    for y in range(height):
        new_layout.append([])
        for x in range(width):
            new_state = new_state_function(layout, x, y, width, height)
            new_layout[-1].append(new_state)

    return new_layout


def count_occupied_seats(layout):
    flattened = [pos for row in layout for pos in row]
    return flattened.count(OCCUPIED)


################################################################################


def from_text(layout):

    if isinstance(layout, str):
        layout = layout.strip().split("\n")

    if isinstance(layout[0], str):
        layout = [[SYMBOL_TO_CODE[pos] for pos in row] for row in layout]

    return layout


def to_text(layout):
    return "\n".join("".join(CODE_TO_SYMBOL[pos] for pos in row) for row in layout)


################################################################################
