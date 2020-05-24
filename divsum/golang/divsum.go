package main

import (
	"fmt"
	"math"
)

func main() {
	var testCase int
	fmt.Scanf("%d", &testCase)
	for t := 0; t < testCase; t++ {
		var num int
		fmt.Scanf("%d", &num)
		divsum := 0

		limit := int(math.Sqrt(float64(num)))
		for i := 2; i <= limit; i++ {
			if num%i == 0 {
				if i == (num / i) {
					divsum += i
				} else {
					divsum += (i + num/i)
				}
			}
		}
		if num > 1 {
			divsum++
		}
		fmt.Println(divsum)
	}
}
