import heapq

def prim(grafo, inicio):
    arvore = []
    visitados = set()
    fila_prioridade = [(0, inicio, None)]
    
    while fila_prioridade:
        custo, atual, pai = heapq.heappop(fila_prioridade)
        
        if atual in visitados:
            continue
        
        visitados.add(atual)
        if pai is not None:
            arvore.append((pai, atual, custo))
        
        for vizinho, custo_aresta in grafo[atual].items():
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (custo_aresta, vizinho, atual))
    
    return arvore

grafo = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 3, 'D': 2},
    'C': {'A': 1, 'B': 3, 'D': 5},
    'D': {'B': 2, 'C': 5}
}

inicio = 'A'
arvore_minima = prim(grafo, inicio)
print("Árvore Geradora Mínima:")
for u, v, custo in arvore_minima:
    print(f"{u} - {v}: {custo}")
