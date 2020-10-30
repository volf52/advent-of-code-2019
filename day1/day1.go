package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func getInput(fname string) (numbers []int) {
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

	for scanner.Scan() {
		tmp := scanner.Text()
		num, err := strconv.Atoi(tmp)

		if err != nil {
			log.Fatal(err)
		}

		numbers = append(numbers, num)
	}

	err = scanner.Err()
	if err != nil {
		log.Fatal(err)
	}

	return
}

func main() {
	numbers := getInput("input")

	totalOne := 0
	totalTwo := 0
	for _, num := range numbers {
		num = num/3 - 2
		totalOne += num

		for num > 0 {
			totalTwo += num
			num = num/3 - 2
		}
	}

	fmt.Printf("Part One -> %d\n", totalOne)
	fmt.Printf("Part Two -> %d\n", totalTwo)
}
