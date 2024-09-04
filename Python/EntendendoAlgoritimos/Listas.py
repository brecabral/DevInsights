def somatorio(lista: list[int]) -> int:
    if (len(lista) <= 1):
        return lista[0]
    return lista.pop() + somatorio(lista)

def myLen(lista: list[int]) -> int:
    if not lista:
        return 0
    lista.pop()
    return myLen(lista) + 1

def myMax(lista: list[int]) -> int:
    num = lista[0]
    for i, valor in enumerate(lista):
        if valor > num:
            num = lista[i]
    return num

lista = [2, 4, 6, 1, 9]
print(myMax(lista))