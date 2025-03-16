def floyd_warshall(grafo):
    distancias = {v: {u: float('inf') for u in grafo} for v in grafo}
    
    for v in grafo:
        distancias[v][v] = 0
        for u, peso in grafo[v].items():
            distancias[v][u] = peso
    
    for k in grafo:
        for i in grafo:
            for j in grafo:
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    
    return distancias

grafo = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2}
}

distancias_minimas = floyd_warshall(grafo)
print("Menor caminho entre todos os pares:")
for origem, destinos in distancias_minimas.items():
    for destino, distancia in destinos.items():
        print(f"{origem} -> {destino}: {distancia}")
