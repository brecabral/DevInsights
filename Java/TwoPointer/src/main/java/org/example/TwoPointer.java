package org.example;

public class TwoPointer {
    public String reverseWords(String s) {
        StringBuilder response = new StringBuilder("");
        int leftPointer = 0, rightPointer = 0;
        while (rightPointer < s.length()) {
            if (s.charAt(rightPointer) != ' ') {
                rightPointer++;
            }else {
                for (int i = rightPointer-1; i >= leftPointer; i--) {
                    response.append(s.charAt(i));
                }
                response.append(' ');
                rightPointer++;
                leftPointer = rightPointer;
            }
        }

        for (int i = rightPointer-1; i >= leftPointer; i--) {
            response.append(s.charAt(i));
        }

        return response.toString();
    }
}
