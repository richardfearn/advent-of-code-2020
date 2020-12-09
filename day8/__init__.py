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


def execute(instructions, start=0):

    pc = start
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
    subprograms = find_subprograms(instructions)
    will_terminate = find_instructions_that_will_terminate(instructions, subprograms)
    return find_instruction_to_change(instructions, will_terminate)


def find_subprograms(instructions):

    # Makes it easier to find connected components
    graph = undirected_graph(instructions)

    components = []
    search_start_remaining = set(range(len(instructions)))

    while len(search_start_remaining) > 0:

        search_start = search_start_remaining.pop()
        visited = set()
        to_explore = [search_start]

        while len(to_explore) > 0:
            next_node = to_explore.pop(0)
            if next_node not in visited:
                if next_node in search_start_remaining:
                    search_start_remaining.remove(next_node)
                visited.add(next_node)
                to_explore += graph[next_node]

        components.append(visited)

    return components


def undirected_graph(instructions):

    graph = {pc: [] for pc in range(len(instructions))}

    for pc, (op, arg) in enumerate(instructions):

        next_pc = (pc + arg) if (op == JMP) else (pc + 1)

        if next_pc < len(instructions):
            graph[pc].append(next_pc)
            graph[next_pc].append(pc)

    return graph


def find_instructions_that_will_terminate(instructions, subprograms):

    will_terminate = set()

    for s in subprograms:
        start_instruction = list(s)[0]
        if execute(instructions, start_instruction)[0] == TERMINATED:
            will_terminate.update(s)

    return will_terminate


def find_instruction_to_change(instructions, will_terminate):

    pc = 0
    acc = 0

    executed = set()

    instruction_changed = False

    while True:

        if pc > len(instructions) - 1:
            return acc

        if pc in executed:
            raise Exception("infinite loop")

        op, arg = instructions[pc]

        executed.add(pc)

        if (not instruction_changed) and op in (NOP, JMP):

            next_pc_with_change = (pc + arg) if (op == NOP) else (pc + 1)

            if (next_pc_with_change > len(instructions) - 1) or (next_pc_with_change in will_terminate):
                op = JMP if (op == NOP) else NOP
                instruction_changed = True

        if op == NOP:
            pc += 1

        elif op == ACC:
            acc += arg
            pc += 1

        elif op == JMP:
            pc += arg
