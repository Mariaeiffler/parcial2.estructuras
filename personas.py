class Persona():
    def _init_(self,nombre,dni,direccion,contacto,fecha_nac):
        self.nombre=nombre
        self.dni=dni
        self.direccion=direccion
        self.contacto=contacto
        self.fecha_nac=fecha_nac
        
    def _str_(self):
        cadena=''
        cadena='La persona llamada {}, nacio el {}, tiene DNI {}, su direccion es {} y la informacion de contacto es {}'.format(self.nombre,self.fecha_nac,self.dni,self.direccion,self.contacto)
        return cadena
    
    def _eq_(self, personita): #es necesario?
        if id(self)==id(personita):
             return True
        elif self.ident==personita.ident:
                return True
        else:  return False
        
    
class Personal(Persona):
    def __init__(self,nombre,dni,direccion,contacto,fecha_nac):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac)
    #def altas(self):
        # cuando se contrata un nuevo empleado que se agregue a la estructura de datos utlizada
    #def bajas(self):
        # cuando se despide un empleado que se agregue a la estructura de datos utlizada
    # def tareas(self):
    # def ingreso(self):
    # def egreso (self):
        