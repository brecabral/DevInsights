package main

func main() {
	arr := []int{1, 2, 4, 8, 16, 32, 64, 128, 256, 1024, 2048}
	target := 20
	indice := ExponetialSearch(arr, target)
	println(indice)
}

func BinarySearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	for high >= low {
		mid := int((high + low) / 2)

		if arr[mid] == target {
			return mid
		} else if arr[mid] > target {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return -1
}

func ExponetialSearch(arr []int, target int) int {
	if len(arr) == 0 {
		return -1
	}

	if arr[0] == target {
		return 0
	}

	currentIndex := 1
	for (currentIndex < len(arr)) && (arr[currentIndex] < target) {
		currentIndex *= 2
	}

	if arr[currentIndex] == target {
		return currentIndex
	}

	subArrIndex := BinarySearch(arr[int(currentIndex/2)+1:], target)
	if subArrIndex == -1 {
		return -1
	}
	return subArrIndex + int(currentIndex/2) + 1

}
