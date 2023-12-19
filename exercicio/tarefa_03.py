import heapq

# Exemplo de usar o progama

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
import heapq

def dijkstra(graph, start):
    # Inicialização das estruturas de dados
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Se a distância atual for maior que a armazenada, ignoramos
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Se encontrarmos um caminho mais curto, atualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Exemplo de utilização:
# Representação do grafo como dicionário de adjacência
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 4},
    'D': {'B': 5, 'C': 4}
}

start_vertex = 'A'
result = dijkstra(graph, start_vertex)
print("Distâncias mínimas a partir do vértice inicial {}: {}".format(start_vertex, result))

