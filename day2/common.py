from typing import List

OPS = [lambda x, y: x + y, lambda x, y: x * y]


def process(instructions: List[int]):
    for IP in range(0, len(instructions), 4):
        opcode, *rest = instructions[IP: IP + 4]
        if opcode == 99:
            break

        op1, op2, op3 = rest
        instructions[op3] = OPS[opcode - 1](
            instructions[op1], instructions[op2]
        )

    return instructions[0]
