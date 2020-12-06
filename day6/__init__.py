import utils


def count_questions_part_1(group_lines):

    all_questions = set()

    for line in group_lines:
        all_questions.update(set(line))

    return len(all_questions)


def part_1(lines):
    groups = utils.group_lines(lines)
    return sum(count_questions_part_1(g) for g in groups)


def count_questions_part_2(group_lines):

    all_questions = set(chr(x) for x in range(97, 123))

    for line in group_lines:
        all_questions = all_questions.intersection(set(line))

    return len(all_questions)


def part_2(lines):
    groups = utils.group_lines(lines)
    return sum(count_questions_part_2(g) for g in groups)
