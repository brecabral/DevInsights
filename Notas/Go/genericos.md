# Generics 

Generics em Go são utilizadas com `[]`

exemplo:
```go
func soma[T int | float64](a, b T) T{
    return a + b
}
```
o tipo pode estar contido em uma [interface](interface.md) como
```go
type number interface {
    int | float64
}
```
dessa forma seria usado `[T number]`

tambem é possivel o uso de `[T any]` o qual permite qualquer tipo (semelhante a intereface vazia ´ìnterface{}´)

## Diferenças com outras linguagens:
### [Java](../Java/generics.md)
 - utiliza <> para generics
 - Permite coringas como <? super T> (superior) e <? extends T> (subtipo).
 - Em Java os generics são implementados por type erasure (eliminação dos tipos em tempo de execução), enquanto em Go os generics existem em tempo de compilação, gerando código específico para cada tipo.
