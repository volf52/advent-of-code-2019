package main

import "fmt"

func main() {
	const start = 246540
	const end = 787419

	totalOne := 0
	totalTwo := 0
	var digits []uint8

	for n := start; n <= end; n++ {
		digits = getDigits(n)

		if meetsCriteriaOne(digits) {
			totalOne++
		}

		if meetsCriteriaTwo(digits) {
			totalTwo++
		}

	}

	fmt.Println(totalOne)
	fmt.Println(totalTwo)
}

func meetsCriteriaOne(digits []uint8) bool {
	foundAdjacent := false

	for i := 1; i < len(digits); i++ {
		// digits are in reverse order. So, non-decreasing means
		// every digits at idx i-1 should be >= digit at idx i
		if digits[i-1] < digits[i] {
			return false
		}

		if digits[i] == digits[i-1] {
			foundAdjacent = true
		}
	}

	return foundAdjacent
}

func meetsCriteriaTwo(digits []uint8) bool {
	adjacent := make(map[uint8]uint8)

	for i := 1; i < len(digits); i++ {
		// digits are in reverse order. So, non-decreasing means
		// every digits at idx i-1 should be >= digit at idx i
		if digits[i-1] < digits[i] {
			return false
		}

		if digits[i] == digits[i-1] {
			tmp := digits[i]*10 + digits[i]
			adjacent[tmp]++
		}
	}

	for _, freq := range adjacent {
		if freq == 1 {
			return true
		}
	}

	return false
}

func getDigits(num int) (digits []uint8) {
	for num > 0 {
		digits = append(digits, uint8(num%10))
		num = num / 10
	}

	// No need to correct the digit order, as it doesn't matter
	//length := len(digits)
	//for i := 0; i < ((length + 1) >> 1); i++ {
	//tmp := digits[i]
	//digits[i] = digits[length - i - 1]
	//digits[length - i - 1] = tmp
	//}

	return
}
