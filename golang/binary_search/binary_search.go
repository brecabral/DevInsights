package main

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Get the list and target parameters from the URL
		listParam := r.URL.Query().Get("list")
		targetParam := r.URL.Query().Get("target")

		// Convert listParam to a slice
		listStr := strings.Split(listParam, ",")
		var list []int
		for _, str := range listStr {
			num, err := strconv.Atoi(str)
			if err != nil {
				http.Error(w, "Invalid list parameter", http.StatusBadRequest)
				return
			}
			list = append(list, num)
		}

		// Convert targetParam to an interger
		target, err := strconv.Atoi(targetParam)
		if err != nil {
			http.Error(w, "Invalid target parameter", http.StatusBadRequest)
			return
		}

		// Perform the binary search
		result := BinarySearch(list, target)
		fmt.Fprintf(w, "The position of the target request is: %d", result)
	})
	http.ListenAndServe(":8080", nil)
}

func BinarySearch(list []int, target int) int {
	return binarySearchRecur(list, target, 0, len(list)-1)
}

func binarySearchRecur(list []int, target, low, high int) int {
	if low > high {
		return -1 // Base case: element not found
	}

	mid := int((high + low) / 2)

	if list[mid] == target {
		return mid // Base case: element found
	} else if list[mid] > target {
		return binarySearchRecur(list, target, low, mid-1) // Recur on the left half
	} else {
		return binarySearchRecur(list, target, mid+1, high) // Recur on the righ half
	}
}
