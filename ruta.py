import heapq

# REGLAS
def evaluar(distancia, tiempo):
    return distancia + tiempo  # menor valor = mejor ruta


# MAPA (GRAFO)
grafo = {
    "A": {"B": {"distancia": 5, "tiempo": 10},
          "C": {"distancia": 8, "tiempo": 15}},
    
    "B": {"D": {"distancia": 3, "tiempo": 5}},
    
    "C": {"D": {"distancia": 2, "tiempo": 4}},
    
    "D": {}
}


# ALGORITMO
def mejor_ruta(inicio, destino):
    cola = [(0, inicio, [inicio])]
    visitados = set()
    
    while cola:
        costo, nodo, camino = heapq.heappop(cola)
        
        if nodo == destino:
            return camino
        
        if nodo in visitados:
            continue
        
        visitados.add(nodo)
        
        for vecino, datos in grafo[nodo].items():
            nuevo_costo = costo + evaluar(datos["distancia"], datos["tiempo"])
            heapq.heappush(cola, (nuevo_costo, vecino, camino + [vecino]))


# EJECUCIÓN
ruta = mejor_ruta("A", "D")
print("Ruta:", ruta)