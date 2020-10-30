from pathlib import Path

from day2.common import process

if __name__ == "__main__":
    inp = [int(x) for x in Path("input").read_text().split(",")]

    for noun in range(100):
        for verb in range(100):
            instructions = inp.copy()
            instructions[1] = noun
            instructions[2] = verb
            result = process(instructions)
            if result == 19690720:
                print(f"Noun: {noun}\tVerb: {verb}")
                print(f"Result: {noun}{verb}")
                break
