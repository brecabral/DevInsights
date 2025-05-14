package org.example;

public class Nativo {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder response = new StringBuilder();

        for (String word : words) {
            response.append(new StringBuilder(word).reverse().toString()).append(" ");
        }

        return response.toString().trim();
    }
}
