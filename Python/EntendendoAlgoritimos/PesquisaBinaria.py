class busca:


    def binaria(self, lista, alvo):
        alto = len(lista) - 1
        baixo = 0
        
        if alto < baixo:
            return -1
        
        meio = (alto + baixo) // 2
        if (lista[meio] == alvo):
            return meio
        elif (lista[meio] > alvo):
            newLista = lista[:-(meio+1)]
            return self.binaria(newLista, alvo)
        elif (lista[meio] < alvo):
            newLista = lista[(meio+1):]
            return (self.binaria(newLista, alvo) + meio + 1)



lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a = busca()
print(a.binaria(lista, 5))