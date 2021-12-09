package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	inputFile, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer inputFile.Close()

	calledNums, boards := parseInput(inputFile)

	part1(calledNums, boards)
	part2(calledNums, boards)
}

func part1(calledNums []int, boards [][]int) {
	marked := make([][]bool, 0)
	for _, board := range boards {
		marked = append(marked, make([]bool, len(board)))
	}

	for _, calledNum := range calledNums {
		for i, board := range boards {
			if markCalledNumber(board, &marked[i], calledNum) {
				if isWon(marked[i]) {
					fmt.Println(calcScore(board, marked[i], calledNum))
					return
				}
			}
		}
	}
}

func part2(calledNums []int, boards [][]int) {
	marked := make([][]bool, 0)
	for _, board := range boards {
		marked = append(marked, make([]bool, len(board)))
	}

	finishedBoards := 0
	for _, calledNum := range calledNums {
		for i, board := range boards {
			if isWon(marked[i]) {
				continue
			}
			if markCalledNumber(board, &marked[i], calledNum) {
				if isWon(marked[i]) {
					finishedBoards += 1
					fmt.Printf("board %d: %d\n", finishedBoards, calcScore(board, marked[i], calledNum))
				}
			}
		}
	}
}

func stringsToInts(strs []string) (ints []int) {
	ints = make([]int, 0)
	for _, str := range strs {
		if num, err := strconv.Atoi(str); err != nil {
			panic(err)
		} else {
			ints = append(ints, num)
		}
	}
	return
}

func parseInput(inputFile *os.File) (calledNums []int, boards [][]int) {
	scanner := bufio.NewScanner(inputFile)

	scanner.Scan()
	calledNums = stringsToInts(strings.Split(scanner.Text(), ","))

	boards = make([][]int, 1)

	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 {
			continue
		}
		currentBoard := &boards[len(boards)-1]
		if len(*currentBoard) == 25 {
			// board is complete, parse the next one
			boards = append(boards, make([]int, 0))
			currentBoard = &boards[len(boards)-1]
		}
		nums := stringsToInts(strings.Fields(line))

		*currentBoard = append(*currentBoard, nums...)
	}

	return
}

func isWon(marked []bool) bool {
	// rows
	for r := 0; r < 5; r++ {
		allMarked := true
		for c := 0; c < 5; c++ {
			if !marked[r*5+c] {
				allMarked = false
			}
		}
		if allMarked {
			return true
		}
	}

	// cols
	for c := 0; c < 5; c++ {
		allMarked := true
		for r := 0; r < 5; r++ {
			if !marked[r*5+c] {
				allMarked = false
			}
		}
		if allMarked {
			return true
		}
	}

	return false
}

func markCalledNumber(board []int, marked *[]bool, calledNum int) bool {
	for i := 0; i < len(board); i++ {
		if board[i] == calledNum {
			(*marked)[i] = true
			return true
		}
	}
	return false
}

func calcScore(board []int, marked []bool, calledNum int) int {
	unmarkedSum := 0
	for i := 0; i < len(board); i++ {
		if !marked[i] {
			unmarkedSum += board[i]
		}
	}

	return unmarkedSum * calledNum
}
