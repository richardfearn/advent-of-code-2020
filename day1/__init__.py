def part_1_answer(entries):

    values = set(entries)

    for n in entries:
        if (2020 - n) in values:
            return n * (2020 - n)


def part_2_answer(entries):

    complements = {}

    for a in entries:
        for b in entries:
            complements[2020 - a - b] = (a, b)

    for n in entries:
        if n in complements:
            (a, b) = complements[n]
            return n * a * b
