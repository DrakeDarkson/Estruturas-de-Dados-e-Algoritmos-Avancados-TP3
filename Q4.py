import heapq

def dijkstra(grafo, origem, destino):
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    caminho = {}
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if custo_atual > distancias[no_atual]:
            continue
        
        for vizinho, custo in grafo[no_atual].items():
            novo_custo = custo_atual + custo
            
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
    
    percurso = []
    atual = destino
    while atual in caminho:
        percurso.insert(0, atual)
        atual = caminho[atual]
    
    if percurso:
        percurso.insert(0, origem)
    
    return percurso, distancias[destino]

grafo = {
    'São Paulo': {'Campinas': 50, 'Rio de Janeiro': 120},
    'Campinas': {'São Paulo': 50, 'Belo Horizonte': 200},
    'Rio de Janeiro': {'São Paulo': 120, 'Vitória': 250},
    'Belo Horizonte': {'Campinas': 200, 'Brasília': 300},
    'Vitória': {'Rio de Janeiro': 250, 'Salvador': 500},
    'Brasília': {'Belo Horizonte': 300, 'Salvador': 600},
    'Salvador': {'Vitória': 500, 'Brasília': 600}
}

origem = 'São Paulo'
destino = 'Salvador'
menor_caminho, custo_total = dijkstra(grafo, origem, destino)
print("Menor rota entre as cidades:", menor_caminho)
print("Custo total da viagem:", custo_total, "reais")
