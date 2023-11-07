from Persona import Persona
from Estadisticas import *
from nodo import NodoTarea

class Gerente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena, tipo):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo = tipo
    
    def asignarTarea(self,tareas:dict,empleados:dict):
        '''Esta función permite la asignación de tareas a los empleados correspondientes. Las tareas poseen un nivel de importancia para indicar la urgencia de la misma'''
        llaves=list(tareas.keys())
        tipo=input('{} \n Ingrese el tipo de personal al que le quiere asignar una tarea: '.format(llaves))
        tipo=valTipoEmpleado(tipo,tareas)
        for i, tarea in enumerate (tareas[tipo]['tareas']):
            print (F"{i} - {tarea}")
        imprimir1='Ingrese la tarea que desea asignar: '
        opcionAsignar=input(imprimir1) 
        opcionAsignar=valOpcAsignacion(opcionAsignar,tareas,tipo,'tareas',imprimir1)
        for i, personal in enumerate (tareas[tipo]['empleados']):
            print (F"{i} - {personal}")
        imprimir2= 'Ingrese el número del usuario del empleados al que le desea asignar la tarea: '
        empleadoAsignar=input(imprimir2)
        empleadoAsignar=valOpcAsignacion(empleadoAsignar,tareas,tipo,'empleados',imprimir2)
        imprimir3='Error. Ingrese como nivel de importancia 1, 2 o 3 (siendo 1 el más urgente): '
        pregImportancia=input('Niveles de importancia: 1,2,3 (siendo 1 el más urgente). \n Ingrese la importancia de la tarea a realizar: ')
        importancia=val_opc(pregImportancia,1,3,imprimir3)
        imprimir='Desea realizar la tarea ahora? (ingrese "si" o "no"): '
        elije=input(imprimir)
        elije=valSiNo(elije,imprimir)
        if elije:
            nodoNuevo=NodoTarea(opcionAsignar,importancia)
            persona=empleados.get(empleadoAsignar) #chequear que me dice que es un string
            persona.tareasPendientes.agregarNodoTarea(nodoNuevo)
            print ('La tarea se ha generado con exito')
        else: 
            print ('La acción se ha cancelado')
        return
    
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
        '''Esta función crea un inventario con todos los empleados'''
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
        '''Esta función crea la nomina de cliente en el hotel'''
        if len(dic) != 0:
            print('Los clientes del hotel son: ')
            for cliente in dic:
                print(dic.get(cliente))
        else:
            print('El hotel todavía no tiene clientes')
        return
    
    def historialBajasEmpleados(self,bajas:set):
        for empleado in bajas:
            print (empleado)
        return
