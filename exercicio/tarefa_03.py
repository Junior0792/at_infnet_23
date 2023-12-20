import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso):
        self.vertices[origem][destino] = peso
        self.vertices[destino][origem] = peso

    def calcular_menor_caminho(self, vertice_origem):
        # Inicializa as distâncias com infinito para todos os vértices
        distancias = {v: float('inf') for v in self.vertices}
        # Define a distância do vértice origem para ele mesmo como 0
        distancias[vertice_origem] = 0
        
        # Fila de prioridade para armazenar os vértices a serem explorados
        fila_prioridade = [(0, vertice_origem)]

        while fila_prioridade:
            # Obtém o vértice com a menor distância atual da fila
            dist_atual, vertice_atual = heapq.heappop(fila_prioridade)

            # Se a distância atual for maior que a distância registrada, ignora
            if dist_atual > distancias[vertice_atual]:
                continue

            # Itera sobre os vizinhos do vértice atual
            for vizinho, peso in self.vertices[vertice_atual].items():
                # Calcula a distância através do vértice atual até o vizinho
                dist = dist_atual + peso
                # Se a distância calculada for menor que a registrada, atualiza
                if dist < distancias[vizinho]:
                    distancias[vizinho] = dist
                    # Insere o vizinho na fila de prioridade com sua nova distância
                    heapq.heappush(fila_prioridade, (dist, vizinho))

        return distancias

# Exemplo de uso:
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')

grafo.adicionar_aresta('A', 'B', 4)
grafo.adicionar_aresta('A', 'C', 2)
grafo.adicionar_aresta('B', 'C', 5)
grafo.adicionar_aresta('B', 'D', 10)
grafo.adicionar_aresta('C', 'D', 3)

distancias = grafo.calcular_menor_caminho('A')
print("Distâncias a partir de A:", distancias)
