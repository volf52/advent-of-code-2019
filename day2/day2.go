package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func getInput(fname string) (instructions []int) {
	fp, err := os.Open(fname)

	if err != nil {
		log.Fatal(err)
	}

	defer func() {
		if err = fp.Close(); err != nil {
			log.Fatalf("error closing file: %s", err)
		}
	}()

	scanner := bufio.NewScanner(fp)
	scanner.Split(bufio.ScanLines)
	if !scanner.Scan() {
		log.Fatalf("empty input")
	}

	// Single line
	for _, n := range strings.Split(scanner.Text(), ",") {
		num, err := strconv.Atoi(n)

		if err != nil {
			log.Fatal(err)
		}

		instructions = append(instructions, num)
	}

	err = scanner.Err()
	if err != nil {
		log.Fatal(err)
	}

	return
}

func processInstructions(instructions []int) int {
	IP := 0

	for IP < len(instructions) {
		opcode := instructions[IP]
		if opcode == 99 {
			return instructions[0]
		}

		op1 := instructions[instructions[IP+1]]
		op2 := instructions[instructions[IP+2]]
		var res int

		switch opcode {
		case 1:
			res = op1 + op2
		case 2:
			res = op1 * op2
		default:
			log.Fatalf("invalid opcode: %d", opcode)
		}

		instructions[instructions[IP+3]] = res

		IP += 4
	}

	return instructions[0]
}

func main() {
	instructions := getInput("input")

	toProcess := make([]int, len(instructions))
	copy(toProcess, instructions)
	toProcess[1] = 12
	toProcess[2] = 2

	partOne := processInstructions(toProcess)
	var partTwo int

	expected := 19690720
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			copy(toProcess, instructions)
			toProcess[1] = noun
			toProcess[2] = verb

			tmp := processInstructions(toProcess)

			if tmp == expected {
				partTwo = 100*noun + verb
				break
			}
		}
	}

	fmt.Printf("Part One -> %d\n", partOne)
	fmt.Printf("Part Two -> %d\n", partTwo)
}
