from operator import add, mul


def part_1(expression):
    tokens = tokenize(expression)
    tree = build_tree(tokens)
    return evaluate_part_1(tree)


def part_2(expression):
    tokens = tokenize(expression)
    tree = build_tree(tokens)
    return evaluate_part_2(tree)


################################################################################


def tokenize(expression):

    tokens = []
    in_number = False
    number = ""

    for c in expression:

        if c in "()+* ":

            if in_number:
                tokens.append(int(number))
                number = ""
                in_number = False

            if c != " ":
                tokens.append(c)

        else:
            number += c
            in_number = True

    if in_number:
        tokens.append(int(number))

    return tokens


################################################################################


def build_tree(tokens):
    tree = []
    build_tree_helper(tokens, 0, tree)
    return tree


def build_tree_helper(tokens, pos, tree):
    i = pos
    while i < len(tokens):
        token = tokens[i]
        if token == "(":
            tree.append([])
            i = build_tree_helper(tokens, i + 1, tree[-1]) + 1
        elif token == ")":
            return i
        else:
            tree.append(token)
            i += 1
    return i


################################################################################


def evaluate_part_1(tree):

    if isinstance(tree, int):
        return tree

    result = evaluate_part_1(tree[0])

    for i in range(1, len(tree), 2):
        operator = tree[i]
        val = evaluate_part_1(tree[i + 1])
        if operator == "+":
            result += val
        else:
            result *= val

    return result


################################################################################


def evaluate_part_2(tree):

    if isinstance(tree, int):
        return tree

    tree = evaluate_operators(tree, "+", add)
    tree = evaluate_operators(tree, "*", mul)

    return tree[0]


def evaluate_operators(tree, operator, function):

    while operator in tree:
        i = tree.index(operator)
        result = function(evaluate_part_2(tree[i - 1]), evaluate_part_2(tree[i + 1]))
        tree = tree[:i - 1] + [result] + tree[i + 2:]

    return tree
