from Persona import Persona
from Estadisticas import *

class Gerente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena, tipo):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo = tipo
        
    def obtener_estadisticas(self, lista, array):
        '''Esta función permite almacenar las estadisticas en el archivo de texto'''
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
        
    def inv_empleados(dic:dict):
        '''Esta función contiene un inventario de todos los empleados'''
        list_a = []
        list_b = []
        if len(dic)+1 != 0:
            for clave in dic:
                if dic.get(clave).tipo != 'gerente':
                    if dic.get(clave).fecbaja == None:
                        list_a.append(dic.get(clave))
                    if dic.get(clave).fecbaja != None:
                        list_b.append(dic.get(clave))
        if len(list_a) != 0:
            print('Los empleados activos son: ')
            for emp in list_a:
                print(emp)
        else:
            print('No hay empleados activos')
        if len(list_b) != 0:
            print('Los empleados dados de baja son: ')
            for emp in list_b:
                print(emp)
        else:
            print('No hay empleados dados de baja ')
        return
    
    def nomina_clientes(dic:dict):
        '''Esta función contiene la nomina de cliente en el hotel'''
        if len(dic) != 0:
            print('Los clientes del hotel son: ')
            for cliente in dic:
                print(dic.get(cliente))
        else:
            print('El hotel todavía no tiene clientes')
        return