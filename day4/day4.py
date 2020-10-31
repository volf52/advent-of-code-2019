from typing import Dict, List, Tuple


def get_digits(n: int) -> List[int]:
    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    # No need to reverse the digits
    # digits.reverse()
    return digits


def meets_criteria(num: int) -> Tuple[bool, bool]:
    digits = get_digits(num)
    adjacent_seen = False
    adjacent_table: Dict[int, int] = {}

    for i in range(1, len(digits)):
        # should be non-decreasing
        if digits[i - 1] < digits[i]:
            return False, False

        if digits[i] == digits[i - 1]:
            adjacent_seen = True
            k = digits[i] * 10 + digits[i]
            adjacent_table[k] = adjacent_table.get(k, 0) + 1

    return adjacent_seen, any(x == 1 for x in adjacent_table.values())


START = 246540
END = 787419

TOTAL_ONE = 0
TOTAL_TWO = 0
for candidate in range(START, END + 1):
    meets_one, meets_two = meets_criteria(candidate)
    if meets_one:
        TOTAL_ONE += 1
    if meets_two:
        TOTAL_TWO += 1

print(TOTAL_ONE)
print(TOTAL_TWO)
