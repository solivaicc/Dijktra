

def file_output_handler(caminos_minimos, nodo_fuente):
    file = open("data/salida.txt", "w")
    file.write('{}\n'.format(nodo_fuente))
    keys_nodos = caminos_minimos.keys()
    for k in keys_nodos:
        info_nodo = caminos_minimos[k]
        predecesor = info_nodo.pop()
        distancia = info_nodo.pop()
        file.write('{} {} {}\n'.format(k, predecesor, distancia))
    file.close
