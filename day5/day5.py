from typing import List
from pathlib import Path

MATH_OPS = [lambda x, y: x + y, lambda x, y: x * y]


def processInstruction(
        memory: List[int], instruction: str, IP: int, inpFn, outFn
) -> int:
    instruction = instruction.zfill(5)
    opcode = int(instruction[-2:])
    mode0 = int(instruction[2])
    mode1 = int(instruction[1])
    mode2 = int(instruction[0])

    arg0 = memory[IP + 1]

    if opcode in (1, 2):
        arg1, arg2 = memory[IP + 2: IP + 4]
        arg0 = arg0 if mode0 else memory[arg0]
        arg1 = arg1 if mode1 else memory[arg1]

        res = MATH_OPS[opcode - 1](arg0, arg1)
        if mode2:
            print("Something looks wrong here")
        else:
            memory[arg2] = res

        IP += 4
    elif opcode in (3, 4):
        if opcode == 3:
            memory[arg0] = inpFn()
        else:
            outFn(memory[arg0])
        IP += 2
    else:
        raise ValueError(f"Invalid opcode : {opcode}.\tIP: {IP}")

    return IP


def inpGen(lst: List[int]):
    gen = (i for i in lst)
    fn = lambda: next(gen)
    return fn


def outputGen():
    lst = list()

    return lst, lst.append


# Main Program

IP = 0
inpFn = inpGen(
    [
        1,
    ]
)
OUTPUT, outFn = outputGen()
MEMORY = [int(x) for x in Path("input").read_text().split(",")]
# MEMORY = [1101, 100, -1, 5, 99, 33]

while IP < len(MEMORY):
    instruction = str(MEMORY[IP])
    if instruction == "99":
        break

    IP = processInstruction(MEMORY, instruction, IP, inpFn, outFn)

print(OUTPUT)
print(OUTPUT[-1])
print("Done")
