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


def isNotPartOfGroup(idx: int, l: int, digits: List[int]) -> bool:
    d = digits[idx]
    if idx == 1:
        return d != digits[idx] + 1
    if idx == l:
        return d != digits[idx - 2]

    return d != digits[idx - 2] and d != digits[idx + 1]


def meets_criteria(num: int) -> bool:
    digits = get_digits(num)
    adjacent_seen = {}
    for i in range(1, len(digits)):
        # should be non-decreasing
        if digits[i] < digits[i - 1]:
            return False

        if digits[i] == digits[i - 1]:
            k = (digits[i], digits[i])
            adjacent_seen[k] = adjacent_seen.get(k, 0) + 1

    return any(x == 1 for x in adjacent_seen.values())


print(meets_criteria(112233))
print(meets_criteria(123444))
print(meets_criteria(11111122))

total = 0
for num in range(start, end + 1):
    if meets_criteria(num):
        total += 1

print(total)
