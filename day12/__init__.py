import numpy as np

NORTH_MOVE = np.array((0, 1))
SOUTH_MOVE = np.array((0, -1))
EAST_MOVE = np.array((1, 0))
WEST_MOVE = np.array((-1, 0))

DIRECTION_MOVES = {
    "N": NORTH_MOVE,
    "S": SOUTH_MOVE,
    "E": EAST_MOVE,
    "W": WEST_MOVE,
}

BEARING_MOVES = {
    0: NORTH_MOVE,
    90: EAST_MOVE,
    180: SOUTH_MOVE,
    270: WEST_MOVE,
}

LEFT_ROTATE = np.array([[0, -1], [1, 0]])
RIGHT_ROTATE = np.array([[0, 1], [-1, 0]])


def part_1(actions):

    actions = convert(actions)

    pos = np.array((0, 0))
    bearing = 90

    for (action, value) in actions:

        if action in ("N", "S", "E", "W"):
            pos += DIRECTION_MOVES[action] * value

        elif action == "L":
            bearing = (bearing - value) % 360

        elif action == "R":
            bearing = (bearing + value) % 360

        elif action == "F":
            pos += BEARING_MOVES[bearing] * value

    return sum(abs(pos))


def part_2(actions):

    actions = convert(actions)

    ship_pos = np.array((0, 0))
    waypoint_pos = np.array((10, 1))

    for (action, value) in actions:

        if action in ("N", "S", "E", "W"):
            waypoint_pos += DIRECTION_MOVES[action] * value

        elif action == "L":
            for i in range(value // 90):
                waypoint_pos = LEFT_ROTATE.dot(waypoint_pos)

        elif action == "R":
            for i in range(value // 90):
                waypoint_pos = RIGHT_ROTATE.dot(waypoint_pos)

        elif action == "F":
            ship_pos += waypoint_pos * value

    return sum(abs(ship_pos))


def convert(actions):

    if isinstance(actions, str):
        actions = actions.strip().split("\n")

    if isinstance(actions[0], str):
        actions = [(a[0], int(a[1:])) for a in actions]

    return actions
