from Persona import Persona
from Estadisticas import *

class Gerente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena, tipo):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo = tipo
        
    def obtener_estadisticas(self, lista, array):
        ocupa = ocupacion (lista)
        ocupa_th = ocupacion_tipohab(lista)
        rec = rec_diaria(array)
        try:
            with open('Estadisticas.txt', "w") as archivo:
                archivo.write(ocupa)
                archivo.write(ocupa_th)
                archivo.write(rec)
        except Exception:
            pass