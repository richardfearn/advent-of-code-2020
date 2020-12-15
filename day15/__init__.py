def generate(starting_numbers, length):

    last_number = None
    seen = {}

    for i, n in enumerate(starting_numbers):
        if i < (len(starting_numbers) - 1):
            seen[n] = i
        else:
            last_number = n

    for i in range(len(starting_numbers), length):
        if last_number not in seen:
            next_number = 0
        else:
            next_number = (i - 1) - seen[last_number]
        seen[last_number] = (i - 1)
        last_number = next_number

    return last_number
