def parse_input(lines):

    if isinstance(lines, str):
        lines = lines.strip().split("\n")

    passports = [[]]
    for line in lines:
        if line == "":
            passports.append([])
        else:
            passports[-1].append(line)

    passports = [create_passport_from_lines(passport) for passport in passports]

    return passports


def create_passport_from_lines(passport_lines):
    line = " ".join(passport_lines)
    key_value_pairs = line.split(" ")
    passport_lines = dict(split_pair(pair) for pair in key_value_pairs)
    return passport_lines


def split_pair(text):
    bits = text.split(":")
    return bits[0], bits[1]
