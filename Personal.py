from datetime import datetime
from Persona import Persona
from nodo import NodoTarea
from list_enlazada import *
from Tareas_Empleados import tareas_empleados

class Personal(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo,fecalta=datetime.now(),fecbaja=None):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.fecalta = fecalta
        self.tipo=tipo
        self.fecbaja=fecbaja
        self.tareasPendientes=Lista_Enlazada()
        
    def __str__(self):
        if self.fecbaja == None:
            return ('El empleado de nombre {} y dni, de tipo {}, se dió de alta el dia {} y sigue vigente'.format(self.nombre, self.dni, self.fecalta))
        else:
            return('El empleado de nombre {} y dni, de tipo {}, se dió de alta el dia {} y de baja el dia {}'.format(self.nombre, self.dni, self.fecalta, self.fecbaja))
        
    def bajas(self):
        self.fechabaja = datetime.now()

    def tareas(self): 
        print(tareas_empleados)
        opcion=input('Ingrese el número de tarea que quiere asignar: ') #chequear que la opcion sea la correcta
        prioridad= input ('Ingrese la prioridad (1,2 o 3): ') #chequear que sea 1,2 o 3
        
    #FALTA VERIFICAR QUE ANDEN BIEN INGRESOS Y EGRESOS Y LOS DOS METODOS DE REGISTROS
    #Falta ver si se appendean a regiastros registro.
    def ingreso(self,nom): #ver si esta bien lo de la list de registros (preguntarle a ian!!!!)
        self.nom=nom
        ahora= datetime.now()
        registro= {'tipo de registro':'ingreso', 'fecha_hora': ahora, 'nombre': self.nom} #noc lo del nombre si esta bien
        self.registros.append(registro)
        print('Se registró el ingreso de {} a las {}'.format(self.nombre,ahora))
        
    def egreso(self, nom):
        self.nom=nom
        ahora= datetime.now()
        registro= {'tipo de registro': 'egreso', 'fecha_hora': ahora, 'nombre':self.nom}
        self.registros.append(registro)
        print('Se registró el egreso de {} a las {}'.format(ahora,self.nombre))

   
    def mostrar_registros(self):
        for registro in self.registros:
            tipo = registro["tipo de registro"]
            fecha_hora = registro["fecha_hora"]
            nombre = registro["nombre"]
            print('Se registró el {} de {} a las {}'.format(tipo,nombre,fecha_hora))

    def menu_registros(self):
        while True:
            print('Control de Ingreso y Egreso de Personal de Hotel')
            print("1. Registrar Ingreso")
            print("2. Registrar Egreso")
            print("3. Mostrar Registros")
            print("4. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre_personal = input("Ingresa el nombre del personal que ingresa: ")
                self.ingreso(nombre_personal)
            elif opcion == "2":
                nombre_personal = input("Ingresa el nombre del personal que egresa: ")
                self.egreso(nombre_personal)
            elif opcion == "3":
                self.mostrar_registros()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
                
        # def agregarTarea (self):
        




