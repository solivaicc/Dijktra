from model.aristas import Aristas
from model.nodos import Nodos
from model.grafo import Grafo
from controller.dijktra import Dijktra
from utils.file_handler import file_output_handler


class View:

    def __init__(self, filenodos, filearistas, nodo_fuente):
        nodos = Nodos(filenodos)
        grafo = Grafo(nodos, Aristas(filearistas, nodos.cantidad))
        dijktra = Dijktra()
        caminos_minimos = dijktra.caminos_minimos(grafo, nodo_fuente)
        file_output_handler(caminos_minimos, nodo_fuente)
