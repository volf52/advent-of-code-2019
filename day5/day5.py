from typing import List
from pathlib import Path

MATH_OPS = [lambda x, y: x + y, lambda x, y: x * y]


class Interpreter:
    __slots__ = "_inp", "_out", "_memory", "_ip", "_is_part_two"

    MIN_OPCODE = 1
    MAX_OPCODE = 8

    def __init__(self, memory: List[int], /, input_src: List[int] = None, is_part_two=False):
        self._inp = (x for x in (input_src or [1]))
        self._out = []
        self._memory = memory.copy()
        self._ip = 0
        self._is_part_two = is_part_two

    def get_input(self) -> int:
        next_one = next(self._inp)
        return next_one

    def send_output(self, num: int):
        self._out.append(num)

    def fetch_next_instruction(self):
        return str(self._memory[self._ip])

    def process_instruction(self, instruction: str) -> int:
        opcode = int(instruction[-2:])

        if opcode > self.MAX_OPCODE or opcode < self.MIN_OPCODE:
            raise ValueError(f"Invalid Opcode: {opcode}\tIP: {self._ip}")

        mode0 = int(instruction[2])
        mode1 = int(instruction[1])
        mode2 = int(instruction[0])

        if mode2:
            raise ValueError(f"No opcodes should have arg2 in immediate mode. {self._ip}")

        arg0, arg1, arg2 = self._memory[self._ip + 1: self._ip + 4]


        # Opcode is in range [MIN_OPCODE, MAX_OPCODE]
        if opcode < 3:  # b/w MIN_OPCODE and 2
            arg0 = arg0 if mode0 else self._memory[arg0]
            arg1 = arg1 if mode1 else self._memory[arg1]
            res = MATH_OPS[opcode - 1](arg0, arg1)
            if mode2:  # should not be true for these opcodes
                print("Something looks wrong here")
            else:
                self._memory[arg2] = res

            new_ip = self._ip + 4

        elif opcode < 5:  # 3 or 4. Never in immediate mode
            if opcode == 3:
                to_put = self.get_input()
                self._memory[arg0] = to_put
            else:
                self.send_output(self._memory[arg0])

            new_ip = self._ip + 2

        elif self._is_part_two:  # Opcode is 5-8. This branch runs only for part_two
            arg0 = arg0 if mode0 else self._memory[arg0]
            arg1 = arg1 if mode1 else self._memory[arg1]

            new_ip = self._ip + 3  # Default is to add 3 to the IP (1 for opcode, 2 for args_

            if opcode == 5 and arg0:  # jump if true (arg0 is non-zero)
                new_ip = arg1
            elif opcode == 6 and not arg0:  # jump if false (arg0 is zero)
                new_ip = arg1

            elif opcode == 7:
                new_ip += 1
                if arg0 < arg1:
                    self._memory[arg2] = 1
                else:
                    self._memory[arg2] = 0
            else:  # opcode is 8
                new_ip += 1
                if arg0 == arg1:
                    self._memory[arg2] = 1
                else:
                    self._memory[arg2] = 0

        return new_ip

    def process_instructions(self):
        while self._ip < len(self._memory):
            instruction = self.fetch_next_instruction()

            if instruction == "99":
                break

            self._ip = self.process_instruction(instruction.zfill(5))

    @property
    def output(self):
        return self._out

    @property
    def memory(self):
        return self._memory


# Main Program
if __name__ == "__main__":
    MEMORY = [int(x) for x in Path("input").read_text().split(",")]
    # MEMORY = [1101, 100, -1, 5, 99, 33]

    interpreter_one = Interpreter(MEMORY, [1])

    interpreter_one.process_instructions()

    print(interpreter_one.output[- 1])
    # interpreter_two = Interpreter(MEMORY, [1], is_part_two=True)
    # interpreter_two.process_instructions()
    # print(interpreter_two.output[-1])
