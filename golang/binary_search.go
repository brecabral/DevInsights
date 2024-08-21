package main

import "fmt"

func main(){
  list := []int{1,2,3,5}
  target := 1
  result := binarySearch(list, target, 0, len(list)-1)
  fmt.Println(result)
}

func binarySearch(list []int, target, low, high int) int {
  if (low > high){
    return -1 // Base case: element not found
  }

  mid := int((high+low) / 2)

  if (list[mid] == target){
    return mid // Base case: element found
  }else if(list[mid] > target){
    return binarySearch(list, target, low, mid-1) // Recur on the left half
  }else{
    return binarySearch(list, target, mid+1, high) // Recur on the righ half
  }
}
