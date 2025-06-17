package main

import (
	"bufio"
	"os"
)

func main() {
	// Criação de arquivo
	f, err := os.Create("teste.txt")
	if err != nil {
		panic(err)
	}
	// Escrita em arquivo
	tamanho, err := f.Write([]byte("Ola Mundo")) // f.WriteString("Ola Mundo")
	if err != nil {
		panic(err)
	}
	println(tamanho)
	f.Close()

	// Abrindo arquivo
	arquivo1, err := os.Open("teste.txt")
	if err != nil {
		panic(err)
	}
	// Leitura com buffer manual
	buffer := make([]byte, 3)
	n, err := arquivo1.Read(buffer)
	if err != nil {
		panic(err)
	}
	println(string(buffer[:n]))
	arquivo1.Close()

	// Abrindo arquivo
	arquivo2, err := os.Open("teste.txt")
	if err != nil {
		panic(err)
	}
	// Leitura com bufio
	reader := bufio.NewReader(arquivo2)
	leitura_linha, _, err := reader.ReadLine()
	if err != nil {
		panic(err)
	}
	println(string(leitura_linha))
	arquivo2.Close()

	// Lendo arquivo diretamente (não necessario .close())
	arquivo3, err := os.ReadFile("teste.txt")
	if err != nil {
		panic(err)
	}
	println(string(arquivo3))

	// Removendo arquivo
	err = os.Remove("teste.txt")
	if err != nil {
		panic(err)
	}
}
