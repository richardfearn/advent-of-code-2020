NOP = "nop"
ACC = "acc"
JMP = "jmp"

LOOP = "loop"
TERMINATED = "terminated"


def parse(instructions):

    if isinstance(instructions, str):
        instructions = instructions.strip().split("\n")

    if isinstance(instructions[0], str):
        instructions = [i.split(" ") for i in instructions]
        instructions = [[i[0], int(i[1])] for i in instructions]

    return instructions


def part_1(instructions):
    instructions = parse(instructions)
    return execute(instructions)[1]


def execute(instructions):

    pc = 0
    acc = 0

    executed = set()

    while True:

        if pc > len(instructions) - 1:
            return TERMINATED, acc

        if pc in executed:
            return LOOP, acc

        op, arg = instructions[pc]

        executed.add(pc)

        if op == NOP:
            pc += 1

        elif op == ACC:
            acc += arg
            pc += 1

        elif op == JMP:
            pc += arg


def part_2(instructions):

    instructions = parse(instructions)

    for i, (op, arg) in enumerate(instructions):

        if op in (NOP, JMP):

            instructions[i][0] = JMP if (op == NOP) else NOP

            result, acc = execute(instructions)
            if result == TERMINATED:
                return acc

            instructions[i][0] = op
