from Estadisticas import *
from Nodo import NodoTarea
from Personal import Personal

class Gerente(Personal):
    def __init__(self,nombre,usuario,dni,contacto,fecha_nac,mail,contrasena, tipo,fecalta=datetime.now(),fecbaja=None):
        super().__init__(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,tipo,fecalta,fecbaja)
    
    def asignarTarea(self,tareas:dict,empleados:dict):
        '''Esta función permite la asignación de tareas a los empleados correspondientes. Las tareas poseen un nivel de importancia para indicar la urgencia de la misma'''
        
        llaves=list(tareas.keys())
        tipo=input('{} \n Ingrese el tipo de personal al que le quiere asignar una tarea: '.format(llaves))
        tipo=valTipoEmpleado(tipo,tareas)
        for i, tarea in enumerate (tareas[tipo]['tareas']):
            print (F"{i} - {tarea}")
        imprimir1='Ingrese la tarea que desea asignar: '
        opcionAsignar=input(imprimir1) 
        opcionAsignar=valOpcAsignacion(opcionAsignar,tareas,tipo,'tareas')
        if len(tareas[tipo]['empleados'])==0:
            print('No hay empleados disponibles para realizar estas tareas.')
        else:
            for i, personal in enumerate (tareas[tipo]['empleados']):
                print (F"{i} - {personal}")
            imprimir2= 'Ingrese el número del usuario del empleados al que le desea asignar la tarea: '
            empleadoAsignar=input(imprimir2)
            empleadoAsignar=valOpcAsignacion(empleadoAsignar,tareas,tipo,'empleados')
            imprimir3='Error. Ingrese como nivel de importancia 1, 2 o 3 (siendo 1 el más urgente): '
            pregImportancia=input('Niveles de importancia: 1,2,3 (siendo 1 el más urgente). \n Ingrese la importancia de la tarea a realizar: ')
            importancia=val_opc(pregImportancia,1,3,imprimir3)
            imprimir='Desea asignar la tarea ahora? (ingrese "si" o "no"): '
            elije=input(imprimir)
            elije=valSiNo(elije,imprimir)
            if elije:
                nodoNuevo=NodoTarea(opcionAsignar,importancia)
                persona=empleados.get(empleadoAsignar) 
                persona.tareasPendientes.agregarNodoTarea(nodoNuevo)
                print ('La tarea se ha generado con exito.')
            else: 
                print ('La acción se ha cancelado.')
        return
        
    def obtener_estadisticas(self, lista, array, clientes:dict):
        '''Esta función permite almacenar las estadisticas en el archivo de texto para su lectura'''
        
        ocupa = ocupacion (lista)
        ocupa_th = ocupacion_tipohab(lista)
        rec = rec_diaria(array)
        cli = cant_clientes_tipo(clientes)
        try:
            with open('Estadisticas.txt', "w") as archivo:
                archivo.write(ocupa)
                archivo.write(ocupa_th)
                archivo.write(rec)
                archivo.write(cli)
        except Exception:
            pass
        
    def inv_empleados(self, dic:dict, bajasEmpleados:set):
        '''Esta función crea un inventario con todos los empleados y lo muestra en un archivo de texto'''
        
        list_a = []
        list_b = []
        if len(dic)+1 != 0:
            for clave in dic:
                if dic.get(clave).tipo != 'gerente':
                    list_a.append(dic.get(clave))
        if len(bajasEmpleados)+1 != 0:
            for emp in bajasEmpleados:
                list_b.append(emp)
        try:
            with open('InventarioEmpleados.txt', "w") as archivo:
                if len(list_a) != 0:
                    archivo.write('Los empleados activos son:')
                    archivo.write('\n')
                    for emp in list_a:
                        archivo.write(emp.__str__())
                        archivo.write('\n')
                else:
                    archivo.write('No hay empleados activos')
                if len(list_b) != 0:
                    archivo.write('\n')
                    archivo.write('Los empleados dados de baja son:')
                    archivo.write('\n')
                    for emp in list_b:
                        archivo.write(emp.__str__())
                        archivo.write('\n')
                else:
                    archivo.write('No hay empleados dados de baja')
        except Exception:
            pass          
        return
    
    def nomina_clientes(self, dic:dict):
        '''Esta función crea la nomina de cliente en el hotel y lo muestar en un archivo de texto'''
        
        try:
            with open('NominaClientes.txt', "w") as archivo:
                if len(dic) != 0:
                    archivo.write('Los clientes del hotel son: ')
                    archivo.write('\n')
                    for cliente in dic:
                        archivo.write(dic.get(cliente).__str__())
                        archivo.write('\n')
                else:
                    archivo.write('El hotel todavía no tiene clientes')
        except Exception:
            pass
        return
    
    def historialBajasEmpleados(self,bajas:set):
        '''Esta funcion muestra lo empleados que se dieron de baja en el hotel. Los mismos se almacenan en un set'''
        
        try:
            with open('HistorialBajasEmpleados.txt', "w") as archivo:
                for empleado in bajas:
                    archivo.write(empleado.__str__())
                    archivo.write('\n')
        except Exception:
            pass
        return
    
    def historial_reservas(self, reservas:dict):
        ''''Esta funcion muestra todas las reservas del hotel en un archivo de texto'''
        
        try:
            with open('HistorialReservas.txt', "w") as archivo:
                for reserva in reservas:
                    archivo.write(reservas.get(reserva).__str__())
                    archivo.write('\n')
        except Exception:
            pass
                
    def crearEmpleado(self,clientes:dict,empleados:dict,tareas:dict):
        '''Esta función le permite al gerente crear un empleado'''
        
        nombre,usuario,dni,contacto,fecha_nac,mail,contrasena = infoPersonas (clientes,empleados)
        llaves=list(tareas.keys())
        tipo=input('Ingrese el tipo al que pertenecera el empleado {}: \n'.format(llaves))
        tipo=valTipoEmpleado(tipo,tareas)
        if tipo == 'gerente':
            empleado=Gerente(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,tipo)
        else:
            empleado=Personal(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,tipo)
        empleados[empleado.usuario]=empleado
        tareas[tipo]['empleados'].append(empleado.usuario)
        print ('El empleado se a creado con éxito.')
        
    def bajaEmpleado(self,empleados:dict,tareas:dict,bajasEmpleados:dict):
        '''Esta funcion le permite al gerente dar de baja a un empleado'''
        
        usuarioBaja=input('Ingrese el usuario del empleado que desea dar de baja: ')
        usuarioBaja=valExiUsu(usuarioBaja,empleados)
        imprimir='¿Desea dar de baja definitivamente al empleado? (ingrese "si" o "no"): '
        elije=input(imprimir)
        elije=valSiNo(elije,imprimir)
        if elije:
            empleado=empleados.get(usuarioBaja)
            empleado.bajas()
            tareas[empleado.tipo]['empleados'].remove(empleado.usuario)
            empleados.pop(empleado.usuario)
            bajasEmpleados.add(empleado)
            print('El empleado ha sido eliminado con éxito')
        else:
            print('La acción se ha cancelado.')
        
