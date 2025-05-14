package org.example;

public class Main {
    public static void main(String[] args) {
        String frase = "Hello, World!";
        System.out.println(frase);

        String fraseInvertida = "";
        for (int i = frase.length()-1; i >= 0; i--) {
            fraseInvertida += frase.charAt(i);
        }
        System.out.println(fraseInvertida);

        TwoPointer twoPointer = new TwoPointer();
        String palavrasInvertidas1 = twoPointer.reverseWords(frase);
        System.out.println(palavrasInvertidas1);

        Nativo nativo = new Nativo();
        String palavrasInvertidas2 = nativo.reverseWords(frase);
        System.out.println(palavrasInvertidas2);
    }
}
