package org.example;

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // while
        //     R++
        //     while
        //         L++

        char[] arr = {'b', 'c', 'b', 'b', 'b', 'c', 'b', 'a'};

        int left = 0, right = 0, max = 0;
        HashMap<Character, Integer> count = new HashMap<>();
        while (right < arr.length) {
            count.put(arr[right], count.getOrDefault(arr[right], 0) + 1);
            while (count.get(arr[right]) == 3) {
                count.put(arr[left], count.get(arr[left]) - 1);
                left++;
            }
            if (max < right - left + 1) {
                max = right - left + 1;
            }
            right++;
        }
        System.out.println(max);
    }
}
