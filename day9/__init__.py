from collections import OrderedDict


def is_valid(previous_numbers, number):
    for other in previous_numbers:
        complement = number - other
        if (other != complement) and (complement in previous_numbers):
            return True
    return False


def part_1(numbers, preamble_length):

    numbers = convert(numbers)

    preamble = numbers[:preamble_length]
    numbers = numbers[preamble_length:]

    previous_numbers = OrderedDict.fromkeys(preamble)

    while len(numbers) > 0:

        number = numbers.pop(0)

        if not is_valid(previous_numbers, number):
            return number

        # noinspection PyArgumentList
        previous_numbers.popitem(last=False)
        previous_numbers[number] = None


def part_2(numbers, invalid_number):
    numbers = convert(numbers)
    nums_in_range = find_range(numbers, invalid_number)
    return min(nums_in_range) + max(nums_in_range)


def find_range(numbers, invalid_number):

    numbers = convert(numbers)

    sums = cumulative_sums(numbers)
    sums.append(0)  # small trick so that if i == 0 below, sums[i - 1] returns 0

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            range_sum = sums[j] - sums[i - 1]
            if range_sum == invalid_number:
                return numbers[i:j + 1]


def cumulative_sums(numbers):
    sums = [numbers[0]]
    for i in range(1, len(numbers)):
        sums.append(sums[i - 1] + numbers[i])
    return sums


def convert(numbers):

    if isinstance(numbers, str):
        numbers = numbers.strip().split("\n")

    if isinstance(numbers[0], str):
        numbers = [int(n) for n in numbers]

    return numbers
