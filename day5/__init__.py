def seat_number(boarding_pass):
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    return row, col


def seat_id(seat):
    return seat[0] * 8 + seat[1]


def part_1(boarding_passes):
    boarding_passes = boarding_passes.split()
    seat_numbers = [seat_number(bp) for bp in boarding_passes]
    seat_ids = [seat_id(seat) for seat in seat_numbers]
    return max(seat_ids)


def part_2(boarding_passes):

    boarding_passes = boarding_passes.split()
    seat_numbers = [seat_number(bp) for bp in boarding_passes]
    seat_ids = set(seat_id(seat) for seat in seat_numbers)

    expected_sum = sum_up_to(max(seat_ids)) - sum_up_to(min(seat_ids) - 1)
    missing_seat_id = expected_sum - sum(seat_ids)
    return missing_seat_id


def sum_up_to(n):
    return n * (n + 1) // 2
