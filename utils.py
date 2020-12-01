from pathlib import Path


def read_input_lines(day):
    path = Path(__file__).parent / f"day{day}" / "input.txt"
    with path.open() as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    return lines


def read_input_line(day):
    return read_input_lines(day)[0]
