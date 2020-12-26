from utils import to_lines


def part_1(lines):
    public_keys = parse(lines)
    loop_sizes = [determine_loop_size(7, pk) for pk in public_keys]
    return transform(public_keys[0], loop_sizes[1])


def determine_loop_size(subject_number, public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value = transform_once(value, subject_number)
        loop_size += 1
    return loop_size


def transform_once(value, subject_number):
    return (value * subject_number) % 20201227


def transform(subject_number, loop_size):
    value = 1
    for step in range(loop_size):
        value = transform_once(value, subject_number)
    return value


def parse(keys):

    if isinstance(keys[0], str):
        keys = [int(key) for key in keys]

    return keys
