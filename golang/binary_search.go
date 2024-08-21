package main

import "fmt"

func main(){
  list := []int{1,2,3,5}
  target := 1
  result := BinarySearch(list, target)
  fmt.Println(result)
}

func BinarySearch(list []int, target int) int {
  return binarySearchRecur(list, target, 0, len(list)-1)
}

func binarySearchRecur(list []int, target, low, high int) int {
  if (low > high){
    return -1 // Base case: element not found
  }

  mid := int((high+low) / 2)

  if (list[mid] == target){
    return mid // Base case: element found
  }else if(list[mid] > target){
    return binarySearchRecur(list, target, low, mid-1) // Recur on the left half
  }else{
    return binarySearchRecur(list, target, mid+1, high) // Recur on the righ half
  }
}
