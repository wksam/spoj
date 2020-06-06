package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	for t := 0; t < n; t++ {
		var i, j int
		fmt.Scanf("%d %d", &i, &j)
		k := reverse(i) + reverse(j)
		fmt.Println(reverse(k))
	}
}

func reverse(number int) int {
	var remainder, reverse int
	for number != 0 {
		remainder = number % 10
		reverse = reverse*10 + remainder
		number /= 10
	}
	return reverse
}
