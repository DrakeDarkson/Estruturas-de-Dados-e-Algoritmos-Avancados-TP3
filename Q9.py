import heapq

def prim(grafo, cidade_inicial):
    custos = {cidade: float('inf') for cidade in grafo}
    custos[cidade_inicial] = 0
    caminho = {}
    fila_prioridade = [(0, cidade_inicial)]
    cidades_conectadas = set()

    while fila_prioridade:
        custo_atual, cidade_atual = heapq.heappop(fila_prioridade)
        
        if cidade_atual in cidades_conectadas:
            continue
        
        cidades_conectadas.add(cidade_atual)
        
        for vizinho, custo in grafo[cidade_atual].items():
            if vizinho not in cidades_conectadas and custo < custos[vizinho]:
                custos[vizinho] = custo
                caminho[vizinho] = cidade_atual
                heapq.heappush(fila_prioridade, (custo, vizinho))
    
    conexoes = []
    for cidade, origem in caminho.items():
        conexoes.append((origem, cidade))
    
    return conexoes, sum(custos[cidade] for cidade in custos if cidade in cidades_conectadas)

grafo = {
    'A': {'B': 10, 'C': 15, 'D': 30},
    'B': {'A': 10, 'C': 20, 'E': 50},
    'C': {'A': 15, 'B': 20, 'E': 10},
    'D': {'A': 30, 'E': 40},
    'E': {'B': 50, 'C': 10, 'D': 40}
}

cidade_inicial = 'A'
conexoes, custo_total = prim(grafo, cidade_inicial)
print("Conjunto de conexões mais econômico:", conexoes)
print("Custo total da expansão:", custo_total)
