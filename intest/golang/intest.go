package main

import "fmt"

func main() {
	count := 0
	var n, k int
	fmt.Scanf("%d %d", &n, &k)
	for i := 0; i < n; i++ {
		var t int
		fmt.Scanf("%d", &t)
		if t%k == 0 {
			count++
		}
	}
	fmt.Println(count)
}
