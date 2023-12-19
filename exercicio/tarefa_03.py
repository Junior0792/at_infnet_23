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

