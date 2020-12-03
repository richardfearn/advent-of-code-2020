from pathlib import Path


def read_input_lines(day):
    with day_path(day).open() as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    return lines


def read_input(day):
    with day_path(day).open() as f:
        text = f.read()
    return text


def day_path(day):
    return Path(__file__).parent / f"day{day}" / "input.txt"
