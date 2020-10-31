package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type coord struct {
	x int
	y int
}
type nodeList map[coord]int

const uintSize = 32 << (^uint(0) >> 32 & 1) // 32 or 64

func main() {
	wire1Path, wire2Path := getPaths("input")
	if len(wire1Path) == 0 || len(wire2Path) == 0 {
		log.Fatal("the path of one or more wires is not present in the input")
	}

	wire1Coords := pathToSteps(wire1Path)
	wire2Coords := pathToSteps(wire2Path)
	intersection := wire1Coords.intersect(wire2Coords)

	minMan := 1<<(uintSize-1) - 1 // 2^32 - 1 or 2^64-1
	minSteps := 1<<(uintSize-1) - 1

	for c, steps := range *intersection {
		if steps < minSteps {
			minSteps = steps
		}

		manhattan := c.Manhattan()
		if manhattan < minMan {
			minMan = manhattan
		}
	}

	fmt.Printf("Part One -> %d\n", minMan)
	fmt.Printf("Part Two -> %d\n", minSteps)
}

func (c *coord) Manhattan() int {
	x := c.x
	y := c.y

	if x < 0 {
		x *= -1
	}

	if y < 0 {
		y *= -1
	}

	return x + y
}

func (list *nodeList) intersect(listTwo *nodeList) *nodeList {
	commonList := nodeList{}

	for c, steps := range *list {
		otherSteps, found := (*listTwo)[c]
		if found {
			commonList[c] = steps + otherSteps
		}
	}

	return &commonList
}

func (list *nodeList) set(c *coord, steps int) {
	_, found := (*list)[*c]

	if !found {
		(*list)[*c] = steps
	}
}

func pathToSteps(path []string) *nodeList {
	stepList := &nodeList{}
	xy := &coord{}
	steps := 0

	for _, move := range path {
		direction := move[0]
		displacement, err := strconv.Atoi(move[1:])

		if err != nil {
			log.Fatal(err)
		}

		switch direction {
		case 'R':
			for displacement > 0 {
				xy.x++
				steps++

				stepList.set(xy, steps)

				displacement--
			}

		case 'L':
			for displacement > 0 {
				xy.x--
				steps++

				stepList.set(xy, steps)
				displacement--
			}

		case 'U':
			for displacement > 0 {
				xy.y++
				steps++

				stepList.set(xy, steps)
				displacement--
			}

		case 'D':
			for displacement > 0 {
				xy.y--
				steps++

				stepList.set(xy, steps)
				displacement--
			}
		}
	}

	return stepList
}

func getPaths(fname string) (wire1Path []string, wire2Path []string) {
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

	if scanner.Scan() {
		wire1Path = strings.Split(scanner.Text(), ",")
	}

	if scanner.Scan() {
		wire2Path = strings.Split(scanner.Text(), ",")
	}

	err = scanner.Err()
	if err != nil {
		log.Fatal(err)
	}

	return
}
