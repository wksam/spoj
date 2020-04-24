package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		if input.Text() == "42" {
			break
		}
		fmt.Println(input.Text())
	}
}
