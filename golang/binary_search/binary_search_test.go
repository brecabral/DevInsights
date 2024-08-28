package main

import (
	"testing"
)

func TestBinarSearch(t *testing.T) {
	tests := []struct {
		list     []int
		target   int
		expected int
	}{
		{list: []int{10, 20, 53, 34, 11}, target: 20, expected: 1},
	}

	for _, test := range tests {
		result := BinarySearch(test.list, test.target)
		if result != test.expected {
			t.Errorf("For list %v and target %d, expected %d but got %d", test.list, test.target, test.expected, result)
		}
	}
}
