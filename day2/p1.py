from pathlib import Path

from day2.common import process

if __name__ == "__main__":
    inp = [int(x) for x in Path("input").read_text().split(',')]
    inp[1] = 12
    inp[2] = 2
    res = process(inp)
    print(res)
