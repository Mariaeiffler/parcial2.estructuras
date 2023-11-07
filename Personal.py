from datetime import datetime
from Persona import Persona
from nodo import NodoTarea
from list_enlazada import *
from Tareas_Empleados import tareas_empleados
from Validaciones import *
from Funciones import *
from Pilas import Pila

class Personal(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo,fecalta=datetime.now(),fecbaja=None):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.fecalta = fecalta
        self.tipo=tipo
        self.fecbaja=fecbaja
        self.tareasPendientes=Lista_Enlazada()
        self.registro = []
        self.tareasRealizadas=Pila()
        
    def __str__(self):
        if self.fecbaja == None:
            return ('El empleado de nombre {} y dni, de tipo {}, se dió de alta el dia {} y sigue vigente'.format(self.nombre, self.dni, self.fecalta))
        else:
            return('El empleado de nombre {} y dni, de tipo {}, se dió de alta el dia {} y de baja el dia {}'.format(self.nombre, self.dni, self.fecalta, self.fecbaja))
        
    def bajas(self):
        '''Esta función da de baja a un empleado'''
        self.fechabaja = datetime.now()

    def realizarTareas(self):
        '''Esta función permite realizar las tareas pendientes'''
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

    # def posicion_registro(self,u,ingresos_egresos:list()):
    #     u=self.usuario
    #     cont=0
    #     for lista in ingresos_egresos:
    #         if lista[0]==u:
    #             return cont
    #         cont+=1
            
    def registrar_ingreso(self):
        '''Esta función registra el ingreso de un empleado'''
        self.registro.append([datetime.now()])
        return
        
    def registrar_egreso(self): 
        '''Esta función registra el egreso de un empleado'''
        print(self.registro)
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

    # def mostrar_registros(self):
    #     for registro in self.registros:
    #         tipo = registro["tipo de registro"]
    #         fecha_hora = registro["fecha_hora"]
    #         nombre = registro["nombre"]
    #         print('Se registró el {} de {} a las {}'.format(tipo,nombre,fecha_hora))

    # def menu_registros(self):
    #     while True:
    #         print('Control de Ingreso y Egreso de Personal de Hotel')
    #         print("1. Registrar Ingreso")
    #         print("2. Registrar Egreso")
    #         print("3. Mostrar Registros")
    #         print("4. Salir")
            
    #         opcion = input("Selecciona una opción: ")
            
    #         if opcion == "1":
    #             nombre_personal = input("Ingresa el nombre del personal que ingresa: ")
    #             self.ingreso(nombre_personal)
    #         elif opcion == "2":
    #             nombre_personal = input("Ingresa el nombre del personal que egresa: ")
    #             self.egreso(nombre_personal)
    #         elif opcion == "3":
    #             self.mostrar_registros()
    #         elif opcion == "4":
    #             break
    #         else:
    #             print("Opción no válida. Por favor, selecciona una opción válida.")
                
        # def agregarTarea (self):
        




