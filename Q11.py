import heapq

def prim(grafo):
    if not grafo:
        return [], 0

    no_inicial = next(iter(grafo))
    heap = [(peso, no_inicial, vizinho) for vizinho, peso in grafo[no_inicial].items()]
    heapq.heapify(heap)
    visitados = {no_inicial}
    mst = []
    custo_total = 0

    while heap and len(visitados) < len(grafo):
        peso, origem, destino = heapq.heappop(heap)

        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, peso))
            custo_total += peso

            for vizinho, custo in grafo[destino].items():
                if vizinho not in visitados:
                    heapq.heappush(heap, (custo, destino, vizinho))

    return mst, custo_total

grafo_torres = {
    'A': {'B': 10, 'C': 20},
    'B': {'A': 10, 'C': 30, 'D': 5},
    'C': {'A': 20, 'B': 30, 'D': 15},
    'D': {'B': 5, 'C': 15}
}

mst, custo = prim(grafo_torres)
print("Árvore Geradora Mínima (MST):", mst)
print("Custo mínimo total:", custo)
