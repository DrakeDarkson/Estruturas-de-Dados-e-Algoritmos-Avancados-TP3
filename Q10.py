import heapq

def prim(grafo, bairro_inicial):
    custos = {bairro: float('inf') for bairro in grafo}
    custos[bairro_inicial] = 0
    caminho = {}
    fila_prioridade = [(0, bairro_inicial)]
    bairros_conectados = set()

    while fila_prioridade:
        custo_atual, bairro_atual = heapq.heappop(fila_prioridade)
        
        if bairro_atual in bairros_conectados:
            continue
        
        bairros_conectados.add(bairro_atual)
        
        for vizinho, custo in grafo[bairro_atual].items():
            if vizinho not in bairros_conectados and custo < custos[vizinho]:
                custos[vizinho] = custo
                caminho[vizinho] = bairro_atual
                heapq.heappush(fila_prioridade, (custo, vizinho))
    
    conexoes = []
    for bairro, origem in caminho.items():
        conexoes.append((origem, bairro))
    
    return conexoes, sum(custos[bairro] for bairro in custos if bairro in bairros_conectados)

grafo = {
    'Bairro1': {'Bairro2': 10, 'Bairro3': 15, 'Bairro4': 30},
    'Bairro2': {'Bairro1': 10, 'Bairro3': 20, 'Bairro5': 50},
    'Bairro3': {'Bairro1': 15, 'Bairro2': 20, 'Bairro5': 10},
    'Bairro4': {'Bairro1': 30, 'Bairro5': 40},
    'Bairro5': {'Bairro2': 50, 'Bairro3': 10, 'Bairro4': 40}
}

bairro_inicial = 'Bairro1'
conexoes, custo_total = prim(grafo, bairro_inicial)
print("Plano de instalação mais econômico:", conexoes)
print("Custo total do sistema de abastecimento:", custo_total)
