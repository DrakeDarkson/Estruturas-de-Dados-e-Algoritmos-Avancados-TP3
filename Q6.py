import heapq

def dijkstra_com_escalas(grafo, escalas, origem, destino, tempo_maximo_conexao):
    custos = {no: float('inf') for no in grafo}
    custos[origem] = 0
    caminho = {}
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if custo_atual > custos[no_atual]:
            continue
        
        for vizinho, (custo, tempo_conexao) in grafo[no_atual].items():
            if tempo_conexao > tempo_maximo_conexao:
                continue
            
            custo_total = custo_atual + custo + escalas.get((no_atual, vizinho), 0)
            
            if custo_total < custos[vizinho]:
                custos[vizinho] = custo_total
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (custo_total, vizinho))
    
    percurso = []
    atual = destino
    while atual in caminho:
        percurso.insert(0, atual)
        atual = caminho[atual]
    
    if percurso:
        percurso.insert(0, origem)
    
    return percurso, custos[destino]

grafo = {
    'JFK': {'LHR': (500, 2), 'CDG': (450, 3)},
    'LHR': {'DXB': (700, 2), 'SIN': (800, 4)},
    'CDG': {'DXB': (650, 3)},
    'DXB': {'SIN': (400, 1)},
    'SIN': {}
}

escalas = {('CDG', 'DXB'): 50, ('LHR', 'SIN'): 100}
origem = 'JFK'
destino = 'SIN'
tempo_maximo_conexao = 3
melhor_rota, custo_total = dijkstra_com_escalas(grafo, escalas, origem, destino, tempo_maximo_conexao)
print("Melhor rota considerando escalas:", melhor_rota)
print("Custo total da viagem:", custo_total, "USD")