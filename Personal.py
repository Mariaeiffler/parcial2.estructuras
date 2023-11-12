from datetime import datetime
from Persona import Persona
from nodo import NodoTarea
from list_enlazada import *
from Tareas_Empleados import tareas_empleados
from Funciones import *
from Pilas import Pila
from Cola import Cola

class Personal(Persona):
    def __init__(self,nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,tipo,fecalta=datetime.now(),fecbaja=None):
        super().__init__(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena)
        self.fecalta = fecalta
        self.tipo=tipo
        self.fecbaja=fecbaja
        self.tareasPendientes=Lista_Enlazada()
        self.registro = []
        self.tareasRealizadas=Pila()
        
    def __str__(self):
        if self.fecbaja == None:
            return ('El empleado de nombre {} y dni, de tipo {}, se dió de alta el dia {} y sigue vigente'.format(self.nombre, self.dni, self.fecalta.strftime('%d/%m/%Y')))
        else:
            return('El empleado de nombre {} y dni, de tipo {}, se dió de alta el dia {} y de baja el dia {}'.format(self.nombre, self.dni, self.fecalta.strftime('%d/%m/%Y'), self.fecbaja.strftime('%d/%m/%Y')))
        
    def bajas(self):
        '''Esta función permite dar de baja a un empleado''' ### ver
        self.fecbaja = datetime.now()

    def realizarTareas(self,ordenes:Cola):
        '''Esta función permite realizar las tareas pendientes'''
        if self.tipo=='cocina':
            opcion=input('Desea: \n 1. Realizar una tarea asignada por el gerente \n 2. Realizar un pedido del buffet \n') 
            imprimir1='\n Error. Desea: \n 1. Realizar una tarea asignada por el gerente \n 2. Realizar un pedido del buffet \n'
            opcion=val_opc(opcion,1,2,imprimir1)
            match opcion:
                case 1:
                    if self.tareasPendientes.head:
                        print('La Tarea a realizar es: {}'.format(self.tareasPendientes.head.__str__()))
                        imprimir='Desea realizar la tarea ahora? (ingrese "si" o "no"): '
                        elije=input(imprimir)
                        elije=valSiNo(elije,imprimir)
                        if elije:
                            self.tareasRealizadas.apilar(self.tareasPendientes.head.valor)
                            self.tareasPendientes.eliminarPrimero() 
                            print('La tarea ha sido marcada como realizada.')
                        else:
                            print('La tarea no se ha realizado')
                    else:
                        print('No hay tareas pendientes')
                   
                case 2:
                    print('El pedido a realizar es: {}'.format(ordenes.mostrarPrimero()))
                    imprimir='Desea realizar el pedido ahora? (ingrese "si" o "no"): '
                    elije=input(imprimir)
                    elije=valSiNo(elije,imprimir)
                    if elije:
                        ordenes.desencolar()
                        print('La tarea se ha realizado con éxito.')
                    else:
                        print ('La acción se ha cancelado')
        else:
            if self.tareasPendientes.head:
                print('La Tarea a realizar es: {}'.format(self.tareasPendientes.head.__str__()))
                imprimir='Desea realizar la tarea ahora? (ingrese "si" o "no"): '
                elije=input(imprimir)
                elije=valSiNo(elije,imprimir)
                if elije:
                    self.tareasRealizadas.apilar(self.tareasPendientes.head.valor)
                    self.tareasPendientes.eliminarPrimero() 
                    print('La tarea ha sido marcada como realizada.')
                else:
                    print('La tarea no se ha realizado')
        return
                
    def visualizarTareaAnterior (self):
        '''Esta función muestra la última tarea realizada'''
        tarea=self.tareasRealizadas.obtenerUltimo()
        print('La última tarea que realizó fue: {}'.format(tarea))
            
    def registrar_ingreso(self):
        '''Esta función registra el ingreso de un empleado'''
        self.registro.append([datetime.now()])
        return
        
    def registrar_egreso(self): 
        '''Esta función registra el egreso de un empleado'''
        if len(self.registro[len(self.registro)-1]) == 1:
            self.registro[len(self.registro)-1].append(datetime.now())
            print('Su egreso se registró con éxito')
            print(self.registro)
        else:
            print('Error, no registró el ingreso')
        return
      
    def egreso(self, nom):
        '''Esta función guarda el egreso de un empleado'''
        self.nom=nom
        ahora= datetime.now()
        registro= {'tipo de registro': 'egreso', 'fecha_hora': ahora, 'nombre':self.nom}
        self.registros.append(registro)
        print('Se registró el egreso de {} a las {}'.format(ahora,self.nombre))

        




