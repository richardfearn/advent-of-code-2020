import re
from utils import to_lines

MASK_REGEX = r"mask = ([X01]{36})"
MEM_REGEX = r"mem\[(\d+)\] = (\d+)"


def part_1(program):

    if isinstance(program, str):
        program = to_lines(program)

    mask_and = mask_or = None
    memory = {}

    for line in program:

        if m := re.match(MASK_REGEX, line):
            mask = m.group(1)
            mask_and = int(mask.replace("0", "0").replace("1", "0").replace("X", "1"), 2)
            mask_or = int(mask.replace("X", "0"), 2)

        elif m := re.match(MEM_REGEX, line):
            address = int(m.group(1))
            value = int(m.group(2))
            result = (value & mask_and) | mask_or
            memory[address] = result

    return sum(memory.values())


def part_2(program):

    if isinstance(program, str):
        program = to_lines(program)

    mask = None
    memory = {}

    for line in program:

        if m := re.match(MASK_REGEX, line):
            mask = m.group(1)

        elif m := re.match(MEM_REGEX, line):
            address = int(m.group(1))
            value = int(m.group(2))
            result = apply_bitmask(address, mask)
            for a in actual_addresses(result):
                memory[a] = value

    return sum(memory.values())


def apply_bitmask(address, mask):

    address = "{:036b}".format(address)

    result = ""
    for i in range(36):
        if mask[i] == "0":
            result += address[i]
        elif mask[i] == "1":
            result += "1"
        else:
            result += "X"

    return result


def actual_addresses(result):

    addresses = [0]

    for bit in result:

        new_addresses = []

        for a in addresses:

            shifted = (a << 1)

            if bit in ("0", "X"):
                new_addresses.append(shifted)

            if bit in ("1", "X"):
                new_addresses.append(shifted + 1)

        addresses = new_addresses

    return addresses
