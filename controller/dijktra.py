
class Dijktra:

    def caminos_minimos(self, grafo, nodo_inicial):
        no_visitados = {nodo: None for nodo in grafo.nodos.data}
        visitado = {}
        actual = nodo_inicial
        predecesor = {str(nodo_inicial): nodo_inicial}
        distancia_actual = 0
        no_visitados[actual] = distancia_actual
        while True:
            actual = str(actual)
            for vecino, distancia in grafo.aristas.data[str(actual)].items():
                if vecino not in no_visitados:
                    continue
                distancia_nueva = distancia_actual + distancia
                if (no_visitados[vecino] is None or no_visitados[vecino] >
                        distancia_nueva):
                    predecesor['{}'.format(vecino)] = actual
                    no_visitados[vecino] = distancia_nueva
            visitado[actual] = {predecesor[actual], distancia_actual}
            del no_visitados[actual]
            if not no_visitados:
                break
            candidatos = [node for node in no_visitados.items() if node[1]]
            candidatos = sorted(candidatos, key=lambda x: x[1])
            actual, distancia_actual = candidatos[0]
        return visitado
