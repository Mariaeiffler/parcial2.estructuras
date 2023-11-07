# from prueba_menu import *
from Hotel_prueba import *
import numpy as np

mi_diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Ejemploville"
}

def valTipoEmpleado(tipo,dicc1:dict):
    while valPalabraDic(tipo,dicc1)==False:
        llaves=list(dicc1.keys())
        tipo=input('Error. Ese tipo de empleado no existe. \n Las opciones disponibles son: {} \n Ingrese una de las opciones existentes:'.format (llaves))
    return tipo

mili=np.array([])

list = [[1,2],[2,3],[3]]

if __name__ == "__main__":
    mi_set = {1}
    if mi_set:
        print (True)
    else:
        print(False)

