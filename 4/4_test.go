package main

import "testing"

func TestIsWonRow(t *testing.T) {
	marked := []bool{
		false, false, false, false, false,
		false, false, false, false, false,
		true, true, true, true, true,
		false, false, false, false, false,
		false, false, false, false, false,
	}
	won := isWon(marked)
	if !won {
		t.Errorf("expected win")
	}
}

func TestIsWonCol(t *testing.T) {
	marked := []bool{
		false, false, true, false, false,
		false, false, true, false, false,
		false, false, true, false, false,
		false, false, true, false, false,
		false, false, true, false, false,
	}
	won := isWon(marked)
	if !won {
		t.Errorf("expected win")
	}
}

func TestIsWonNoWin(t *testing.T) {
	marked := []bool{
		false, false, true, false, false,
		false, false, true, false, false,
		true, false, true, true, true,
		false, false, false, false, false,
		false, false, true, false, false,
	}
	won := isWon(marked)
	if won {
		t.Errorf("expected lose")
	}
}

func TestMarkCalledNumber(t *testing.T) {
	marked := make([]bool, 25)
	board := make([]int, 25)
	board[13] = 49

	found := markCalledNumber(board, &marked, 49)
	if !found {
		t.Error()
	}
	if !marked[13] {
		t.Error()
	}

	found = markCalledNumber(board, &marked, 99)
	if found {
		t.Error()
	}
}
