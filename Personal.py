from datetime import datetime
from Persona import Persona
from nodo import Nodo
from list_enlazada import Lista_Enlazada
from Tareas_Empleados import tareas_empleados

class Personal(Persona):
    registros= []
    def __init__(self,nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado,fecalta,tipo,fecbaja: None):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
        self.fecalta = datetime.now()
        self.tipo=tipo
        self.Tareas=Lista_Enlazada()
        
    def bajas(self):
        self.fechabaja = datetime.now()

    def tareas(self): 
        print(tareas_empleados)
        opcion=input('Ingrese el número de tarea que quiere asignar: ') #chequear que la opcion sea la correcta
        prioridad= input ('Ingrese la prioridad (1,2 o 3): ') #chequear que sea 1,2 o 3
        
  
    
    # def egreso (self):
    
    
    
    def ingreso(self,nombre): #ver si esta bien lo de la list de registros (preguntarle a ian!!!!)
        ahora= datetime.now()
        registro= {'tipo de registro':'ingreso', 'fecha_hora': ahora, 'nombre': self.nombre} #noc lo del nombre si esta bien
        registros.append(registro)
        print('Se registró el ingreso de {} a las {}'.format(self.nombre,ahora))
    def egreso(self, nombre):
        ahora= datetime.now()
        registro= {'tipo de registro': 'egreso', 'fecha_hora': ahora, 'nombre':self.nombre}
        registros.append(registro)
        print('Se registró el egreso de {} a las {}'.format(ahora,self.nombre))

   

    def mostrar_registros():
        for registro in registros:
            tipo = registro["tipo de registro"]
            fecha_hora = registro["fecha_hora"]
            nombre = registro["nombre"]
            print('Se registró el {} de {} a las {}'.format(tipo,nombre,fecha_hora))

    def menu_registros():
        while True:
            print('Control de Ingreso y Egreso de Personal de Hotel')
            print("1. Registrar Ingreso")
            print("2. Registrar Egreso")
            print("3. Mostrar Registros")
            print("4. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre_personal = input("Ingresa el nombre del personal que ingresa: ")
                ingreso(nombre_personal)
            elif opcion == "2":
                nombre_personal = input("Ingresa el nombre del personal que egresa: ")
                egreso(nombre_personal)
            elif opcion == "3":
                mostrar_registros()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")


        
