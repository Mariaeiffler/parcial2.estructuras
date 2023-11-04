from prueba_menu import *
from Hotel_prueba import *

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

if __name__ == "__main__":
    tipo='perro'
    valTipoEmpleado (tipo,mi_diccionario)
