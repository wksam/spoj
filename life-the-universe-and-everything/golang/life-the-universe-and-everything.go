package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	var stop bool
	for input.Scan() {
		if input.Text() == "42" {
			stop = true
		}
		if !stop {
			fmt.Println(input.Text())
		}
	}
}
