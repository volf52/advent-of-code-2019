from pathlib import Path
from typing import List

OPS = [lambda x, y: x + y, lambda x, y: x * y]


def process(instructions: List[int]):
    for idx in range(0, len(instructions), 4):
        opcode, *rest = instructions[idx: idx + 4]
        if opcode == 99:
            break

        op1, op2, op3 = rest
        instructions[op3] = OPS[opcode - 1](instructions[op1], instructions[op2])


if __name__ == "__main__":
    inp = [int(x) for x in Path("input").read_text().split(',')]
    inp[1] = 12
    inp[2] = 2
    process(inp)
    print(inp[0])
