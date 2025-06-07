package org.example;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int target = 5;
        System.out.println(binarySearch(arr, target));
    }
    public static int binarySearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        while (high >= low) {
            int middle = low + ((high - low) / 2);
            if (arr[middle] == target) {
                return middle;
            }
            if (arr[middle] > target) {
                high = middle - 1;
            }else {
                low = middle + 1;
            }
        }
        return -1;
    }
}
