import heapq



# Digite o número de vértices: 4
# Digite o nome do vértice 1: A
# Digite o nome do vértice 2: B
# Digite o nome do vértice 3: C
# Digite o nome do vértice 4: D
# Digite o número de arestas: 5
# Digite origem, destino e peso da aresta 1 (separados por espaço): A B 4
# Digite origem, destino e peso da aresta 2 (separados por espaço): A C 2
# Digite origem, destino e peso da aresta 3 (separados por espaço): B C 5
# Digite origem, destino e peso da aresta 4 (separados por espaço): B D 10
# Digite origem, destino e peso da aresta 5 (separados por espaço): C D 3
# Digite o vértice de origem para calcular as distâncias: A




class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso):
        self.vertices[origem][destino] = peso
        # Para um grafo não direcionado, descomente a linha abaixo
        # self.vertices[destino][origem] = peso

    def dijkstra(self, origem):
        # Inicializa as distâncias com infinito para todos os vértices, exceto a origem
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[origem] = 0

        # Inicializa a fila de prioridade com a origem e sua distância zero
        fila = [(0, origem)]

        while fila:
            # Obtém o vértice com menor distância
            distancia_atual, vertice_atual = heapq.heappop(fila)

            # Para cada vizinho do vértice atual
            for vizinho, peso in self.vertices[vertice_atual].items():
                # Calcula a nova distância até o vizinho
                nova_distancia = distancia_atual + peso

                # Se a nova distância for menor que a distância armazenada
                if nova_distancia < distancias[vizinho]:
                    # Atualiza a distância e insere na fila de prioridade
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila, (nova_distancia, vizinho))

        return distancias

# Input dos dados do grafo
grafo = Grafo()

num_vertices = int(input("Digite o número de vértices: "))
for i in range(num_vertices):
    vertice = input(f"Digite o nome do vértice {i + 1}: ")
    grafo.adicionar_vertice(vertice)

num_arestas = int(input("Digite o número de arestas: "))
for i in range(num_arestas):
    origem, destino, peso = input(f"Digite origem, destino e peso da aresta {i + 1} (separados por espaço): ").split()
    peso = int(peso)
    grafo.adicionar_aresta(origem, destino, peso)

origem = input("Digite o vértice de origem para calcular as distâncias: ")
distancias = grafo.dijkstra(origem)
print(f"Distâncias a partir do vértice {origem}: {distancias}")
