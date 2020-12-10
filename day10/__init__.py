import math
from collections import defaultdict


def part_1_counts(joltages):

    joltages = convert(joltages)

    joltages = sorted(joltages)
    device_joltage = joltages[-1] + 3
    joltages = [0] + joltages + [device_joltage]

    diff_counts = defaultdict(int)
    for i in range(1, len(joltages)):
        diff_counts[joltages[i] - joltages[i - 1]] += 1

    return diff_counts[1], diff_counts[3]


def part_1(joltages):
    diff_counts = part_1_counts(joltages)
    return diff_counts[0] * diff_counts[1]


def part_2(joltages):

    joltages = convert(joltages)

    joltages = sorted(joltages)
    device_joltage = joltages[-1] + 3
    joltages = [0] + joltages + [device_joltage]

    # Partition into groups where the difference between each group is 3.
    # Each group is a sequence of consecutive numbers, e.g. [4, 5, 6, 7].
    # Within each group, the first/last numbers must remain, but if there are more than 2,
    # some or all of the middle number(s) could potentially be removed (as long as a gap
    # of more than 3 is not introduced).

    groups = partition(joltages)

    valid_subsets = {
        1: 1,  # e.g. [19] - must keep it
        2: 1,  # e.g. [15, 16] - must keep both
        3: 2,  # e.g. [10, 11, 12] - can remove 11, or leave as-is
        4: 4,  # e.g. [4, 5, 6, 7] - can remove 5, or 6, or both, or leave as-is
        5: 7,
    }

    return math.prod(valid_subsets[len(g)] for g in groups)


def partition(joltages):
    groups = [[joltages[0]]]
    for n in joltages[1:]:
        if (n - groups[-1][-1]) == 3:
            groups.append([])
        groups[-1].append(n)
    return groups


def convert(joltages):

    if isinstance(joltages, str):
        joltages = joltages.strip().split("\n")

    if isinstance(joltages[0], str):
        joltages = [int(n) for n in joltages]

    return joltages
