
class Aristas:

    data = dict()

    def __init__(self, filename, cantidad):
        self.data = self.cargar_aristas(filename, cantidad)

    def cargar_aristas(self, filename, cantidad):
        file = open(filename, 'r')
        dict_aristas = {}
        for n in range(1, cantidad + 1):
            dict_aristas[str(n)] = {}
        for line in file:
            if not line.strip() == 'EOF':
                arista = line.strip().split()
                dict_aristas[str(arista[0])].update({str(arista[1]):
                                                     int(arista[2])})

        file.close()
        return dict_aristas
