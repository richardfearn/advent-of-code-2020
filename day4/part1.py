from day4 import parser

REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_valid(passport):
    return has_required_keys(passport)


def has_required_keys(passport):
    return REQUIRED_KEYS.intersection(passport.keys()) == REQUIRED_KEYS


def count_valid_passports(text):
    passports = parser.parse_input(text)
    return sum(1 for passport in passports if is_valid(passport))
