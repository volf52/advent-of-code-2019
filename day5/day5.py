from typing import List
from pathlib import Path

MATH_OPS = [lambda x, y: x + y, lambda x, y: x * y]


class Interpreter:
    __slots__ = "_inp", "_out", "_memory", "_ip", "_is_part_two"

    MIN_OPCODE = 1
    MAX_OPCODE = 8

    def __init__(self, memory: List[int], /, input_src: List[int] = None, is_part_two=False):
        self._inp = (x for x in (input_src or []))
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
        # Checking the mode for arg2 (A) isn't really necessary

        arg0 = self._memory[self._ip + 1]

        # Opcode is in range [MIN_OPCODE, MAX_OPCODE]
        if opcode < 3:  # b/w MIN_OPCODE and 2
            arg1, arg2 = self._memory[self._ip + 2: self._ip + 4]

            arg0 = arg0 if mode0 else self._memory[arg0]
            arg1 = arg1 if mode1 else self._memory[arg1]
            res = MATH_OPS[opcode - 1](arg0, arg1)

            self._memory[arg2] = res

            new_ip = self._ip + 4

        elif opcode < 5:  # 3 or 4. Never in immediate mode
            if opcode == 3:
                to_put = self.get_input()
                self._memory[arg0] = to_put
            else:
                self.send_output(arg0 if mode0 else self._memory[arg0])

            new_ip = self._ip + 2

        elif self._is_part_two:  # Opcode is 5-8. This branch runs only for part_two
            arg1 = self._memory[self._ip + 2]

            arg0 = arg0 if mode0 else self._memory[arg0]
            arg1 = arg1 if mode1 else self._memory[arg1]

            new_ip = self._ip + 3  # Default is to add 3 to the IP (1 for opcode, 2 for args_

            if opcode == 5 and arg0:  # jump if true (arg0 is non-zero)
                new_ip = arg1
            elif opcode == 6 and not arg0:  # jump if false (arg0 is zero)
                new_ip = arg1

            elif opcode == 7:
                new_ip += 1
                arg2 = self._memory[self._ip + 3]

                if arg0 < arg1:
                    self._memory[arg2] = 1
                else:
                    self._memory[arg2] = 0
            elif opcode == 8:  # opcode is 8
                new_ip += 1
                arg2 = self._memory[self._ip + 3]

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
    # MEMORY = [1101, 100, -1, 5, 99, 33] # Part one test

    # Part Two tests
    # MEMORY = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8] # input equal to 8 - pos mode
    # MEMORY = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8] # input less than 8 - pos mode
    # MEMORY = [3, 3, 1108, -1, 8, 3, 4, 3, 99]  # input equal to 8 - immediate mode
    # MEMORY = [3, 3, 1107, -1, 8, 3, 4, 3, 99]  # input less than 8 - immediate mode
    # MEMORY = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]  # is input non-zero - pos mode
    # MEMORY = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]  # is input non-zero - immediate mode

    # MEMORY = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #           1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #           999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    #           ]  # 999 in input below 8, 1000 if equal to 8, 1001 if above 8

    interpreter_one = Interpreter(MEMORY, [1])
    interpreter_one.process_instructions()
    print(interpreter_one.output[- 1])

    interpreter_two = Interpreter(MEMORY, [5], is_part_two=True)
    interpreter_two.process_instructions()
    print(interpreter_two.output[-1])
