# Generics em Java

Generics em Java são utilizados com **`<>`**.

### Uso de coringas (`wildcards`):
- **`<? extends T>`** → aceita **subtipos de T** (T e suas subclasses).  
  Útil quando você **lê dados** de uma estrutura, garantindo que os elementos são do tipo T ou derivados dele.  
  Não permite adicionar elementos, exceto `null`.

- **`<? super T>`** → aceita **supertypos de T** (T e suas superclasses).  
  Útil quando você **escreve dados** em uma estrutura, garantindo que pode adicionar objetos do tipo T.  
  A leitura retorna como `Object`, já que o compilador não sabe o tipo específico.

### Exemplo prático:
```java
List<? extends Number> numerosLeitura;
List<? super Integer> numerosEscrita;