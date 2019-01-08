from view.view import View
import sys

if __name__ == "__main__":
    try:
        view = View(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError as e:
        print('Para arrancar app ingrese lo siguiente:\n'
              'python app.py nombre_archivo_nodos.txt '
              'nombre_archivo_aristas.txt nodo_fuente.\n'
              'ej: python app.py data/nodos.txt data/arcos.txt 1')
    except Exception as e:
        print('Ocurrio un error inesperado: {}'.format(e))
