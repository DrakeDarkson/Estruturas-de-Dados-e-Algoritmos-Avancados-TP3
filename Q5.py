import heapq

def dijkstra_com_recarga(grafo, estacoes_recarga, origem, destino, autonomia_maxima):
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    caminho = {}
    fila_prioridade = [(0, origem, autonomia_maxima)]
    
    while fila_prioridade:
        tempo_atual, no_atual, autonomia_atual = heapq.heappop(fila_prioridade)
        
        if tempo_atual > distancias[no_atual]:
            continue
        
        for vizinho, tempo in grafo[no_atual].items():
            nova_autonomia = autonomia_atual - tempo
            
            if nova_autonomia < 0 and no_atual not in estacoes_recarga:
                continue
            
            if no_atual in estacoes_recarga:
                nova_autonomia = autonomia_maxima
            
            novo_tempo = tempo_atual + tempo
            
            if novo_tempo < distancias[vizinho]:
                distancias[vizinho] = novo_tempo
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (novo_tempo, vizinho, nova_autonomia))
    
    percurso = []
    atual = destino
    while atual in caminho:
        percurso.insert(0, atual)
        atual = caminho[atual]
    
    if percurso:
        percurso.insert(0, origem)
    
    return percurso, distancias[destino]

grafo = {
    'A': {'B': 10, 'C': 15},
    'B': {'A': 10, 'D': 12, 'E': 15},
    'C': {'A': 15, 'F': 10},
    'D': {'B': 12, 'E': 2},
    'E': {'B': 15, 'D': 2, 'F': 5},
    'F': {'C': 10, 'E': 5}
}

estacoes_recarga = {'B', 'E'}
origem = 'A'
destino = 'F'
autonomia_maxima = 20
melhor_rota, tempo_total = dijkstra_com_recarga(grafo, estacoes_recarga, origem, destino, autonomia_maxima)
print("Melhor rota considerando recarga:", melhor_rota)
print("Tempo total de deslocamento:", tempo_total, "minutos")
