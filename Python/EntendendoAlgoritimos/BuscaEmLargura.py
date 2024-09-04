from collections import deque

def BuscaEmLargura(grafo, inicio, func_alvo):
    fila_de_pesquisa = deque(grafo[inicio])
    verificados = set()
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificados:
            print("---------------------------")
            print("Verificando: " + pessoa)
            print("---------------------------")
            if func_alvo(pessoa):
                print ("Alvo encontrado")
                print("---------------------------")
                print (pessoa)
                print("---------------------------")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificados.add(pessoa)
    print("Alvo não encontrado")
    return False

def ultima_letra_m(nome):
    return nome[-1] == 'm'



grafo = {
        "voce": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": [],
        }


BuscaEmLargura(grafo, "voce", ultima_letra_m)
