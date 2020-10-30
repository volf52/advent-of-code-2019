from pathlib import Path

inp = (int(x) for x in Path("input").read_text().splitlines())


def proc(x: int) -> int:
    total = 0
    x = x // 3 - 2

    while x > 0:
        total += x
        x = x // 3 - 2

    return total


print(sum(proc(x) for x in inp))
