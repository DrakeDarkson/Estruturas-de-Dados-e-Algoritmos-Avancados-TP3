import heapq

def dijkstra(grafo, origem, destino):
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    caminho = {}
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        dist_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if dist_atual > distancias[no_atual]:
            continue
        
        for vizinho, peso in grafo[no_atual].items():
            nova_dist = dist_atual + peso
            
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (nova_dist, vizinho))
    
    percurso = []
    atual = destino
    while atual in caminho:
        percurso.insert(0, atual)
        atual = caminho[atual]
    
    if percurso:
        percurso.insert(0, origem)
    
    return percurso, distancias[destino]

grafo = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 7, 'E': 8},
    'C': {'A': 10, 'E': 5},
    'D': {'B': 7, 'E': 2, 'F': 3},
    'E': {'B': 8, 'C': 5, 'D': 2, 'F': 6},
    'F': {'D': 3, 'E': 6}
}

origem = 'A'
destino = 'F'
menor_caminho, tempo = dijkstra(grafo, origem, destino)
print("Menor percurso entre os bairros:", menor_caminho)
print("Tempo estimado de deslocamento:", tempo, "minutos")
