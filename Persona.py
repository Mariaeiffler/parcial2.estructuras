class Persona():
    def _init_(self,nombre,dni,direccion,contacto,fecha_nac,mail):
        self.nombre=nombre
        self.dni=dni
        self.direccion=direccion
        self.contacto=contacto
        self.fecha_nac=fecha_nac
        self.mail=mail
        
    def _str_(self):
        cadena=''
        cadena='La persona llamada {}, nacio el {}, tiene DNI {}, su direccion es {}, la informacion de contacto es {} y el mail es {}'.format(self.nombre,self.fecha_nac,self.dni,self.direccion,self.contacto,self.mail)
        return cadena
    
    def _eq_(self, personita): #es necesario?
        if id(self)==id(personita):
             return True
        elif self.ident==personita.ident:
                return True
        else:  return False
        
    

        