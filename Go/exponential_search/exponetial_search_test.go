package main

import (
	"testing"
)

func TestExponetialSearch(t *testing.T) {
	tests := []struct {
		name     string
		arr      []int
		target   int
		expected int
	}{
		{name: "target at beginning", arr: []int{1, 2, 4, 8}, target: 1, expected: 0},
		{name: "target in middle", arr: []int{1, 2, 4, 8, 16, 32}, target: 4, expected: 2},
		{name: "target at end", arr: []int{1, 2, 4, 8, 16}, target: 16, expected: 4},
		{name: "target not found", arr: []int{1, 2, 4, 8, 16}, target: 10, expected: -1},
		{name: "empty array", arr: []int{}, target: 5, expected: -1},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := ExponetialSearch(test.arr, test.target)
			if result != test.expected {
				t.Errorf("For %s: expected %d, got %d", test.name, test.expected, result)
			}
		})
	}
}
