from operator import itemgetter
from utils import to_lines


def part_1(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    earliest_departure_time = int(lines[0])
    bus_ids = [int(bus_id) for bus_id in lines[1].split(",") if bus_id != "x"]

    next_departures = [(n, ((earliest_departure_time + n - 1) // n) * n) for n in bus_ids]
    earliest_bus = sorted(next_departures, key=itemgetter(1))[0]
    wait_time = earliest_bus[1] - earliest_departure_time
    return earliest_bus[0] * wait_time


def part_2(bus_ids):

    bus_ids = [int(bus_id) if (bus_id != "x") else None for bus_id in bus_ids.split(",")]

    buses = [(offset, bus_id) for offset, bus_id in enumerate(bus_ids) if bus_id is not None]

    interval = buses[0][1]
    timestamp = 0
    for (offset, bus_id) in buses[1:]:
        multiplier = 1
        while True:
            if (timestamp + multiplier * interval + offset) % bus_id == 0:
                break
            multiplier += 1
        timestamp += multiplier * interval
        interval *= bus_id

    return timestamp
