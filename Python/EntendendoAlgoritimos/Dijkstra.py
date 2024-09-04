class Dijkstra:
    def __init__(self, grafo: dict[str, dict], inicio: str) -> None:
        self.processados = []
        self.grafo = grafo
        self.inicio = inicio
        self.custos = self._encontra_custos_iniciais()
        self.pais = self._encontra_pais_iniciais()
        self.no_para_analise = self._encontra_no_mais_barato()

    def _encontra_custos_iniciais(self) -> dict[str, int|float]:
        c = {no: float("inf") for no in self.grafo}
        c[self.inicio] = 0
        for vizinho, custo in self.grafo[self.inicio].items():
            c[vizinho] = custo
        return c

    def _encontra_pais_iniciais(self) -> dict[str, str]:
        return {no: self.inicio for no in self.grafo[self.inicio]}

    def _encontra_no_mais_barato(self) -> None|str:
        menor_custo = float("inf")
        no_mais_barato = None
        for n in self.custos:
            custo_atual = self.custos[n]
            if (custo_atual < menor_custo) and (n not in self.processados):
                menor_custo = custo_atual
                no_mais_barato = n
        return no_mais_barato

    def _processamento(self) -> None:
        while self.no_para_analise is not None:
            custo = self.custos[self.no_para_analise]
            vizinhos = self.grafo[self.no_para_analise]
            for n in vizinhos.keys():
                novo_custo = custo + vizinhos[n]
                if (self.custos[n] > novo_custo):
                    self.custos[n] = novo_custo
                    self.pais[n] = self.no_para_analise
            self.processados.append(self.no_para_analise)
            self.no_para_analise = self._encontra_no_mais_barato()
        return None

    def resultados(self) -> None:
        self._processamento()
        print("--- Custos ---")
        for no, custo in self.custos.items():
            print(f"{no} = {custo}")
        print("--- Pais ---")
        for no, pai in self.pais.items():
            print(f"{no} = {pai}")
        return None

grafo = {
        "inicio": { "a": 6, "b": 2},
        "a": { "fim": 1},
        "b": { "a": 3, "fim": 5},
        "fim": {}
        }

grafo_e1 = {
        "inicio": {"a":5, "b":2},
        "a": {"c":4, "d":2},
        "b": {"a":8, "d":7},
        "c": {"fim":3, "d":6},
        "d": {"fim":1},
        "fim": {}
        }

algoritimo = Dijkstra(grafo_e1, "inicio")
algoritimo.resultados()
