from typing import List
from pathlib import Path

MATH_OPS = [lambda x, y: x + y, lambda x, y: x * y]


class Interpreter:
    __slots__ = "_inp", "_out", "_memory", "_ip"

    def __init__(self, memory: List[int], /, input_src: List[int] = None):
        self._inp = (x for x in (input_src or [1]))
        self._out = []
        self._memory = memory
        self._ip = 0

    def get_input(self) -> int:
        return next(self._inp)

    def send_output(self, num: int):
        self._out.append(num)

    def fetch_next_instruction(self):
        return str(self._memory[self._ip])

    def process_instruction(self, instruction: str) -> int:
        opcode = int(instruction[-2:])
        mode0 = int(instruction[2])
        mode1 = int(instruction[1])
        mode2 = int(instruction[0])

        arg0 = self._memory[self._ip + 1]

        if opcode in (1, 2):
            arg1, arg2 = self._memory[self._ip + 2: self._ip + 4]
            arg0 = arg0 if mode0 else self._memory[arg0]
            arg1 = arg1 if mode1 else self._memory[arg1]

            res = MATH_OPS[opcode - 1](arg0, arg1)
            if mode2:
                print("Something looks wrong here")
            else:
                self._memory[arg2] = res

            to_add = 4
        elif opcode in (3, 4):
            if opcode == 3:
                self._memory[arg0] = self.get_input()
            else:
                self.send_output(self._memory[arg0])
            to_add = 2
        else:
            raise ValueError(f"Invalid opcode : {opcode}.\tIP: {self._ip}")

        return to_add

    def process_instructions(self):
        while self._ip < len(self._memory):
            instruction = self.fetch_next_instruction()

            if instruction == "99":
                break

            self._ip += self.process_instruction(instruction.zfill(5))

    @property
    def output(self):
        return self._out


# Main Program
if __name__ == "__main__":
    MEMORY = [int(x) for x in Path("input").read_text().split(",")]
    # MEMORY = [1101, 100, -1, 5, 99, 33]

    interpreter = Interpreter(MEMORY, [1])

    interpreter.process_instructions()

    print(interpreter.output[- 1])
    print("Done")
