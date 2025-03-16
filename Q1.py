import heapq

def dijkstra(grafo, origem):
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        dist_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if dist_atual > distancias[no_atual]:
            continue
        
        for vizinho, peso in grafo[no_atual].items():
            nova_dist = dist_atual + peso
            
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila_prioridade, (nova_dist, vizinho))
    
    return distancias

grafo = {
    'Centro': {'A': 10, 'B': 20},
    'A': {'Centro': 10, 'C': 15, 'D': 25},
    'B': {'Centro': 20, 'D': 30},
    'C': {'A': 15, 'D': 10, 'E': 20},
    'D': {'A': 25, 'B': 30, 'C': 10, 'E': 5},
    'E': {'C': 20, 'D': 5}
}

origem = 'Centro'
menores_caminhos = dijkstra(grafo, origem)
print("Menor distância do centro de distribuição para cada bairro:")
for bairro, distancia in menores_caminhos.items():
    print(f"{bairro}: {distancia} km")
