
class Nodos:

    data = tuple()

    def __init__(self, filename):
        self.data, self.cantidad = self.cargar_nodos(filename)

    def cargar_nodos(self, filename):
        file = open(filename, 'r')
        for line in file:
            cantidad_nodos = int(line)
        lista = tuple()
        for n in range(1, cantidad_nodos + 1):
            lista += (str(n),)
        file.close()
        return lista, cantidad_nodos
