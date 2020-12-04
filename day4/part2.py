from day4 import parser, part1
import re


def is_valid_byr(value):
    return is_valid_year(value, 1920, 2002)


def is_valid_iyr(value):
    return is_valid_year(value, 2010, 2020)


def is_valid_eyr(value):
    return is_valid_year(value, 2020, 2030)


def is_valid_year(value, min_year, max_year):
    m = re.fullmatch("([0-9]{4})", value)
    if not m:
        return False
    year = int(m.group(1))
    return min_year <= year <= max_year


def is_valid_hgt(value):
    m = re.fullmatch("([0-9]+)(cm|in)", value)
    if not m:
        return False
    (number, unit) = int(m.group(1)), m.group(2)
    return (unit == "cm" and 150 <= number <= 193) or (unit == "in" and 59 <= number <= 76)


def is_valid_hcl(value):
    return re.fullmatch("#[0-9a-f]{6}", value) is not None


def is_valid_ecl(value):
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def is_valid_pid(value):
    return re.fullmatch("[0-9]{9}", value) is not None


VALIDATORS = {
    "byr": is_valid_byr,
    "iyr": is_valid_iyr,
    "eyr": is_valid_eyr,
    "hgt": is_valid_hgt,
    "hcl": is_valid_hcl,
    "ecl": is_valid_ecl,
    "pid": is_valid_pid,
    "cid": lambda *_: True,
}


def is_valid(passport):
    return part1.has_required_keys(passport) and values_are_valid(passport)


def values_are_valid(passport):
    return all(VALIDATORS[k](v) for (k, v) in passport.items())


def count_valid_passports(text):
    passports = parser.parse_input(text)
    return sum(1 for passport in passports if is_valid(passport))
