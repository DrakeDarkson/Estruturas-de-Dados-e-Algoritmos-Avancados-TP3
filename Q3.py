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
    'JFK': {'LAX': 3983, 'ORD': 1184},
    'LAX': {'JFK': 3983, 'DFW': 2015, 'SFO': 543},
    'ORD': {'JFK': 1184, 'DFW': 1290},
    'DFW': {'LAX': 2015, 'ORD': 1290, 'MIA': 1772},
    'SFO': {'LAX': 543, 'SEA': 1093},
    'SEA': {'SFO': 1093, 'MIA': 4382},
    'MIA': {'DFW': 1772, 'SEA': 4382}
}

origem = 'JFK'
destino = 'MIA'
menor_caminho, distancia = dijkstra(grafo, origem, destino)
print("Menor trajeto entre os aeroportos:", menor_caminho)
print("Distância total da rota:", distancia, "km")
