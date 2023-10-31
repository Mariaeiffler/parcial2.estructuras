from datetime import datetime
from Persona import Persona
from nodo import Nodo
from list_enlazada import Lista_Enlazada
from Tareas_Empleados import tareas_empleados

class Personal(Persona):
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
        
    # def ingreso(self):
    
    # def egreso (self):
    
    
    
