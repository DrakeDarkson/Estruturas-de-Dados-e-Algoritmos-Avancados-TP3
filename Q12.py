import time
import random
import heapq

def dijkstra(grafo, origem):
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    heap = [(0, origem)]

    while heap:
        distancia_atual, no_atual = heapq.heappop(heap)

        if distancia_atual > distancias[no_atual]:
            continue

        for vizinho, peso in grafo[no_atual].items():
            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(heap, (nova_distancia, vizinho))

    return distancias

def floyd_warshall(grafo):
    vertices = list(grafo.keys())
    n = len(vertices)
    distancia = {v: {u: float('inf') for u in vertices} for v in vertices}

    for v in vertices:
        distancia[v][v] = 0

    for v in grafo:
        for u, peso in grafo[v].items():
            distancia[v][u] = peso

    for k in vertices:
        for i in vertices:
            for j in vertices:
                distancia[i][j] = min(distancia[i][j], distancia[i][k] + distancia[k][j])

    return distancia

def gerar_grafo(n, m, peso_max=100):
    grafo = {str(i): {} for i in range(n)}
    arestas = set()

    while len(arestas) < m:
        u, v = random.sample(range(n), 2)
        peso = random.randint(1, peso_max)
        if (u, v) not in arestas and (v, u) not in arestas:
            grafo[str(u)][str(v)] = peso
            grafo[str(v)][str(u)] = peso
            arestas.add((u, v))

    return grafo

tamanhos = [10, 50, 100, 200, 500]
arestas_porcentagem = 0.2

for tamanho in tamanhos:
    m = int(arestas_porcentagem * tamanho * (tamanho - 1) / 2)
    grafo_teste = gerar_grafo(tamanho, m)

    inicio_dijkstra = time.perf_counter()
    dijkstra(grafo_teste, '0')
    tempo_dijkstra = time.perf_counter() - inicio_dijkstra

    inicio_floyd = time.perf_counter()
    floyd_warshall(grafo_teste)
    tempo_floyd = time.perf_counter() - inicio_floyd

    print(f"Grafo com {tamanho} vértices e {m} arestas:")
    print(f"Dijkstra: {tempo_dijkstra:.6f} segundos")
    print(f"Floyd-Warshall: {tempo_floyd:.6f} segundos")
    print("-" * 40)
