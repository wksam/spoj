package main

import "fmt"

func main() {
	var t int
	fmt.Scanf("%d", &t)
	for i := 0; i < t; i++ {
		var n int
		fmt.Scanf("%d", &n)
		count := 0
		i := 5
		for n/i >= 1 {
			count += n / i
			i *= 5
		}
		fmt.Println(count)
	}
}
