from datetime import datetime
from Persona import Persona
class Personal(Persona):
    def __init__(self,nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado,fecalta,tipo,fecbaja: None):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
        self.fecalta = datetime.now()
        self.tip=tipo
        
    def bajas(self):
        self.fechabaja = datetime.now()

    # def tareas(self):
    
    # def ingreso(self):
    
    # def egreso (self):
    
    
    
