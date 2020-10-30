from typing import List

start = 246540
end = 787419


def get_digits(n: int) -> List[int]:
    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    digits.reverse()
    return digits


def meets_criteria(num: int) -> bool:
    digits = get_digits(num)
    found_adjacent = False
    for i in range(1, len(digits)):
        # should be non-decreasing
        if digits[i] < digits[i - 1]:
            return False

        if digits[i] == digits[i - 1]:
            found_adjacent = True

    return found_adjacent


total = 0
for num in range(start, end + 1):
    if meets_criteria(num):
        total += 1

print(total)
