from prueba_menu import *
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

mili=

if __name__ == "__main__":
    mi_set = {1, 2, 3, 4, 5}
    for i in mi_set:
        print (i)

