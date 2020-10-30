from pathlib import Path

inp = (int(x) for x in Path("input").read_text().splitlines())

print(sum(x//3 - 2 for x in inp))
